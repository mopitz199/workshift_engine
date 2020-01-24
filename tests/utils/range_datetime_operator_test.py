from datetime import datetime

from utils.range_datetime import RangeDateTime
from utils.range_datetime_operator import RangeDateTimeOperator


class TestRangeDatetimeAreIntersection(object):

    def test_are_intersection1(self):
        r1 = RangeDateTime(
            datetime(2019, 5, 1),
            datetime(2019, 5, 4))

        r2 = RangeDateTime(
            datetime(2019, 5, 3),
            datetime(2019, 5, 5))

        assert RangeDateTimeOperator.are_intersection(r1, r2)

    def test_are_intersection2(self):
        r1 = RangeDateTime(
            datetime(2019, 5, 1, 10, 0, 0),
            datetime(2019, 5, 4, 10, 0, 0))

        r2 = RangeDateTime(
            datetime(2019, 5, 4, 10, 0, 0),
            datetime(2019, 5, 5, 10, 0, 0))

        assert RangeDateTimeOperator.are_intersection(r1, r2)

    def test_are_intersection3(self):
        r1 = RangeDateTime(
            datetime(2019, 5, 1, 10, 0, 0),
            datetime(2019, 5, 4, 10, 0, 0))

        r2 = RangeDateTime(
            datetime(2019, 5, 4, 10, 0, 1),
            datetime(2019, 5, 5, 10, 0, 0))

        assert not RangeDateTimeOperator.are_intersection(r1, r2)
