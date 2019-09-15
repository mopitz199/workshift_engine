from datetime import datetime, timedelta


class CycleAssignationFacade(object):

    def __init__(self, assignation_data):
        self.assignation_data = assignation_data

    def get_first_date_of_day_number(self, day_number):
        starting_day = self.assignation_data['starting_day']
        total_days = self.get_total_days()
        starting_date = self.assignation_data['starting_date']

        if starting_day > day_number:
            day = total_days - starting_day + day_number
        else:
            day = day_number - starting_day

        return starting_date + timedelta(days=day)

    def get_day_data(self, day_number):
        return self.assignation_data['workshift']['days'][day_number]

    def get_days(self):
        return self.assignation_data['workshift']['days']

    def get_ending_date(self):
        return self.assignation_data['ending_date']

    def get_total_days(self):
        return self.assignation_data['workshift']['total_days']
