import copy
from datetime import datetime, timedelta
from assignation.operators.range_operator import RangeOperator


class RangeDateTime(object):
    """Class that represent a range"""

    def __init__(self, *args):
        self.starting_datetime = args[0]
        self.ending_datetime = args[1]

    def __eq__(self, other):
        return (self.starting_datetime == other.starting_datetime and
                self.ending_datetime == other.ending_datetime)

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

    def __repr__(self):
        return "{} {}".format(self.starting_datetime, self.ending_datetime)

    def __str__(self):
        return "{} {}".format(self.starting_datetime, self.ending_datetime)
