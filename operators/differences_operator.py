import copy
from operators.assignation_operator import AssignationOperator


class DifferencesOperator(object):
    """
    Class to check and process the differences
    after all the assigns and unasigns
    """

    def __init__(self, db):
        self.db = db

    def clean_updated_assign(self, assign, assigns):
        response = []
        differences = assign.get_differences()
        for aux_assign in assigns:
            are_compatible = AssignationOperator.are_compatible(
                assign, aux_assign)

            if assign != aux_assign and are_compatible:
                was_deleted = differences['was_deleted']
                for del_range in was_deleted:
                    del_range, new_range = del_range - aux_assign.range_mapper
                    response.append(del_range)
                    if new_range:
                        response.append(new_range)
        if not response:
            response = differences['was_deleted'] + differences['was_created']

        return response

    def process_differences(self):
        total = {}
        assigns_created = self.db.get_assigns_to_by_created_by_hash()
        assigns_updated = self.db.get_assigns_to_by_updated_by_hash()

        for updated_assign in self.db.to_be_updated:
            hash_key = self.db.hash_function(updated_assign)
            to_be_created = assigns_created.get(hash_key, [])
            to_be_updated = assigns_updated.get(hash_key, [])
            assigns = to_be_created + to_be_updated
            ranges = self.clean_updated_assign(updated_assign, assigns)
            person_id = str(updated_assign.person_id)
            if person_id not in total:
                total[person_id] = []
            total[person_id] += ranges

        for deleted_assign in self.db.to_be_deleted:
            person_id = str(deleted_assign.person_id)
            if person_id not in total:
                total[person_id] = []
            total[person_id].append(deleted_assign.range_mapper)

        for created_assign in self.db.to_be_created:
            person_id = str(created_assign.person_id)
            if person_id not in total:
                total[person_id] = []
            total[person_id].append(created_assign.range_mapper)

        return total
