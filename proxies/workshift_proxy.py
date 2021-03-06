import copy

from datetime import timedelta

from database.db_extension import DBExtension
from proxies.base_proxy import Proxy
from assignation.operators.assignation_operator import AssignationOperator
from utils.range import Range


class WorkShiftProxy(Proxy, DBExtension):

    def __init__(self, obj, *args, **kwargs):
        super(WorkShiftProxy, self).__init__(obj)

    def get_dict_days(self):
        """Get days in a dict where the keys are a
        date or a number day identification"""

        days = self.get_days()
        response = {}
        for day in days:
            if self.workshift_type == 'weekly':
                key = "{}".format(day.day_number)
            elif self.workshift_type == 'cyclic':
                key = "{}".format(day.day_number)
            elif self.workshift_type == 'manually':
                key = "{}".format(day.date)
            else:
                raise Exception('Unknown workshift type')

            response[key] = day

        return response

    def get_days(self):
        return self.days
