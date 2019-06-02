import pdb

from database.generic_database import DB
from operators.assignation_operator import AssignationOperator


class AssignationDB(DB):
    """
    Class to operate instances of AssignationMapper class as a RAM database
    """

    def add(self, element):
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
            best.range_mapper = element.range_mapper
            best.start_day = element.start_day

            self.to_be_deleted.remove(best)
            if best.has_change():
                self.to_be_updated.append(best)
            hash_key = self.hash_function(best)
            if hash_key not in self.db:
                self.db[hash_key] = []
            self.db[hash_key].append(best)
        else:
            super().add(element)

    def hash_function(self, element):
        """A function to et the key from where we must save and get the data"""

        return '{}_{}'.format(element.workshift_id, element.person_id)

    def get_assigns(self, assign):
        """
        Get all the assign that has the same workshift and person
        of the given assign
        """

        key = self.hash_function(assign)
        return self.db.get(key, [])

    def assignate(self, new_assign):
        """
        The main method to assign
        """

        db_assigns = self.get_assigns(new_assign)

        best, others = AssignationOperator.get_candidates(
            new_assign, db_assigns)

        if best:
            best += new_assign
            for other in others:
                best += other
                self.remove(other)
            if best.has_change:
                self.update(best)
        else:
            self.add(new_assign)

    def unassign(self, fake_assign):
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
                fake_assign.range_mapper.starting_date,
                fake_assign.range_mapper.ending_date)

            if resp['update']:
                self.update(resp['update'])

            if resp['create']:
                self.add(resp['create'])

            if resp['delete']:
                self.remove(resp['delete'])
