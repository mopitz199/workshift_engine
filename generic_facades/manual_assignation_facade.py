from datetime import datetime, timedelta

from generic_facades.generic_assignation_facade import GenericAssignationFacade
from collisions.utils import Util


class ManualAssignationFacade(GenericAssignationFacade):

    def __init__(self, assignation):
        self.assignation = assignation

    def get_days(self):
        return self.assignation.workshift_proxy.get_days()

    def range_obj_from_day_number(self, manual_day, base_date):
        starting_time = manual_day.starting_time
        ending_time = manual_day.ending_time
        if starting_time is not None and ending_time is not None:
            return Util.create_range(starting_time, ending_time, base_date)
        else:
            return None
