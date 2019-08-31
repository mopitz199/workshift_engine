from datetime import datetime

from utils.range import Range


class TestRangeSub(object):
    """To test if the __sub__ function work properly"""

    def test_sub1(self):
        r1 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 10).date())

        r2 = Range(
            datetime(2019, 5, 10).date(),
            datetime(2019, 5, 17).date())

        r2, new = r2 - r1

        assert (r2.starting_date == datetime(2019, 5, 11).date() and
                r2.ending_date == datetime(2019, 5, 17).date() and new is None)

    def test_sub2(self):
        r1 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 17).date())

        r2 = Range(
            datetime(2019, 5, 10).date(),
            datetime(2019, 5, 13).date())

        r1, new = r1 - r2

        assert (r1.starting_date == datetime(2019, 5, 5).date() and
                r1.ending_date == datetime(2019, 5, 9).date() and
                new.starting_date == datetime(2019, 5, 14).date() and
                new.ending_date == datetime(2019, 5, 17).date())

    def test_sub3(self):
        r1 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 17).date())

        r2 = Range(
            datetime(2019, 5, 10).date(),
            datetime(2019, 5, 13).date())

        r1, new = r2 - r1

        assert r1 is None and new is None

    def test_sub4(self):
        r1 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 17).date())

        r2 = Range(
            datetime(2019, 5, 6).date(),
            datetime(2019, 5, 8).date())

        r1, new = r1 - r2

        assert (r1.starting_date == datetime(2019, 5, 9).date() and
                r1.ending_date == datetime(2019, 5, 17).date() and
                new.starting_date == datetime(2019, 5, 5).date() and
                new.ending_date == datetime(2019, 5, 5).date())


class TestRangeAdd(object):
    """To test if the __add__ function work properly"""

    def test_add1(self):
        r1 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 10).date())

        r2 = Range(
            datetime(2019, 5, 10).date(),
            datetime(2019, 5, 17).date())

        r2 = r2 + r1

        assert (r2.starting_date == datetime(2019, 5, 5).date() and
                r2.ending_date == datetime(2019, 5, 17).date())

    def test_add2(self):
        r1 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 10).date())

        r2 = Range(
            datetime(2019, 5, 11).date(),
            datetime(2019, 5, 17).date())

        r2 = r2 + r1

        assert (r2.starting_date == datetime(2019, 5, 5).date() and
                r2.ending_date == datetime(2019, 5, 17).date())

    def test_add3(self):
        r1 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 10).date())

        r2 = Range(
            datetime(2019, 5, 12).date(),
            datetime(2019, 5, 17).date())

        r1 = r1 + r2

        assert (r1.starting_date == datetime(2019, 5, 5).date() and
                r1.ending_date == datetime(2019, 5, 10).date())

    def test_add4(self):
        r1 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 10).date())

        r2 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 10).date())

        r1 = r1 + r2

        assert (r1.starting_date == datetime(2019, 5, 5).date() and
                r1.ending_date == datetime(2019, 5, 10).date())
