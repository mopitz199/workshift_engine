# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
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
