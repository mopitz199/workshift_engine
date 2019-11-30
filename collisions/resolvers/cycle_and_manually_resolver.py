from datetime import datetime, timedelta

from assignation.operators.range_operator import RangeOperator
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.utils import Util
from generic_facades.day_facade import DayFacade


class CycleToManuallyCollision():

    def __init__(self, cycle_facade, manually_facade):
        self.base_prev_date = BASE_PREV_DATE
        self.base_current_date = BASE_CURRENT_DATE
        self.base_next_date = BASE_NEXT_DATE
        self.cycle_facade = cycle_facade
        self.manually_facade = manually_facade

    def can_check_collision(self, manually_day, check_type):
        manually_date = manually_day.date
        aux_starting_date = self.cycle_facade.assignation.starting_date
        aux_ending_date = self.cycle_facade.assignation.ending_date

        if check_type == 'previous':
            aux_starting_date = aux_starting_date + timedelta(days=1)
            aux_ending_date = aux_ending_date + timedelta(days=1)
        elif check_type == 'next':
            aux_starting_date = aux_starting_date - timedelta(days=1)
            aux_ending_date = aux_ending_date - timedelta(days=1)
        elif check_type == 'current':
            pass
        else:
            raise Exception('Unknown check type')

        return aux_starting_date <= manually_date <= aux_ending_date

    def check_prev_collision(self, manually_day, cycle_day):
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

    def check_current_collision(self, manually_day, cycle_day):
        current_range = self.cycle_facade.range_obj_from_day_number(
            cycle_day,
            self.base_current_date)

        manually_range = self.manually_facade.range_obj_from_day(
            manually_day,
            self.base_current_date)

        return RangeOperator.are_intersection(current_range, manually_range)

    def check_next_collision(self, manually_day, cycle_day):
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

    def ensure_empty_list(self, collisions, key):
        if key not in collisions:
            collisions[key] = []
        return collisions

    def resolve(self, detail=False):

        manually_days = self.manually_facade.get_days()
        collisions = {}
        for manually_day in manually_days:
            date = manually_day.date
            str_date = str(date)

            day_number = self.cycle_facade.simulate_starting_day(
                date) - 1

            cycle_day = self.cycle_facade.get_day_data(day_number)

            if self.can_check_collision(manually_day, 'previous'):
                if self.check_prev_collision(manually_day, cycle_day):
                    if detail:
                        collisions = self.ensure_empty_list(collisions, str_date)
                        prev_day_number = self.cycle_facade.get_prev_day_number(
                            day_number
                        )
                        collisions[str_date].append(prev_day_number)
                    else:
                        return True, collisions

            if self.can_check_collision(manually_day, 'current'):
                if self.check_current_collision(manually_day, cycle_day):
                    if detail:
                        collisions = self.ensure_empty_list(collisions, str_date)
                        collisions[str_date].append(day_number)
                    else:
                        return True, collisions

            if self.can_check_collision(manually_day, 'next'):
                if self.check_next_collision(manually_day, cycle_day):
                    if detail:
                        collisions = self.ensure_empty_list(collisions, str_date)
                        next_day_number = self.cycle_facade.get_next_day_number(
                            day_number
                        )
                        collisions[str_date].append(next_day_number)
                    else:
                        return True, collisions

        if collisions:
            return True, collisions
        else:
            return False, collisions
