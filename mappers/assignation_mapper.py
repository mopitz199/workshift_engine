from mapper import Mapper
from operators.assignation_operator import AssignationOperator
from mappers.range_mapper import RangeMapper

class AssignationMapper(Mapper):

    def __init__(self, obj, attr_mapping):
        super(AssignationMapper, self).__init__(obj, attr_mapping)
        self.range_mapper = RangeMapper(self.starting_date, self.ending_date)

    def __len__(self):
        return len(self.range_mapper)

    def __repr__(self):
        return self.range_mapper

    def __add__(self, other_assign):
        if AssignationOperator.are_compatible(self, other_assign):
            self.starting_date = min(
                self.starting_date,
                other_assign.starting_date)

            self.ending_date = max(
                self.ending_date,
                other_assign.ending_date)

            self.eaten_assignments.append(other_assign)

    def __sub__(self, other_assign):
        pass
    
