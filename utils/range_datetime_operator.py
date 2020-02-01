# make all type hints be strings and skip evaluating them
from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING, List, Union, Optional

from utils.date_util import DateUtil
from utils.range import Range
from utils.range_datetime import RangeDateTime


class RangeDateTimeOperator:
    """ A class with functions to handle and make operations with ranges """

    @staticmethod
    def are_intersection(
        r1: RangeDateTime,
        r2: RangeDateTime
    ) -> bool:
        """ Check if two ranges intersect """

        return (r1.starting_datetime <= r2.ending_datetime and
                r1.ending_datetime >= r2.starting_datetime)

    @staticmethod
    def get_intersection(
        r1: RangeDateTime,
        r2: RangeDateTime
    ) -> Optional[RangeDateTime]:
        if RangeDateTimeOperator.are_intersection(r1, r2):
            return RangeDateTime(
                max(r1.starting_datetime, r2.starting_datetime),
                min(r1.ending_datetime, r2.ending_datetime)
            )
        return None

    @staticmethod
    def is_in(
        r1: RangeDateTime,
        r2: RangeDateTime
    ) -> bool:
        return (
            r1.starting_datetime >= r2.starting_datetime and
            r1.ending_datetime <= r2.ending_datetime
        )

    @staticmethod
    def split_borders(
        range_obj: RangeDateTime
    ) -> List[Union[RangeDateTime, Range, None]]:

        starting_datetime = range_obj.starting_datetime
        ending_datetime = range_obj.ending_datetime

        delta = ending_datetime.date() - starting_datetime.date()

        if delta.days == 0:
            return [range_obj, None, None]

        time_obj = DateUtil.str_to_time('23:59')
        aux_ending_datetime = datetime.combine(
            starting_datetime.date(),
            time_obj
        )
        left_range_datetime = RangeDateTime(
            starting_datetime,
            aux_ending_datetime
        )

        time_obj = DateUtil.str_to_time('00:00')
        aux_starting_datetime = datetime.combine(
            ending_datetime.date(),
            time_obj
        )
        right_range_datetime = RangeDateTime(
            aux_starting_datetime,
            ending_datetime
        )

        body = None
        if delta.days > 1:
            body = Range(
                starting_datetime.date() + timedelta(days=1),
                ending_datetime.date() - timedelta(days=1)
            )

        return [
            left_range_datetime,
            body,
            right_range_datetime
        ]
