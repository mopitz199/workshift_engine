from collisions.utils import Util


class WeeklyAssignationFacade(object):

    def __init__(self, assignation_data):
        self.assignation_data = assignation_data
        self.day_names = ['monday', 'tuesday', 'wednesday',
                          'thursday', 'friday', 'saturday',
                          'sunday']

    def get_day_data(self, day_name):
        return self.assignation_data['workshift']['days'][day_name]

    def get_next_day_name(self, day_name):
        index = self.day_names.index(day_name)
        if index == len(self.day_names) - 1:
            return self.day_names[0]
        else:
            return self.day_names[index + 1]

    def get_prev_day_name(self, day_name):
        index = self.day_names.index(day_name)
        if index == 0:
            last_index = len(self.day_names)
            return self.day_names[last_index - 1]
        else:
            return self.day_names[index - 1]

    def range_obj_from_day_name(self, day_name, base_date):
        data = self.get_day_data(day_name)
        starting_time = data['starting_time']
        ending_time = data['ending_time']
        if starting_time is not None and ending_time is not None:
            return Util.create_range(starting_time, ending_time, base_date)
        else:
            return None
