# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Tuple,
    List
)

import copy
from datetime import datetime, timedelta

if TYPE_CHECKING:
    from utils.range import Range


class RangeOperator:
    """ A class with functions to handle and make operations with ranges """

    @staticmethod
    def are_neighbors(
        r1: Range,
        r2: Range
    ) -> bool:
        """ Check if two ranges intersect or are next to the other """

        return (r1.starting_date <= (r2.ending_date + timedelta(days=1)) and
                (r1.ending_date + timedelta(days=1)) >= r2.starting_date)

    @staticmethod
    def are_intersection(
        r1: Range,
        r2: Range
    ) -> bool:
        """ Check if two ranges intersect """

        return (r1.starting_date <= r2.ending_date and
                r1.ending_date >= r2.starting_date)

    @staticmethod
    def get_intersection(
        r1: Range,
        r2: Range
    ) -> Range:
        if RangeOperator.are_intersection(r1, r1):
            copy_range = copy.copy(r1)
            copy_range.starting_date = max(r1.starting_date, r2.starting_date)
            copy_range.ending_date = min(r1.ending_date, r2.ending_date)
            return copy_range
        else:
            return r1

    @staticmethod
    def eat_ranges(
        main_range: Range,
        list_ranges: List[Range]
    ) -> Tuple[Range, List[Range]]:
        list_main_range_before = list_ranges
        list_main_range_after = None
        while(list_main_range_before != list_main_range_after):
            if list_main_range_after is not None:
                list_main_range_before = copy.deepcopy(list_main_range_after)

            list_main_range_after = []
            for r in list_main_range_before:
                if RangeOperator.are_neighbors(main_range, r):
                    main_range += r
                else:
                    list_main_range_after.append(r)

        return main_range, list_main_range_after

    @staticmethod
    def compress_range_list(
        range_list: List[Range]
    ) -> List[Range]:
        range_list = copy.deepcopy(range_list)
        response = []
        while range_list:
            main_range = range_list[0]
            range_list.remove(main_range)

            main_range, range_list = RangeOperator.eat_ranges(
                main_range,
                range_list)

            response.append(main_range)

        return response
