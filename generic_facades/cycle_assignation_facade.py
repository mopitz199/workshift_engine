from datetime import datetime, timedelta
from generic_facades.generic_assignation_facade import GenericAssignationFacade
from collisions.utils import Util


class CycleAssignationFacade(GenericAssignationFacade):

    def get_first_date_of_day_number(self, day_number):
        """Get the first date that represent a day number"""

        starting_day = self.assignation.starting_day
        total_days = self.get_total_days()
        starting_date = self.assignation.starting_date

        if starting_day > day_number:
            day = total_days - starting_day + day_number
        else:
            day = day_number - starting_day

        return starting_date + timedelta(days=day)

    def get_day_data(self, day_number):
        str_day_number = str(day_number)
        dict_days = self.assignation.workshift_proxy.get_dict_days()
        return dict_days[str_day_number]

    def get_days(self):
        return self.assignation.workshift_proxy.get_days()

    def get_total_days(self):
        return self.assignation.workshift_proxy.total_workshift_days

    def get_prev_day_number(self, day_number):
        workshift_proxy = self.assignation.workshift_proxy
        total_workshift_days = workshift_proxy.total_workshift_days
        if day_number >= total_workshift_days:
            raise Exception('The day number exceeds the limit')

        if day_number > 0:
            return day_number - 1
        return total_workshift_days - 1

    def get_next_day_number(self, day_number):
        workshift_proxy = self.assignation.workshift_proxy
        total_workshift_days = workshift_proxy.total_workshift_days
        if day_number >= total_workshift_days:
            raise Exception('The day number exceeds the limit')

        if day_number < total_workshift_days - 1:
            return day_number + 1
        return 0

    def simulate_starting_day(self, date_obj):
        """
        To simulate an starting_day in an specific date

        :param assign: An assign proxy object
        :type assign: AssignationProxy
        :param date_obj: The date which want to simulate
        :type date_obj: date

        :rtype: Int
        """
        assign = self.assignation

        if assign.starting_day:
            starting_date = assign.range_obj.starting_date
            delta = timedelta(days=assign.starting_day - 1)
            aux_starting_date = starting_date - delta

            range_days = (date_obj - aux_starting_date).days + 1
            total_days = assign.workshift.total_workshift_days

            return (range_days % total_days) or total_days
        else:
            return None

    def range_obj_from_day_number(self, cycle_day, base_date):
        starting_time = cycle_day.starting_time
        ending_time = cycle_day.ending_time
        if starting_time is not None and ending_time is not None:
            return Util.create_range(starting_time, ending_time, base_date)
        else:
            return None
