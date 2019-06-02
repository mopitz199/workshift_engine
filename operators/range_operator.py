from datetime import datetime, timedelta


class RangeOperator:
    """A class with functions to handle and make operations with ranges"""

    @staticmethod
    def are_neighbors(r1, r2):
        """
            Function to check of two ranges intersect or are next to the other

            :param r1: a range of dates
            :type r1: Range
            :param r2: a range of dates
            :type r2: Range
            :rtype: True or False
        """

        return (r1.starting_date <= (r2.ending_date + timedelta(days=1)) and
                (r1.ending_date + timedelta(days=1)) >= r2.starting_date)

    @staticmethod
    def are_intersection(r1, r2):
        """
            Function to check of two ranges intersect

            :param r1: a range of dates
            :type r1: Range
            :param r2: a range of dates
            :type r2: Range
            :rtype: True or False
        """

        return (r1.starting_date <= r2.ending_date and
                r1.ending_date >= r2.starting_date)
