# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import (
    Any,
    Dict,
    List,
    Tuple,
    TYPE_CHECKING,
    Optional
)

from datetime import datetime, timedelta, date as dateclass

from utils.range_datetime_operator import RangeDateTimeOperator
from collisions.constants import (
    PREVIOUS,
    CURRENT,
    NEXT
)
from collisions.custom_typings import CToMCollisionType, CToMResolverType
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.utils import Util
from utils.range_datetime import RangeDateTime

if TYPE_CHECKING:
    from generic_facades.cycle_assignation_facade import CycleAssignationFacade
    from generic_facades.day_facade import DayFacade
    from generic_facades.manually_assignation_facade import (
        ManualAssignationFacade
    )


class CycleToManuallyCollision():

    def __init__(
        self,
        cycle_facade: CycleAssignationFacade,
        manually_facade: ManualAssignationFacade,
    ):
        self.base_prev_date = BASE_PREV_DATE
        self.base_current_date = BASE_CURRENT_DATE
        self.base_next_date = BASE_NEXT_DATE
        self.cycle_facade = cycle_facade
        self.manually_facade = manually_facade

    def can_check_collision(
        self,
        manually_day: Any,
        check_type: str
    ) -> bool:
        manually_date = manually_day.date
        aux_starting_date = self.cycle_facade.assignation.starting_date
        aux_ending_date = self.cycle_facade.assignation.ending_date

        if check_type == PREVIOUS:
            aux_starting_date = aux_starting_date + timedelta(days=1)
            aux_ending_date = aux_ending_date + timedelta(days=1)
        elif check_type == NEXT:
            aux_starting_date = aux_starting_date - timedelta(days=1)
            aux_ending_date = aux_ending_date - timedelta(days=1)
        elif check_type == CURRENT:
            pass
        else:
            raise Exception('Unknown check type')

        return aux_starting_date <= manually_date <= aux_ending_date

    def ensure_empty_list(
        self,
        collisions: Dict,
        key: str
    ) -> None:
        if key not in collisions:
            collisions[key] = []

    def try_check_prev_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> Optional[Dict]:
        collisions: Dict = {}
        if self.can_check_collision(manually_day, PREVIOUS):
            date = manually_day.date
            str_date = str(date)

            intersection = self.check_prev_collision(
                manually_day,
                cycle_day
            )
            if intersection:
                self.ensure_empty_list(collisions, str_date)
                prev_day_number = self.cycle_facade.get_prev_day_number(
                    cycle_day.day_number
                )
                real_intersection = self.get_real_intersection(
                    date,
                    intersection
                )
                covered = self.cycle_facade.covered(real_intersection)
                if not covered:
                    collisions[str_date].append(prev_day_number)
                return collisions
        return None

    def try_check_current_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> Optional[Dict]:
        collisions: Dict = {}
        if self.can_check_collision(manually_day, CURRENT):
            date = manually_day.date
            str_date = str(date)
            day_number = cycle_day.day_number

            intersection = self.check_current_collision(
                manually_day,
                cycle_day
            )
            if intersection:
                self.ensure_empty_list(collisions, str_date)
                real_intersection = self.get_real_intersection(
                    date,
                    intersection
                )
                covered = self.cycle_facade.covered(real_intersection)
                if not covered:
                    collisions[str_date].append(day_number)

                return collisions
        return None

    def try_check_next_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> Optional[Dict]:
        collisions: Dict = {}
        if self.can_check_collision(manually_day, NEXT):
            date = manually_day.date
            str_date = str(date)
            day_number = cycle_day.day_number

            intersection = self.check_next_collision(
                manually_day,
                cycle_day
            )

            if intersection:
                self.ensure_empty_list(collisions, str_date)
                next_day_number = self.cycle_facade.get_next_day_number(
                    day_number
                )
                real_intersection = self.get_real_intersection(
                    date + timedelta(days=1),
                    intersection
                )
                covered = self.cycle_facade.covered(real_intersection)
                if not covered:
                    collisions[str_date].append(next_day_number)
                    return collisions

        return None

    def check_prev_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> Optional[RangeDateTime]:
        day_number = cycle_day.day_number
        prev_day_number = self.cycle_facade.get_prev_day_number(day_number)
        prev_cycle_day = self.cycle_facade.get_day_data(prev_day_number)
        prev_range = self.cycle_facade.range_datetime_obj_from_day_number(
            prev_cycle_day,
            self.base_prev_date)

        manually_range = self.manually_facade.range_datetime_obj_from_day(
            manually_day,
            self.base_current_date)

        if prev_range and manually_range:
            intersection = RangeDateTimeOperator.get_intersection(
                prev_range,
                manually_range
            )
            if intersection:
                return intersection
            else:
                return None
        else:
            return None

    def check_current_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> Optional[RangeDateTime]:
        current_range = self.cycle_facade.range_datetime_obj_from_day_number(
            cycle_day,
            self.base_current_date)

        manually_range = self.manually_facade.range_datetime_obj_from_day(
            manually_day,
            self.base_current_date)

        if current_range and manually_range:
            intersection = RangeDateTimeOperator.get_intersection(
                current_range,
                manually_range
            )
            if intersection:
                return intersection
            else:
                return None
        else:
            return None

    def check_next_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> Optional[RangeDateTime]:
        day_number = cycle_day.day_number
        next_day_number = self.cycle_facade.get_next_day_number(day_number)
        next_cycle_day = self.cycle_facade.get_day_data(next_day_number)
        next_range = self.cycle_facade.range_datetime_obj_from_day_number(
            next_cycle_day,
            self.base_next_date)

        manually_range = self.manually_facade.range_datetime_obj_from_day(
            manually_day,
            self.base_current_date)

        if next_range and manually_range:
            intersection = RangeDateTimeOperator.get_intersection(
                next_range,
                manually_range
            )
            if intersection:
                return intersection
            else:
                return None
        else:
            return None

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

    def get_collision_detail(
        self,
        manually_day: Any
    ) -> Optional[Dict]:
        collisions: Dict = {}
        date = manually_day.date
        str_date = str(date)
        day_number = self.cycle_facade.simulate_starting_day(date)

        if day_number is not None:
            day_number -= 1
            cycle_day = self.cycle_facade.get_day_data(day_number)

            prev_collisions = self.try_check_prev_collision(
                manually_day,
                cycle_day
            )

            current_collisions = (
                self.try_check_current_collision(
                    manually_day,
                    cycle_day
                )
            )

            next_collisions = self.try_check_next_collision(
                manually_day,
                cycle_day
            )

            has_collision = (
                prev_collisions or
                current_collisions or
                next_collisions
            )

            if has_collision:
                collisions[str_date] = []
                if prev_collisions:
                    collisions[str_date] += prev_collisions.get(str_date, [])
                if current_collisions:
                    collisions[str_date] += current_collisions.get(str_date, [])
                if next_collisions:
                    collisions[str_date] += next_collisions.get(str_date, [])

            if collisions:
                return collisions
            else:
                return None
        else:
            raise Exception('Simulation response None')

    def resolve(self) -> Optional[Dict]:
        collisions: Dict = {}
        manually_days = self.manually_facade.get_days()
        for manually_day in manually_days:
            aux_collisions = self.get_collision_detail(
                manually_day
            )
            if aux_collisions:
                collisions.update(aux_collisions)

        if collisions:
            return collisions
        else:
            return None
