# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import Any, List, Dict, Tuple, Optional, TYPE_CHECKING
from datetime import datetime, timedelta, date as dateclass

from assignation.operators.range_operator import RangeOperator
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.custom_typings import CToWResolverType, CToWCollisionType
from collisions.utils import Util
from generic_facades.day_facade import DayFacade

if TYPE_CHECKING:
    from generic_facades.manually_assignation_facade import (
        ManualAssignationFacade
    )
    from generic_facades.weekly_assignation_facade import (
        WeeklyAssignationFacade
    )
    from utils.range import Range


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
        manually_range: Range,
        weekly_day: Any
    ) -> Optional[int]:
        prev_weekly_day = self.weekly_facade.get_prev_day(weekly_day)
        weekly_prev_range = self.weekly_facade.range_obj_from_weekly_day(
            prev_weekly_day,
            self.base_prev_date
        )
        if weekly_prev_range:
            if RangeOperator.are_intersection(
                weekly_prev_range,
                manually_range
            ):
                return prev_weekly_day.day_number
            else:
                return None
        else:
            return None

    def check_next_collision(
        self,
        manually_range: Range,
        weekly_day: Any
    ) -> Optional[int]:
        next_weekly_day = self.weekly_facade.get_prev_day(weekly_day)
        weekly_next_range = self.weekly_facade.range_obj_from_weekly_day(
            next_weekly_day,
            self.base_next_date
        )

        if weekly_next_range:
            if RangeOperator.are_intersection(
                weekly_next_range,
                manually_range
            ):
                return next_weekly_day.day_number
            else:
                return None
        else:
            return None

    def check_current_collision(
        self,
        manually_range: Range,
        weekly_day: Any
    ) -> Optional[int]:

        weekly_current_range = self.weekly_facade.range_obj_from_weekly_day(
            weekly_day,
            self.base_current_date
        )

        if weekly_current_range:
            if RangeOperator.are_intersection(
                weekly_current_range,
                manually_range
            ):
                return weekly_day.day_number
            else:
                return None
        else:
            return None

    def check_manually_day(
        self,
        manually_day: Any,
        weekly_day: Any
    ) -> Dict[str, List]:

        str_date = "{}".format(manually_day.date)
        collisions = {}  # type: Dict[str, List]
        collisions[str_date] = []

        manually_range = self.manually_facade.range_obj_from_day(
            manually_day,
            self.base_current_date
        )

        if manually_range:
            if True:
                day_number = self.check_prev_collision(
                    manually_range,
                    weekly_day
                )
                if day_number:
                    collisions[str_date].append(day_number)

            day_number = self.check_current_collision(
                manually_range,
                weekly_day
            )
            if day_number:
                collisions[str_date].append(day_number)

            if True:
                day_number = self.check_next_collision(
                    manually_range,
                    weekly_day
                )
                if day_number:
                    collisions[str_date].append(day_number)

        return collisions

    def resolve(
        self,
        detail=False
    ) -> Tuple[bool, Dict]:
        collisions = {}
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
                    collisions.update(manually_day_collisions)
                else:
                    return True, collisions

        has_collisions = False
        if collisions:
            has_collisions = True

        return has_collisions, collisions
