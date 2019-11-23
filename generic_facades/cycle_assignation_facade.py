from datetime import datetime, timedelta


class CycleAssignationFacade(object):

    def __init__(self, assignation):
        self.assignation = assignation

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
        dict_days = self.assignation.workshift_proxy.get_dict_days()
        return dict_days[day_number]

    def get_days(self):
        return self.assignation.workshift_proxy.get_days()

    def get_total_days(self):
        return self.assignation.workshift_proxy.total_days

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
