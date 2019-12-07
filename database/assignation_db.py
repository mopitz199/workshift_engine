from typing import List, Dict

from assignation.operators.assignation_operator import AssignationOperator
from database.generic_database import DB
from proxies.assignation_proxy import AssignationProxy

from database.custom_typings import ProxyAssignationByHashType


class AssignationDB(DB):
    """
    Class to operate instances of AssignationProxy class as a RAM database
    """

    def add(
        self,
        element: AssignationProxy
    ) -> None:
        compatible_list = []
        for deleted_element in self.to_be_deleted:
            intersect = AssignationOperator.are_intersection(
                element,
                deleted_element)

            are_compatible = AssignationOperator.are_compatible(
                element,
                deleted_element
            )

            if intersect and are_compatible:
                compatible_list.append(deleted_element)

        best = AssignationOperator.get_biggest_assign(compatible_list)
        if best:
            best.range_obj = element.range_obj
            best.starting_day = element.starting_day

            self.to_be_deleted.remove(best)
            if best.has_change():
                self.to_be_updated.append(best)
            hash_key = self.hash_function(best)
            if hash_key not in self.db:
                self.db[hash_key] = []
            self.db[hash_key].append(best)
        else:
            super().add(element)

    def hash_function(
        self,
        element: AssignationProxy
    ) -> str:
        """A function to et the key from where we must save and get the data"""

        return '{}_{}'.format(element.workshift_id, element.person_id)

    def get_assigns(
        self,
        assign: AssignationProxy
    ) -> List[AssignationProxy]:
        """
        Get all the assign that has the same workshift and person
        of the given assign
        """

        key = self.hash_function(assign)
        return self.db.get(key, [])

    def assignate(
        self,
        new_assign: AssignationProxy
    ) -> None:
        """
        The main method to assign
        """

        db_assigns = self.get_assigns(new_assign)

        best, others = AssignationOperator.get_candidates(
            new_assign, db_assigns)

        if best:
            best += new_assign
            for other in others:
                best = best + other
                self.remove(other)
            if best.has_change():
                self.update(best)
        else:
            self.add(new_assign)

    def unassign(
        self,
        fake_assign: AssignationProxy
    ) -> None:
        """
        The main method to unassign. In this case, the fake_assign
        is just an AssignationMaper that represent the attributes
        of the range to remove in a specific workshift of a person
        """

        db_assigns = self.get_assigns(fake_assign)
        compatibe_assigns = AssignationOperator.are_multiple_compatible(
            fake_assign, db_assigns)

        for compatibe_assign in compatibe_assigns:
            resp = AssignationOperator.remove(
                compatibe_assign,
                fake_assign.range_obj.starting_date,
                fake_assign.range_obj.ending_date)

            if resp['update']:
                self.update(resp['update'])

            if resp['create']:
                self.add(resp['create'])

            if resp['delete']:
                self.remove(resp['delete'])

    def get_assign_list_by_hash(
        self,
        assign_list: List[AssignationProxy]
    ) -> ProxyAssignationByHashType:
        response = ProxyAssignationByHashType({})
        for assign in assign_list:
            hash_key = self.hash_function(assign)
            if hash_key not in response:
                response[hash_key] = []
            response[hash_key].append(assign)
        return response

    def get_assigns_to_by_updated_by_hash(
        self
    ) -> ProxyAssignationByHashType:
        return self.get_assign_list_by_hash(self.to_be_updated)

    def get_assigns_to_by_deleted_by_hash(
        self
    ) -> ProxyAssignationByHashType:
        return self.get_assign_list_by_hash(self.to_be_deleted)

    def get_assigns_to_by_created_by_hash(
        self
    ) -> ProxyAssignationByHashType:
        return self.get_assign_list_by_hash(self.to_be_created)

    def get_changes_by_hash(
        self
    ) -> Dict[str, ProxyAssignationByHashType]:
        response = {}
        response['updated'] = self.get_assigns_to_by_updated_by_hash()
        response['created'] = self.get_assigns_to_by_created_by_hash()
        response['deleted'] = self.get_assigns_to_by_deleted_by_hash()
        return response
