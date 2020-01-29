from datetime import datetime

from utils.range_datetime import RangeDateTime
from utils.range import Range
from utils.range_datetime_operator import RangeDateTimeOperator


class TestRangeDatetimeAreIntersection(object):

    def test_are_intersection1(self):
        r1 = RangeDateTime(
            datetime(2019, 5, 1),
            datetime(2019, 5, 4)
        )

        r2 = RangeDateTime(
            datetime(2019, 5, 3),
            datetime(2019, 5, 5)
        )

        assert RangeDateTimeOperator.are_intersection(r1, r2)

    def test_are_intersection2(self):
        r1 = RangeDateTime(
            datetime(2019, 5, 1, 10, 0, 0),
            datetime(2019, 5, 4, 10, 0, 0)
        )

        r2 = RangeDateTime(
            datetime(2019, 5, 4, 10, 0, 0),
            datetime(2019, 5, 5, 10, 0, 0)
        )

        assert RangeDateTimeOperator.are_intersection(r1, r2)

    def test_are_intersection3(self):
        r1 = RangeDateTime(
            datetime(2019, 5, 1, 10, 0, 0),
            datetime(2019, 5, 4, 10, 0, 0)
        )

        r2 = RangeDateTime(
            datetime(2019, 5, 4, 10, 0, 1),
            datetime(2019, 5, 5, 10, 0, 0)
        )

        assert not RangeDateTimeOperator.are_intersection(r1, r2)


class TestSplitBorders(object):

    def test_split_borders_1(self):

        range_datetime = RangeDateTime(
            datetime(2019, 5, 1, 10, 0, 0),
            datetime(2019, 5, 4, 10, 0, 0)
        )

        response = RangeDateTimeOperator.split_borders(range_datetime)

        expected = [
            RangeDateTime(
                datetime(2019, 5, 1, 10, 0, 0),
                datetime(2019, 5, 1, 23, 59, 0)
            ),
            Range(
                datetime(2019, 5, 2).date(),
                datetime(2019, 5, 3).date()
            ),
            RangeDateTime(
                datetime(2019, 5, 4, 0, 0, 0),
                datetime(2019, 5, 4, 10, 0, 0)
            ),
        ]
        assert response == expected

    def test_split_borders_2(self):

        range_datetime = RangeDateTime(
            datetime(2019, 5, 1, 10, 0, 0),
            datetime(2019, 5, 1, 10, 1, 0)
        )

        response = RangeDateTimeOperator.split_borders(range_datetime)

        expected = [
            RangeDateTime(
                datetime(2019, 5, 1, 10, 0, 0),
                datetime(2019, 5, 1, 10, 1, 0)
            ),
            None,
            None,
        ]
        assert response == expected

    def test_split_borders_3(self):

        range_datetime = RangeDateTime(
            datetime(2019, 5, 1, 10, 0, 0),
            datetime(2019, 5, 2, 10, 0, 0)
        )

        response = RangeDateTimeOperator.split_borders(range_datetime)

        expected = [
            RangeDateTime(
                datetime(2019, 5, 1, 10, 0, 0),
                datetime(2019, 5, 1, 23, 59, 0)
            ),
            None,
            RangeDateTime(
                datetime(2019, 5, 2, 0, 0, 0),
                datetime(2019, 5, 2, 10, 0, 0)
            ),
        ]
        assert response == expected

    def test_split_borders_4(self):

        range_datetime = RangeDateTime(
            datetime(2019, 5, 1, 10, 0, 0),
            datetime(2019, 5, 1, 10, 0, 0)
        )

        response = RangeDateTimeOperator.split_borders(range_datetime)

        expected = [
            RangeDateTime(
                datetime(2019, 5, 1, 10, 0, 0),
                datetime(2019, 5, 1, 10, 0, 0)
            ),
            None,
            None,
        ]
        assert response == expected
