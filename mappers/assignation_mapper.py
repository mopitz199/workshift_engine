from mapper import Mapper
from operators.assignation_operator import AssignationOperator
from mappers.range_mapper import RangeMapper

class AssignationMapper(Mapper):

    def __init__(self, obj, attr_mapping):
        super(AssignationMapper, self).__init__(obj, attr_mapping)
        self.range_mapper = RangeMapper(self.starting_date, self.ending_date)
        self.workshift_obj = None

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
        if AssignationOperator.are_compatible(self, other_assign):
            self.range_mapper += other_assign.range_mapper
        return self

    def __sub__(self, other_assign):
        pass

    @property
    def workshift(self):
        """
        .. function:: workshift(self)

            To get the workshift associated with the assignation

            :rtype: <WorkshiftMapper>
        """
        if not self.workshift_obj:
            # Search for the workshift object in db
            pass
        return self.workshift_obj
    
