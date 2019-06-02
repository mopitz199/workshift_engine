import copy

from datetime import timedelta

from mappers.mapper import Mapper
from operators.assignation_operator import AssignationOperator
from mappers.range_mapper import Range

from database.db_extension import DBExtension


class AssignationMapper(Mapper, DBExtension):
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
        super(AssignationMapper, self).__init__(obj)
        self.range_mapper = Range(self.starting_date, self.ending_date)
        self.init_range = copy.copy(self.range_mapper)
        self.init_start_day = getattr(self.obj, 'start_day', None)

    def __len__(self):
        return len(self.range_mapper)

    def __repr__(self):
        return "{}".format(self.range_mapper)

    def __str__(self):
        return "{}".format(self.range_mapper)

    def __setattr__(self, attr, val):
        super(AssignationMapper, self).__setattr__(attr, val)
        if attr in ['starting_date', 'ending_date']:
            setattr(self.range_mapper, attr, val)
        if attr in ['range_mapper']:
            super(AssignationMapper, self).__setattr__(attr, val)
            setattr(self, 'starting_date', self.range_mapper.starting_date)
            setattr(self, 'ending_date', self.range_mapper.ending_date)

    def __add__(self, other_assign):
        if AssignationOperator.can_be_joined(self, other_assign):
            starting_date = self.range_mapper.starting_date
            other_starting_date = other_assign.range_mapper.starting_date

            if starting_date > other_starting_date:
                start_day = other_assign.start_day
                self.start_day = start_day

            self.range_mapper += other_assign.range_mapper

        return self

    def __sub__(self, other_assign):
        pass

    def has_change(self):
        return (self.init_range != self.range_mapper or
                self.start_day != self.init_start_day)

    def get_difference(self):
        """
        This function return the difference of range
        between the init range and the current range
        """

        init_range = self.init_range
        range_mapper = self.range_mapper

        left_range = None
        if init_range.starting_date != range_mapper.starting_date:

            min_date = min(init_range.starting_date,
                           range_mapper.starting_date)

            max_date = max(init_range.starting_date,
                           range_mapper.starting_date - timedelta(days=1))

            left_range = Range(min_date, max_date)

        right_range = None
        if init_range.ending_date != range_mapper.ending_date:

            min_date = min(init_range.ending_date,
                           range_mapper.ending_date + timedelta(days=1))

            max_date = max(init_range.ending_date,
                           range_mapper.ending_date)

            right_range = Range(min_date, max_date)

        return left_range, right_range
