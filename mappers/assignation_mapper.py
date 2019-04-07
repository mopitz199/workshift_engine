from mapper import Mapper
from operators.assignation_operator import AssignationOperator
class AssignationMapper(Mapper):

    def __init__(self, obj, attr_mapping):
        super(AssignationMapper, self).__init__(obj, attr_mapping)
        self.eaten_assignments = []

    def __len__(self):
        return (self.ending_date - self.starting_date).days

    def __repr__(self):
        return "{} - {}".format(self.starting_date, self.ending_date)

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
    
