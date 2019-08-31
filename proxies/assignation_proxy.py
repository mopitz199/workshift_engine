import copy

from datetime import timedelta

from proxies.base_proxy import Proxy
from operators.assignation_operator import AssignationOperator
from utils.range import Range

from database.db_extension import DBExtension


class AssignationProxy(Proxy, DBExtension):
    """This class is to map the attributes of an assignation and their relations.
    Some requirements from the assignation are:

    * id: The id of the assignation (if is created in the database)
    * starting_date: The starting date of the assignation
    * ending_date: The ending date of the assignation
    * workshift_id: The workshift id of the assignation
    * workshift: The workshift obj
    * person_id: The person if of the assignation
    * person: The person obj
    * start_day: The starting day of the assignation

    """

    def __init__(self, obj, *args, **kwargs):
        super(AssignationProxy, self).__init__(obj)
        self.range_obj = Range(self.starting_date, self.ending_date)
        self.init_range = copy.copy(self.range_obj)
        self.init_start_day = getattr(self.obj, 'start_day', None)

    def __len__(self):
        return len(self.range_obj)

    def __repr__(self):
        return "{}".format(self.range_obj)

    def __str__(self):
        return "{}".format(self.range_obj)

    def __setattr__(self, attr, val):
        super(AssignationProxy, self).__setattr__(attr, val)
        if attr in ['starting_date', 'ending_date']:
            setattr(self.range_obj, attr, val)
        if attr in ['range_obj']:
            super(AssignationProxy, self).__setattr__(attr, val)
            setattr(self, 'starting_date', self.range_obj.starting_date)
            setattr(self, 'ending_date', self.range_obj.ending_date)

    def __add__(self, other_assign):
        if AssignationOperator.can_be_joined(self, other_assign):
            starting_date = self.range_obj.starting_date
            other_starting_date = other_assign.range_obj.starting_date

            if starting_date > other_starting_date:
                start_day = other_assign.start_day
                self.start_day = start_day

            self.range_obj += other_assign.range_obj

        return self

    def __sub__(self, other_assign):
        pass

    def has_change(self):
        return (self.init_range != self.range_obj or
                self.start_day != self.init_start_day)

    def get_differences(self):
        """
        This function return the difference of range
        between the init range and the current range
        """

        init_range = self.init_range
        range_obj = self.range_obj

        resp = {
            'was_deleted': [],
            'was_created': []}

        if init_range.starting_date != range_obj.starting_date:

            min_date = min(init_range.starting_date,
                           range_obj.starting_date)

            max_date = max(init_range.starting_date - timedelta(days=1),
                           range_obj.starting_date - timedelta(days=1))

            left_range = Range(min_date, max_date)

            if init_range.starting_date > range_obj.starting_date:
                resp['was_created'].append(left_range)
            else:
                resp['was_deleted'].append(left_range)

        if init_range.ending_date != range_obj.ending_date:

            min_date = min(init_range.ending_date + timedelta(days=1),
                           range_obj.ending_date + timedelta(days=1))

            max_date = max(init_range.ending_date,
                           range_obj.ending_date)

            right_range = Range(min_date, max_date)

            if init_range.ending_date > range_obj.ending_date:
                resp['was_deleted'].append(right_range)
            else:
                resp['was_created'].append(right_range)

        return resp
