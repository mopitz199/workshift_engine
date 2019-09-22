from datetime import datetime

from utils.range import Range
from assignation.operators.range_operator import RangeOperator


class TestRangeEatRangeList(object):

    def test_eat_ranges1(self):
        main_range = Range(
            datetime(2019, 5, 1).date(),
            datetime(2019, 5, 4).date())

        r1 = Range(
            datetime(2019, 5, 3).date(),
            datetime(2019, 5, 5).date())

        r2 = Range(
            datetime(2019, 5, 8).date(),
            datetime(2019, 5, 10).date())

        range_list = [r1, r2]

        main_range, range_list = RangeOperator.eat_ranges(
            main_range,
            range_list)

        expect1 = Range(
            datetime(2019, 5, 1).date(),
            datetime(2019, 5, 5).date())

        expect2 = [
            Range(
                datetime(2019, 5, 8).date(),
                datetime(2019, 5, 10).date())
        ]

        assert main_range == expect1 and range_list == expect2

    def test_eat_ranges2(self):
        main_range = Range(
            datetime(2019, 5, 1).date(),
            datetime(2019, 5, 4).date())

        r1 = Range(
            datetime(2019, 5, 8).date(),
            datetime(2019, 5, 10).date())

        r2 = Range(
            datetime(2019, 5, 5).date(),
            datetime(2019, 5, 7).date())

        range_list = [r1, r2]

        main_range, range_list = RangeOperator.eat_ranges(
            main_range,
            range_list)

        expect1 = Range(
            datetime(2019, 5, 1).date(),
            datetime(2019, 5, 10).date())

        expect2 = []

        assert main_range == expect1 and range_list == expect2

    def test_eat_ranges3(self):
        main_range = Range(
            datetime(2019, 5, 1).date(),
            datetime(2019, 5, 4).date())

        r1 = Range(
            datetime(2019, 5, 8).date(),
            datetime(2019, 5, 10).date())

        r2 = Range(
            datetime(2019, 5, 6).date(),
            datetime(2019, 5, 12).date())

        range_list = [r1, r2]

        main_range, range_list = RangeOperator.eat_ranges(
            main_range,
            range_list)

        expect1 = Range(
            datetime(2019, 5, 1).date(),
            datetime(2019, 5, 4).date())

        expect2 = [r1, r2]

        assert main_range == expect1 and range_list == expect2

    def test_eat_ranges4(self):
        main_range = Range(
            datetime(2019, 5, 1).date(),
            datetime(2019, 5, 4).date())

        range_list = []

        main_range, range_list = RangeOperator.eat_ranges(
            main_range,
            range_list)

        expect1 = Range(
            datetime(2019, 5, 1).date(),
            datetime(2019, 5, 4).date())

        expect2 = []

        assert main_range == expect1 and range_list == expect2


class TestRangeCompressRangeList(object):

    def test_compress_range_list1(self):
        range_list = [
            Range(
                datetime(2019, 5, 1).date(),
                datetime(2019, 5, 4).date()),
            Range(
                datetime(2019, 5, 5).date(),
                datetime(2019, 5, 9).date()),
        ]

        response = RangeOperator.compress_range_list(range_list)

        expect2 = [
            Range(
                datetime(2019, 5, 1).date(),
                datetime(2019, 5, 9).date()),
        ]

        assert response == expect2

    def test_compress_range_list2(self):
        range_list = [
            Range(
                datetime(2019, 5, 1).date(),
                datetime(2019, 5, 4).date()),
            Range(
                datetime(2019, 5, 6).date(),
                datetime(2019, 5, 9).date()),
        ]

        response = RangeOperator.compress_range_list(range_list)

        assert response == range_list

    def test_compress_range_list3(self):
        range_list = [
            Range(
                datetime(2019, 5, 1).date(),
                datetime(2019, 5, 4).date()),
            Range(
                datetime(2019, 5, 2).date(),
                datetime(2019, 5, 4).date()),
            Range(
                datetime(2019, 5, 8).date(),
                datetime(2019, 5, 9).date()),
            Range(
                datetime(2019, 5, 10).date(),
                datetime(2019, 5, 11).date()),
        ]

        response = RangeOperator.compress_range_list(range_list)

        expect2 = [
            Range(
                datetime(2019, 5, 1).date(),
                datetime(2019, 5, 4).date()),
            Range(
                datetime(2019, 5, 8).date(),
                datetime(2019, 5, 11).date()),
        ]

        assert response == expect2

    def test_compress_range_list4(self):
        range_list = []

        response = RangeOperator.compress_range_list(range_list)

        assert response == []
