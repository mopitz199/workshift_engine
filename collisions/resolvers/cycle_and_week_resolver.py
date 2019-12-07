from typing import List, Dict, Tuple
from datetime import datetime, timedelta, date as dateclass

from assignation.operators.range_operator import RangeOperator
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.custom_typings import CToWResolverType, CToWCollisionType
from collisions.utils import Util

from generic_facades.cycle_assignation_facade import CycleAssignationFacade
from generic_facades.day_facade import DayFacade
from generic_facades.weekly_assignation_facade import WeeklyAssignationFacade

from utils.range import Range


class CycleToWeeklyColission(object):

    def __init__(
        self,
        cycle_facade: CycleAssignationFacade,
        weekly_facade: WeeklyAssignationFacade,
    ) -> None:
        self.base_prev_date = BASE_PREV_DATE
        self.base_current_date = BASE_CURRENT_DATE
        self.base_next_date = BASE_NEXT_DATE
        self.cycle_facade = cycle_facade
        self.weekly_facade = weekly_facade

    def week_is_full(
        self,
        week: List
    ) -> bool:
        return len(week) == 7

    def cycle_week_day_revision(
        self,
        begining_date: dateclass
    ) -> List:
        """To check which days of the week this
        cycle day of the assignation pass through"""

        ending_date = self.cycle_facade.assignation.ending_date
        total_days = self.cycle_facade.get_total_days()

        week_days = []  # type: List

        current_date = begining_date
        while current_date <= ending_date:
            weekday = current_date.weekday()
            weekday_str = "{}".format(weekday)
            if weekday_str not in week_days:
                week_days.append(weekday_str)

            if self.week_is_full(week_days):
                return week_days

            current_date += timedelta(days=total_days)

        return week_days

    def cycle_week_day_full_revision(
        self,
        begining_date: dateclass
    ) -> Dict[str, List]:
        """To classify which dates this
        cycle day of the assignation pass through"""

        ending_date = self.cycle_facade.assignation.ending_date
        total_days = self.cycle_facade.get_total_days()

        week = {}  # type: Dict[str, List]
        current_date = begining_date
        while current_date <= ending_date:
            weekday = current_date.weekday()
            weekday_str = "{}".format(weekday)
            if weekday_str not in week:
                week[weekday_str] = []

            week[weekday_str].append(current_date)
            current_date += timedelta(days=total_days)

        return week

    def check_prev_colision(
        self,
        current_day_name: str,
        main_range: Range
    ) -> bool:
        prev_day_name = self.weekly_facade.get_prev_day_number(
            current_day_name)

        prev_range = self.weekly_facade.range_obj_from_day_number(
                    prev_day_name,
                    self.base_prev_date)

        if not prev_range:
            return False

        return RangeOperator.are_intersection(prev_range, main_range)

    def check_current_colision(
        self,
        current_day_name: str,
        main_range: Range
    ) -> bool:
        current_range = self.weekly_facade.range_obj_from_day_number(
                    current_day_name,
                    self.base_current_date)

        if not current_range:
            return False

        return RangeOperator.are_intersection(current_range, main_range)

    def check_next_colision(
        self,
        current_day_name: str,
        main_range: Range
    ) -> bool:
        next_day_name = self.weekly_facade.get_next_day_number(
            current_day_name)

        next_range = self.weekly_facade.range_obj_from_day_number(
                    next_day_name,
                    self.base_next_date)

        if not next_range:
            return False

        return RangeOperator.are_intersection(next_range, main_range)

    def has_collision(
        self,
        main_range: Range,
        week_revision: List
    ) -> bool:
        for day_name in week_revision:
            if self.check_prev_colision(day_name, main_range):
                return True
            if self.check_current_colision(day_name, main_range):
                return True
            if self.check_next_colision(day_name, main_range):
                return True
        return False

    def filter_dates(
        self,
        dates: List,
        collision_type: str
    ) -> List:
        ending_date = self.weekly_facade.assignation.ending_date

        starting_date = self.weekly_facade.assignation.starting_date

        if collision_type == 'previous':
            return list(filter(lambda d: d > starting_date, dates))

        if collision_type == 'next':
            return list(filter(lambda d: d < ending_date, dates))

        if collision_type == 'current':
            return list(filter(lambda d: d <= ending_date, dates))

        return dates

    def get_collision_detail(
        self,
        main_range: Range,
        week_full_revision: Dict
    ) -> Dict:
        day_names = {}  # type: Dict
        for day_name in week_full_revision:
            dates = week_full_revision[day_name]
            if self.check_prev_colision(day_name, main_range):
                prev_day_name = self.weekly_facade.get_prev_day_number(
                    day_name)

                dates = self.filter_dates(dates, 'previous')
                if dates:
                    if prev_day_name not in day_names:
                        day_names[prev_day_name] = []
                    day_names[prev_day_name] += dates

            if self.check_current_colision(day_name, main_range):
                dates = self.filter_dates(dates, 'current')
                if dates:
                    if day_name not in day_names:
                        day_names[day_name] = []
                    day_names[day_name] += dates

            if self.check_next_colision(day_name, main_range):
                next_day_name = self.weekly_facade.get_next_day_number(
                    day_name)

                dates = self.filter_dates(dates, 'next')
                if dates:
                    if next_day_name not in day_names:
                        day_names[next_day_name] = []
                    day_names[next_day_name] += dates

        return day_names

    def resolve(
        self,
        detail=False
    ) -> CToWResolverType:
        collision_detail = {}  # Type: CToWCollisionType
        has_collisions = False
        for day in self.cycle_facade.get_days():
            day_facade = DayFacade(day)
            if day_facade.is_working_day():

                cycle_day_range = Util.create_range(
                    day.starting_time,
                    day.ending_time,
                    self.base_current_date
                )

                begining_date = self.cycle_facade.get_first_date_of_day_number(
                    day.day_number)

                week_revision = self.cycle_week_day_revision(begining_date)

                week_full_revision = {}  # type: Dict
                if detail:
                    week_full_revision = self.cycle_week_day_full_revision(
                        begining_date)

                if detail:
                    collision_day_detail = self.get_collision_detail(
                        cycle_day_range,
                        week_full_revision)
                    day_str_number = "{}".format(day.day_number)
                    collision_detail[day_str_number] = collision_day_detail

                collisions = self.has_collision(cycle_day_range, week_revision)

                if collisions and not has_collisions:
                    has_collisions = True

                if has_collisions and not detail:
                    return CToWResolverType(
                        (True, CToWCollisionType(collision_detail))
                    )
        return CToWResolverType(
            (has_collisions, CToWCollisionType(collision_detail))
        )
