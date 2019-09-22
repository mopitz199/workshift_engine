import copy

from datetime import timedelta

from proxies.base_proxy import Proxy
from assignation.operators.assignation_operator import AssignationOperator
from utils.range import Range


class WorkShiftProxy(Proxy):

    def __init__(self, obj, *args, **kwargs):
        super(WorkShiftProxy, self).__init__(obj)

    def get_dict_days(self):
        days = self.days
        response = {}
        for day in days:
            if self.workshift_type == 'weekly':
                key = day.number_day
            elif self.workshift_type == 'cyclic':
                pass
            elif self.workshift_type == 'manually':
                pass
            else:
                raise Exception('Unknown workshift type')
            
            
            response
