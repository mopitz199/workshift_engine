# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import List, Dict, Tuple, Optional, TYPE_CHECKING, Any
from datetime import datetime, timedelta, date as dateclass

from collisions.constants import (
    PREVIOUS,
    CURRENT,
    NEXT
)
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.custom_typings import CToWResolverType, CToWCollisionType
from collisions.iterators import CycleDateIterator
from collisions.utils import Util
from generic_facades.day_facade import DayFacade

from utils.range_datetime import RangeDateTime
from utils.range_datetime_operator import RangeDateTimeOperator

if TYPE_CHECKING:
    from generic_facades.cycle_assignation_facade import CycleAssignationFacade
    from generic_facades.weekly_assignation_facade import (
        WeeklyAssignationFacade
    )
    from utils.range import Range


class CycleToCycleColission(object):

    def __init__(
        self,
        cycle_facade_1: CycleAssignationFacade,
        cycle_facade_2: CycleAssignationFacade,
    ) -> None:
        self.base_prev_date = BASE_PREV_DATE
        self.base_current_date = BASE_CURRENT_DATE
        self.base_next_date = BASE_NEXT_DATE
        self.cycle_facade_1 = cycle_facade_1
        self.cycle_facade_2 = cycle_facade_2

    def day_to_range_datetime(self, day, collision_type):
        if collision_type == PREVIOUS:
            day_starting_datetime = datetime.combine(
                self.base_prev_date,
                day.starting_time
            )
        elif collision_type == CURRENT:
            day_starting_datetime = datetime.combine(
                self.base_current_date,
                day.starting_time
            )
        elif collision_type == NEXT:
            day_starting_datetime = datetime.combine(
                self.base_next_date,
                day.starting_time
            )
        else:
            raise Exception(f'Collision type not allowed: {collision_type}')

        ending_date = day_starting_datetime.date()
        if day.starting_time > day.ending_time:
            ending_date = ending_date + timedelta(days=1)

        day_ending_datetime = datetime.combine(
            ending_date,
            day.ending_time
        )

        return RangeDateTime(
            day_starting_datetime,
            day_ending_datetime
        )

    def check_prev_collision(
        self,
        main_day: Any,
        prev_day: Any
    ) -> Optional[RangeDateTime]:
        main_range = self.day_to_range_datetime(main_day, CURRENT)
        prev_range = self.day_to_range_datetime(prev_day, PREVIOUS)
        intersection = RangeDateTimeOperator.get_intersection(
            main_range,
            prev_range
        )
        if intersection:
            return intersection
        else:
            return None

    def check_current_collision(
        self,
        main_day: Any,
        current_day: Any
    ) -> Optional[RangeDateTime]:
        main_range = self.day_to_range_datetime(main_day, CURRENT)
        current_range = self.day_to_range_datetime(current_day, CURRENT)
        intersection = RangeDateTimeOperator.get_intersection(
            main_range,
            current_range
        )
        if intersection:
            return intersection
        else:
            return None

    def check_next_collision(
        self,
        main_day: Any,
        next_day: Any
    ) -> Optional[RangeDateTime]:
        main_range = self.day_to_range_datetime(main_day, CURRENT)
        next_range = self.day_to_range_datetime(next_day, NEXT)
        intersection = RangeDateTimeOperator.get_intersection(
            main_range,
            next_range
        )
        if intersection:
            return intersection
        else:
            return None

    def get_all_day_numbers(
        self,
        date_obj: dateclass
    ) -> Optional[Dict]:
        day_number = self.cycle_facade_2.simulate_starting_day(date_obj)
        if day_number:
            day_number -= 1
            prev_day_number = self.cycle_facade_2.get_prev_day_number(
                day_number
            )
            next_day_number = self.cycle_facade_2.get_next_day_number(
                day_number
            )
            return {
                'prev_day_number': prev_day_number,
                'current_day_number': day_number,
                'next_day_number': next_day_number
            }
        else:
            return None

    def filter_all_day_numbers(
        self,
        date_obj: dateclass,
        all_day_numbers: Optional[Dict]
    ) -> Optional[Dict]:
        if not all_day_numbers:
            return None

        prev_date = date_obj - timedelta(days=1)
        current_date = date_obj
        next_date = date_obj + timedelta(days=1)
        assignation_2 = self.cycle_facade_2.assignation
        starting_date = assignation_2.starting_date
        ending_date = assignation_2.ending_date
        if not (starting_date <= prev_date <= ending_date):
            del all_day_numbers['prev_day_number']
        if not (starting_date <= current_date <= ending_date):
            del all_day_numbers['current_day_number']
        if not (starting_date <= next_date <= ending_date):
            del all_day_numbers['next_day_number']

        if all_day_numbers:
            return all_day_numbers
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

    def check_collisions(
        self,
        day: Any,
        all_day_numbers: Dict
    ) -> Optional[Dict]:
        collisions = {}

        prev_day_number = all_day_numbers.get('prev_day_number', None)
        current_day_number = all_day_numbers.get('current_day_number', None)
        next_day_number = all_day_numbers.get('next_day_number', None)
        if prev_day_number is not None:
            prev_day = self.cycle_facade_2.get_day_obj_from_day_number(
                prev_day_number
            )
            intersection = self.check_prev_collision(day, prev_day)
            if intersection:
                collisions['prev'] = {
                    'day_number': prev_day_number,
                    'intersection': intersection
                }

        if current_day_number is not None:
            current_day = self.cycle_facade_2.get_day_obj_from_day_number(
                current_day_number
            )
            intersection = self.check_current_collision(day, current_day)
            if intersection:
                collisions['current'] = {
                    'day_number': current_day_number,
                    'intersection': intersection
                }

        if next_day_number is not None:
            next_day = self.cycle_facade_2.get_day_obj_from_day_number(
                next_day_number
            )
            intersection = self.check_next_collision(day, next_day)
            if intersection:
                collisions['next'] = {
                    'day_number': next_day_number,
                    'intersection': intersection
                }
        if collisions:
            return collisions
        else:
            return None

    def filter_by_days_off(
        self,
        date_obj: dateclass,
        collisions: Optional[Dict]
    ) -> Optional[Dict]:
        if not collisions:
            return None

        prev_collision = collisions.get('prev', None)
        if prev_collision:
            prev_real_intersection = self.get_real_intersection(
                date_obj,
                prev_collision.pop('intersection')
            )
            covered = self.cycle_facade_2.covered(prev_real_intersection)
            if covered:
                del collisions['prev']

        current_collision = collisions.get('current', None)
        if current_collision:
            current_real_intersection = self.get_real_intersection(
                date_obj,
                current_collision.pop('intersection')
            )
            covered = self.cycle_facade_2.covered(current_real_intersection)
            if covered:
                del collisions['current']

        next_collision = collisions.get('next', None)
        if next_collision:
            next_real_intersection = self.get_real_intersection(
                date_obj + timedelta(days=1),
                next_collision.pop('intersection')
            )
            covered = self.cycle_facade_2.covered(next_real_intersection)
            if covered:
                del collisions['next']

        if collisions:
            return collisions
        else:
            return None

    def resolve(self) -> Optional[Dict]:
        all_collisions: Dict = {}
        for day in self.cycle_facade_1.get_days():
            day_facade = DayFacade(day)
            if day_facade.is_working_day():
                interator = CycleDateIterator(
                    assignation=self.cycle_facade_1.assignation,
                    day_number=day.day_number
                )
                for date_obj in interator:
                    all_day_numbers = self.get_all_day_numbers(date_obj)
                    all_day_numbers = self.filter_all_day_numbers(
                        date_obj,
                        all_day_numbers
                    )
                    if all_day_numbers:
                        collisions = self.check_collisions(
                            day,
                            all_day_numbers
                        )
                        collisions = self.filter_by_days_off(
                            date_obj,
                            collisions
                        )

                        if collisions:
                            key = f"{day.day_number}"
                            if key not in all_collisions:
                                all_collisions[key] = {}

                            date_str = f"{date_obj}"
                            all_collisions[key][date_str] = collisions
        return all_collisions
