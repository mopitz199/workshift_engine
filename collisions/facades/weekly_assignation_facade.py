from collisions.utils import Util


class WeeklyAssignationFacade(object):

    def __init__(self, assignation):
        self.assignation = assignation

    def get_day(self, day_name):
        dict_days = self.assignation.workshift_proxy.get_dict_days()
        return dict_days[day_name]

    def get_next_day_name(self, day_name):
        day_name = int(day_name)
        if day_name == 6:
            return '0'
        else:
            return '{}'.format(day_name + 1)

    def get_prev_day_name(self, day_name):
        day_name = int(day_name)
        if day_name == 0:
            return '6'
        else:
            return '{}'.format(day_name - 1)

    def range_obj_from_day_name(self, day_name, base_date):
        day = self.get_day(day_name)
        starting_time = day.starting_time
        ending_time = day.ending_time
        if starting_time is not None and ending_time is not None:

            return Util.create_range(starting_time, ending_time, base_date)
        else:
            return None
