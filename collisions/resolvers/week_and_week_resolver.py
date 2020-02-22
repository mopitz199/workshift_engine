# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import Any, List, Dict, Tuple, Optional, TYPE_CHECKING
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

from utils.range_operator import RangeOperator
from utils.range_datetime import RangeDateTime
from utils.range_datetime_operator import RangeDateTimeOperator

if TYPE_CHECKING:
    from generic_facades.weekly_assignation_facade import (
        WeeklyAssignationFacade
    )


class WeeklyAndWeeklyCollision():

    def __init__(
        self,
        weekly_facade_1: WeeklyAssignationFacade,
        weekly_facade_2: WeeklyAssignationFacade,
    ) -> None:
        self.base_prev_date = BASE_PREV_DATE
        self.base_current_date = BASE_CURRENT_DATE
        self.base_next_date = BASE_NEXT_DATE
        self.weekly_facade_1 = weekly_facade_1
        self.weekly_facade_2 = weekly_facade_2

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

    def check_prev_collision(self, main_day, prev_day):
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

    def check_current_collision(self, main_day, current_day):
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

    def check_next_collision(self, main_day, next_day):
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

    def get_base_collisions(self):
        base_collisions = {}
        days = self.weekly_facade_1.assignation.workshift_proxy.get_days()
        for main_day in days:
            current_day = self.weekly_facade_2.get_day(main_day.day_number)
            prev_day = self.weekly_facade_2.get_prev_day(current_day)
            next_day = self.weekly_facade_2.get_next_day(current_day)

            base_collisions[main_day.day_number] = {}

            intersection = self.check_prev_collision(main_day, prev_day)
            if intersection:
                base_collisions[main_day.day_number]['prev'] = {
                    'day_number': prev_day.day_number,
                    'intersection': intersection
                }

            intersection = self.check_current_collision(main_day, current_day)
            if intersection:
                base_collisions[main_day.day_number]['current'] = {
                    'day_number': current_day.day_number,
                    'intersection': intersection
                }

            intersection = self.check_next_collision(main_day, next_day)
            if intersection:
                base_collisions[main_day.day_number]['next'] = {
                    'day_number': next_day.day_number,
                    'intersection': intersection
                }
        return base_collisions

    def get_day_collisions(self, main_day, base_collisions):
        collisions = base_collisions[main_day.day_number]
        return collisions

    def filter_range_collisions(self, date_obj, collisions):
        prev_date = date_obj - timedelta(days=1)
        current_date = date_obj
        next_date = date_obj + timedelta(days=1)
        assignation_2 = self.weekly_facade_2.assignation
        starting_date = assignation_2.starting_date
        ending_date = assignation_2.ending_date
        if not starting_date <= prev_date <= ending_date:
            del collisions['prev']
        if not starting_date <= current_date <= ending_date:
            del collisions['current']
        if not starting_date <= next_date <= ending_date:
            del collisions['next']
        return collisions

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

    def filter_by_days_off(self, date_obj, collisions):
        if not collisions:
            return None

        prev_collision = collisions.get('prev', None)
        if prev_collision:
            prev_real_intersection = self.get_real_intersection(
                date_obj,
                prev_collision['intersection']
            )
            covered = self.weekly_facade_1.covered(prev_real_intersection)
            if covered:
                del collisions['prev']

        current_collision = collisions.get('current', None)
        if current_collision:
            current_real_intersection = self.get_real_intersection(
                date_obj,
                current_collision['intersection']
            )
            covered = self.weekly_facade_1.covered(current_real_intersection)
            if covered:
                del collisions['current']

        next_collision = collisions.get('next', None)
        if next_collision:
            next_real_intersection = self.get_real_intersection(
                date_obj + timedelta(days=1),
                next_collision['intersection']
            )
            covered = self.weekly_facade_1.covered(next_real_intersection)
            if covered:
                del collisions['next']

        if collisions:
            return collisions
        else:
            return None

    def transform_collisions(self, collisions):
        new_collisions = {}

        if not collisions:
            return None

        prev_collision = collisions.get('prev', None)
        if prev_collision:
            new_collisions['prev'] = prev_collision['day_number']

        current_collision = collisions.get('current', None)
        if current_collision:
            new_collisions['current'] = current_collision['day_number']

        next_collision = collisions.get('next', None)
        if next_collision:
            new_collisions['next'] = next_collision['day_number']

        return new_collisions

    def resolve(self):
        base_collisions = self.get_base_collisions()

        range_1 = self.weekly_facade_1.assignation.range_obj
        range_2 = self.weekly_facade_2.assignation.range_obj

        total_collisions = {}

        intersection = RangeOperator.get_intersection(range_1, range_2)
        aux_date = intersection.starting_date
        while aux_date <= intersection.ending_date:
            week_day = aux_date.weekday()
            main_day = self.weekly_facade_1.get_day(week_day)

            collisions = self.get_day_collisions(main_day, base_collisions)

            if collisions:
                collisions = self.filter_by_days_off(aux_date, collisions)

            if collisions:
                collisions = self.transform_collisions(collisions)

            if collisions:
                str_date = f"{aux_date}"
                total_collisions[str_date] = [main_day.day_number, collisions]

            aux_date += timedelta(days=1)

        if total_collisions:
            return total_collisions
        else:
            return None
