from datetime import datetime

from assignation.operators.range_operator import RangeOperator
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.utils import Util
from generic_facades.day_facade import DayFacade


class CycleToManualCollision():

    def __init__(self, cycle_facade, manual_facade):
        self.base_prev_date = BASE_PREV_DATE
        self.base_current_date = BASE_CURRENT_DATE
        self.base_next_date = BASE_NEXT_DATE
        self.cycle_facade = cycle_facade
        self.manual_facade = manual_facade

    def check_prev_collision(self, manual_day, cycle_day):
        day_number = cycle_day.day_number
        prev_day_number = self.cycle_facade.get_prev_day_number(day_number)
        prev_cycle_day = self.cycle_facade.get_day_data(prev_day_number)
        prev_range = self.cycle_facade.range_obj_from_day_number(
            prev_cycle_day,
            self.base_prev_date)

        manual_range = self.manual_facade.range_obj_from_day(
            manual_day,
            self.base_current_date)

        return RangeOperator.are_intersection(prev_range, manual_range)

    def check_current_collision(self, manual_day, cycle_day):
        current_range = self.cycle_facade.range_obj_from_day_number(
            cycle_day,
            self.base_current_date)

        manual_range = self.manual_facade.range_obj_from_day(
            manual_day,
            self.base_current_date)

        return RangeOperator.are_intersection(current_range, manual_range)

    def check_next_collision(self, manual_day, cycle_day):
        day_number = cycle_day.day_number
        next_day_number = self.cycle_facade.get_next_day_number(day_number)
        next_cycle_day = self.cycle_facade.get_day_data(next_day_number)
        next_range = self.cycle_facade.range_obj_from_day_number(
            next_cycle_day,
            self.base_next_date)

        manual_range = self.manual_facade.range_obj_from_day(
            manual_day,
            self.base_current_date)

        return RangeOperator.are_intersection(next_range, manual_range)

    def resolver(self, detail=False):

        manual_days = self.manual_facade.get_days()
        for manual_day in manual_days:
            date = manual_day.date
            day_number = self.cycle_facade.simulate_starting_day(
                date)

            cycle_day = self.cycle_facade.get_day_data(day_number)

            if self.check_prev_collision(manual_day, cycle_day):
                pass

            if self.check_current_collision(manual_day, cycle_day):
                pass

            if self.check_next_collision(manual_day, cycle_day):
                pass
