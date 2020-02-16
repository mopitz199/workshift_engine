from datetime import timedelta

from generic_facades.cycle_assignation_facade import CycleAssignationFacade


class CycleDateIterator:
    """An iterator that returns the date of an specific day number
    in cyclic assignation"""

    def __init__(self, assignation, day_number):
        self.facade = CycleAssignationFacade(assignation)
        beginning_date = self.facade.get_first_date_of_day_number(
            day_number
        )
        self.next_date = beginning_date
        self.assignation = assignation
        self.total_days = self.facade.get_total_days()

    def __iter__(self):
        return self

    def __next__(self):
        aux_next_date = self.next_date
        if aux_next_date > self.assignation.ending_date:
            raise StopIteration
        else:
            next_date = self.next_date + timedelta(days=self.total_days)
            self.next_date = next_date
            return aux_next_date
