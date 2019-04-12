from datetime import datetime, timedelta

class RangeOperator(object):

    @staticmethod
    def are_neighbors(r1, r2):
        return ((r1.starting_date - timedelta(days = 1)) <= r2.ending_date and
            (r1.ending_date + timedelta(days = 1)) >= r2.starting_date)