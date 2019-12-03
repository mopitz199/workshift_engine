from typing import Any, Dict, List, Tuple, NewType, Union

from datetime import datetime, timedelta

from assignation.operators.range_operator import RangeOperator
from collisions.constants import (
    PREVIOUS,
    CURRENT,
    NEXT
)
from collisions.custom_typings import CollisionType
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.utils import Util

from generic_facades.cycle_assignation_facade import CycleAssignationFacade
from generic_facades.day_facade import DayFacade
from generic_facades.manually_assignation_facade import ManualAssignationFacade


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

    def check_prev_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> bool:
        day_number = cycle_day.day_number
        prev_day_number = self.cycle_facade.get_prev_day_number(day_number)
        prev_cycle_day = self.cycle_facade.get_day_data(prev_day_number)
        prev_range = self.cycle_facade.range_obj_from_day_number(
            prev_cycle_day,
            self.base_prev_date)

        manually_range = self.manually_facade.range_obj_from_day(
            manually_day,
            self.base_current_date)

        return RangeOperator.are_intersection(prev_range, manually_range)

    def check_current_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> bool:
        current_range = self.cycle_facade.range_obj_from_day_number(
            cycle_day,
            self.base_current_date)

        manually_range = self.manually_facade.range_obj_from_day(
            manually_day,
            self.base_current_date)

        return RangeOperator.are_intersection(current_range, manually_range)

    def check_next_collision(
        self,
        manually_day: Any,
        cycle_day: Any
    ) -> bool:
        day_number = cycle_day.day_number
        next_day_number = self.cycle_facade.get_next_day_number(day_number)
        next_cycle_day = self.cycle_facade.get_day_data(next_day_number)
        next_range = self.cycle_facade.range_obj_from_day_number(
            next_cycle_day,
            self.base_next_date)

        manually_range = self.manually_facade.range_obj_from_day(
            manually_day,
            self.base_current_date)

        return RangeOperator.are_intersection(next_range, manually_range)

    def ensure_empty_list(
        self,
        collisions: CollisionType,
        key: str
    ) -> None:
        if key not in collisions:
            collisions[key] = []

    def try_check_prev_collision(
        self,
        manually_day: Any,
        cycle_day: Any,
        detail=False
    ) -> Tuple[bool, CollisionType]:
        collisions = CollisionType({})
        if self.can_check_collision(manually_day, PREVIOUS):
            date = manually_day.date
            str_date = str(date)

            if self.check_prev_collision(manually_day, cycle_day):
                if detail:
                    self.ensure_empty_list(collisions, str_date)
                    prev_day_number = self.cycle_facade.get_prev_day_number(
                        cycle_day.day_number
                    )
                    collisions[str_date].append(prev_day_number)
                return (True, collisions)
        return (False, collisions)

    def try_check_current_collision(
        self,
        manually_day: Any,
        cycle_day: Any,
        detail: bool = False
    ) -> Tuple[bool, CollisionType]:
        collisions = CollisionType({})
        if self.can_check_collision(manually_day, CURRENT):
            date = manually_day.date
            str_date = str(date)
            day_number = cycle_day.day_number

            if self.check_current_collision(manually_day, cycle_day):
                if detail:
                    self.ensure_empty_list(collisions, str_date)
                    collisions[str_date].append(day_number)

                return (True, collisions)
        return (False, collisions)

    def try_check_next_collision(
        self,
        manually_day: Any,
        cycle_day: Any,
        detail: bool = False
    ) -> Tuple[bool, CollisionType]:
        collisions = CollisionType({})
        if self.can_check_collision(manually_day, NEXT):
            date = manually_day.date
            str_date = str(date)
            day_number = cycle_day.day_number

            if self.check_next_collision(manually_day, cycle_day):
                if detail:
                    self.ensure_empty_list(collisions, str_date)
                    next_day_number = self.cycle_facade.get_next_day_number(
                        day_number
                    )
                    collisions[str_date].append(next_day_number)
                else:
                    return (True, collisions)
        return (False, collisions)

    def check_manually_day_collision(
        self,
        manually_day: Any,
        detail: bool = False
    ) -> Tuple[bool, CollisionType]:
        collisions = CollisionType({})
        date = manually_day.date
        str_date = str(date)
        day_number = self.cycle_facade.simulate_starting_day(
            date) - 1

        cycle_day = self.cycle_facade.get_day_data(day_number)

        has_collision, prev_collisions = self.try_check_prev_collision(
            manually_day,
            cycle_day,
            detail
        )
        if not detail and has_collision:
            return has_collision, collisions

        has_collision, current_collisions = self.try_check_current_collision(
            manually_day,
            cycle_day,
            detail
        )
        if not detail and has_collision:
            return has_collision, collisions

        has_collision, next_collisions = self.try_check_next_collision(
            manually_day,
            cycle_day,
            detail
        )
        if not detail and has_collision:
            return has_collision, collisions

        if prev_collisions or current_collisions or next_collisions:
            collisions[str_date] = []
            collisions[str_date] += prev_collisions.get(str_date, [])
            collisions[str_date] += current_collisions.get(str_date, [])
            collisions[str_date] += next_collisions.get(str_date, [])

        has_collision = False
        if collisions:
            has_collision = True
        return (has_collision, collisions)

    def resolve(
        self,
        detail: bool = False
    ) -> Tuple[bool, CollisionType]:
        collisions = CollisionType({})
        manually_days = self.manually_facade.get_days()
        for manually_day in manually_days:
            has_collision, aux_collisions = self.check_manually_day_collision(
                manually_day,
                detail
            )
            collisions.update(aux_collisions)

            if not detail and has_collision:
                return has_collision, collisions

        has_collision = False
        if collisions:
            has_collision = True
        return (has_collision, collisions)
