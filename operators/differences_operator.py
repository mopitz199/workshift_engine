import copy
from operators.assignation_operator import AssignationOperator
from operators.range_operator import RangeOperator


class DifferencesOperator(object):
    """
    Class to check and process the differences
    after all the assigns and unasigns
    """

    def __init__(self, db):
        self.db = db

    def remove_range_on_created_range(self, remove_range, assign):
        response = []
        if hasattr(assign, 'was_created'):
            ranges = assign.was_created
        else:
            differences = assign.get_differences()
            ranges = differences['was_created']

        for was_created_range in ranges:
            was_created_range, _ = was_created_range - remove_range
            if _:
                raise Exception
            if was_created_range is not None:
                response.append(was_created_range)
        return response

    def remove_range_on_new_assign(self, remove_range, assign):
        response = []
        if hasattr(assign, 'was_created'):
            ranges = assign.was_created
        else:
            ranges = [assign.range_obj]

        for aux_range in ranges:
            aux_range, _ = aux_range - remove_range
            if _:
                raise Exception
            if aux_range is not None:
                response.append(aux_range)
        return response

    def clean_updated_assign(self, assign, assigns):
        if hasattr(assign, 'was_deleted'):
            was_deleted = assign.was_deleted
        else:
            differences = assign.get_differences()
            was_deleted = differences['was_deleted']
        for aux_assign in assigns:
            are_compatible = AssignationOperator.are_compatible(
                assign, aux_assign)

            if assign != aux_assign and are_compatible:
                for del_range in was_deleted:
                    intersection = RangeOperator.get_intersection(
                        del_range,
                        aux_assign.range_obj)
                    del_range, new_range = del_range - intersection
                    if new_range:
                        was_deleted.append(new_range)

                    if aux_assign.is_in_real_db():
                        ranges = self.remove_range_on_created_range(
                            intersection,
                            aux_assign)
                        aux_assign.was_created = ranges
                    else:
                        ranges = self.remove_range_on_new_assign(
                            intersection,
                            aux_assign)
                        aux_assign.was_created = ranges

        assign.was_deleted = was_deleted

    def process_differences(self):
        total = {}
        assigns_created = self.db.get_assigns_to_by_created_by_hash()
        assigns_updated = self.db.get_assigns_to_by_updated_by_hash()

        for updated_assign in self.db.to_be_updated:
            hash_key = self.db.hash_function(updated_assign)
            to_be_created = assigns_created.get(hash_key, [])
            to_be_updated = assigns_updated.get(hash_key, [])
            assigns = to_be_created + to_be_updated
            self.clean_updated_assign(updated_assign, assigns)

        for assign in self.db.to_be_updated:
            person_id = str(assign.person_id)
            if person_id not in total:
                total[person_id] = []

            differences = assign.get_differences()
            if hasattr(assign, 'was_created'):
                total[person_id] += assign.was_created
            else:
                total[person_id] += differences['was_created']

            if hasattr(assign, 'was_deleted'):
                total[person_id] += assign.was_deleted
            else:
                total[person_id] += differences['was_deleted']

        for assign in self.db.to_be_created:
            person_id = str(assign.person_id)
            if person_id not in total:
                total[person_id] = []

            if hasattr(assign, 'was_created'):
                total[person_id] += assign.was_created
            else:
                total[person_id].append(assign.range_obj)

        for assign in self.db.to_be_deleted:
            person_id = str(assign.person_id)
            if person_id not in total:
                total[person_id] = []
            total[person_id].append(assign.range_obj)

        return self.compress_differences(total)

    def compress_differences(self, differences):
        response = {}
        for key in differences:
            range_list = differences[key]
            response[key] = RangeOperator.compress_range_list(range_list)
        return response
