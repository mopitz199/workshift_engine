# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import Any, List, Dict, Tuple, Optional, TYPE_CHECKING
from datetime import datetime, timedelta, date as dateclass

from utils.range_datetime_operator import RangeDateTimeOperator
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.custom_typings import WToMCollisionType, WToMResolverType
from collisions.utils import Util
from generic_facades.day_facade import DayFacade
from utils.range_datetime import RangeDateTime

if TYPE_CHECKING:
    from generic_facades.manually_assignation_facade import (
        ManualAssignationFacade
    )
    from generic_facades.weekly_assignation_facade import (
        WeeklyAssignationFacade
    )


class WeeklyAndManuallyCollision():

    def __init__(
        self,
        weekly_facade: WeeklyAssignationFacade,
        manually_facade: ManualAssignationFacade,
    ) -> None:
        self.base_prev_date = BASE_PREV_DATE
        self.base_current_date = BASE_CURRENT_DATE
        self.base_next_date = BASE_NEXT_DATE
        self.manually_facade = manually_facade
        self.weekly_facade = weekly_facade

    def check_prev_collision(
        self,
        manually_range: RangeDateTime,
        weekly_day: Any
    ) -> Tuple[Optional[int], Optional[RangeDateTime]]:
        prev_weekly_day = self.weekly_facade.get_prev_day(weekly_day)
        weekly_prev_range = self.weekly_facade.range_datetime_from_weekly_day(
            prev_weekly_day,
            self.base_prev_date
        )
        if weekly_prev_range:
            intersection = RangeDateTimeOperator.get_intersection(
                weekly_prev_range,
                manually_range
            )
            if intersection:
                return (prev_weekly_day.day_number, intersection)
            else:
                return (None, None)
        else:
            return (None, None)

    def check_next_collision(
        self,
        manually_range: RangeDateTime,
        weekly_day: Any
    ) -> Tuple[Optional[int], Optional[RangeDateTime]]:
        next_weekly_day = self.weekly_facade.get_next_day(weekly_day)
        weekly_next_range = self.weekly_facade.range_datetime_from_weekly_day(
            next_weekly_day,
            self.base_next_date
        )

        if weekly_next_range:
            intersection = RangeDateTimeOperator.get_intersection(
                weekly_next_range,
                manually_range
            )
            if intersection:
                return (next_weekly_day.day_number, intersection)
            else:
                return (None, None)
        else:
            return (None, None)

    def check_current_collision(
        self,
        manually_range: RangeDateTime,
        weekly_day: Any
    ) -> Tuple[Optional[int], Optional[RangeDateTime]]:
        weekly_current_range = self.weekly_facade\
            .range_datetime_from_weekly_day(
                weekly_day,
                self.base_current_date
            )

        if weekly_current_range:
            intersection = RangeDateTimeOperator.get_intersection(
                weekly_current_range,
                manually_range
            )
            if intersection:
                return weekly_day.day_number, intersection
            else:
                return None, None
        else:
            return None, None

    def get_real_intersection(
        self,
        date_obj: dateclass,
        aux_intersection: RangeDateTime
    ):
        starting_datetime = datetime.combine(
            date_obj,
            aux_intersection.starting_datetime.time()
        )

        ending_datetime = datetime.combine(
            date_obj,
            aux_intersection.ending_datetime.time()
        )

        return RangeDateTime(starting_datetime, ending_datetime)

    def check_manually_day(
        self,
        manually_day: Any,
        weekly_day: Any
    ) -> Dict[str, List]:

        str_date = "{}".format(manually_day.date)
        collisions = {}  # type: Dict[str, List]
        collisions[str_date] = []

        manually_range = self.manually_facade.range_datetime_obj_from_day(
            manually_day,
            self.base_current_date
        )

        if manually_range:
            weekly_starting_date = self.weekly_facade.assignation.starting_date
            weekly_ending_date = self.weekly_facade.assignation.ending_date

            if manually_day.date > weekly_starting_date:
                day_number, intersection = self.check_prev_collision(
                    manually_range,
                    weekly_day
                )
                if day_number is not None and intersection:
                    real_intersection = self.get_real_intersection(
                        manually_day.date,
                        intersection
                    )
                    covered = self.weekly_facade.covered(real_intersection)
                    if not covered:
                        collisions[str_date].append(day_number)

            if weekly_ending_date >= manually_day.date >= weekly_starting_date:
                day_number, intersection = self.check_current_collision(
                    manually_range,
                    weekly_day
                )
                if day_number is not None and intersection:
                    real_intersection = self.get_real_intersection(
                        manually_day.date,
                        intersection
                    )
                    covered = self.weekly_facade.covered(real_intersection)
                    if not covered:
                        collisions[str_date].append(day_number)

            if manually_day.date < weekly_ending_date:
                day_number, intersection = self.check_next_collision(
                    manually_range,
                    weekly_day
                )
                if day_number is not None and intersection:
                    real_intersection = self.get_real_intersection(
                        manually_day.date,
                        intersection
                    )
                    covered = self.weekly_facade.covered(real_intersection)
                    if not covered:
                        collisions[str_date].append(day_number)

        if collisions[str_date]:
            return collisions
        else:
            return {}

    def resolve(
        self,
        detail=False
    ) -> WToMResolverType:
        collisions = WToMCollisionType({})
        manually_days = self.manually_facade.get_days()
        for manually_day in manually_days:
            week_day = manually_day.date.weekday()
            str_week_day = str(week_day)
            weekly_day = self.weekly_facade.get_day(str_week_day)

            manually_day_collisions = self.check_manually_day(
                manually_day,
                weekly_day
            )

            if manually_day_collisions:
                if detail:
                    collisions.update(
                        WToMCollisionType(manually_day_collisions)
                    )
                else:
                    return WToMResolverType(
                        (True, collisions)
                    )

        has_collisions = False
        if collisions:
            has_collisions = True

        return WToMResolverType((has_collisions, collisions))
