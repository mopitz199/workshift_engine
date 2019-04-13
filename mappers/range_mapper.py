import copy
from datetime import datetime, timedelta
from operators.range_operator import RangeOperator


class RangeMapper(object):
    """Class that represent a range"""

    def __init__(self, *args):
        self.starting_date = args[0]
        self.ending_date = args[1]
        super(RangeMapper, self).__init__()

    def __sub__(self, other_range):
        left = (other_range.starting_date - self.starting_date).days
        right = (self.ending_date - other_range.ending_date).days

        if left > 0 and right > 0:
            new = copy.deepcopy(self)
            new.starting_date = other_range.ending_date + timedelta(days = 1)
            new.ending_date = self.ending_date

            self.ending_date = other_range.starting_date - timedelta(days = 1)

            return self, new
        elif left > 0:
            self.ending_date = other_range.starting_date - timedelta(days = 1)
            return self, None
        elif right > 0:
            self.starting_date = other_range.ending_date + timedelta(days = 1)
            return self, None
        else:
            return None, None

    def __add__(self, other_range):
        if RangeOperator.are_neighbors(self, other_range):
            self.starting_date = min(self.starting_date, other_range.starting_date)
            self.ending_date = max(self.ending_date, other_range.ending_date)
        return self

    def __repr__(self):
        return "{} {}".format(self.starting_date, self.ending_date)

    def __str__(self):
        return "{} {}".format(self.starting_date, self.ending_date)

    def __len__(self):
        return (self.ending_date - self.starting_date).days