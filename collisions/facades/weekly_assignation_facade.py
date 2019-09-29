from collisions.utils import Util


class WeeklyAssignationFacade(object):

    def __init__(self, assignation):
        self.assignation = assignation

    def get_day(self, day_number):
        dict_days = self.assignation.workshift_proxy.get_dict_days()
        return dict_days[day_number]

    def get_next_day_number(self, day_number):
        day_number = int(day_number)
        if day_number == 6:
            return '0'
        else:
            return '{}'.format(day_number + 1)

    def get_prev_day_number(self, day_number):
        day_number = int(day_number)
        if day_number == 0:
            return '6'
        else:
            return '{}'.format(day_number - 1)

    def range_obj_from_day_number(self, day_number, base_date):
        day = self.get_day(day_number)
        starting_time = day.starting_time
        ending_time = day.ending_time
        if starting_time is not None and ending_time is not None:

            return Util.create_range(starting_time, ending_time, base_date)
        else:
            return None
