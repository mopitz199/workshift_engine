# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import List, Dict, Tuple, Optional, TYPE_CHECKING
from datetime import datetime, timedelta, date as dateclass

from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.custom_typings import CToWResolverType, CToWCollisionType
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
        main_range: RangeDateTime
    ) -> Optional[RangeDateTime]:
        prev_day_name = self.weekly_facade.get_prev_day_number(
            current_day_name)

        prev_range = self.weekly_facade.range_datetime_obj_from_day_number(
                    prev_day_name,
                    self.base_prev_date)

        if not prev_range:
            return None

        intersection = RangeDateTimeOperator.get_intersection(
            prev_range,
            main_range
        )
        if intersection:
            return intersection
        else:
            return None

    def check_current_colision(
        self,
        current_day_name: str,
        main_range: RangeDateTime
    ) -> Optional[RangeDateTime]:
        current_range = self.weekly_facade.range_datetime_obj_from_day_number(
                    current_day_name,
                    self.base_current_date)

        if not current_range:
            return None

        intersection = RangeDateTimeOperator.get_intersection(
            current_range,
            main_range
        )
        if intersection:
            return intersection
        else:
            return None

    def check_next_colision(
        self,
        current_day_name: str,
        main_range: RangeDateTime
    ) -> Optional[RangeDateTime]:
        next_day_name = self.weekly_facade.get_next_day_number(
            current_day_name)

        next_range = self.weekly_facade.range_datetime_obj_from_day_number(
                    next_day_name,
                    self.base_next_date)

        if not next_range:
            return None

        intersection = RangeDateTimeOperator.get_intersection(
            next_range,
            main_range
        )
        if intersection:
            return intersection
        else:
            return None

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

    def not_covered_dates(
        self,
        dates: List[dateclass],
        intersection: RangeDateTime,
        check_type: str = None,
    ):
        filtered_dates = []
        for date_obj in dates:
            if check_type == 'next':
                aux_date_obj = date_obj + timedelta(days=1)
            else:
                aux_date_obj = date_obj

            real_intersection = self.get_real_intersection(
                aux_date_obj,
                intersection
            )

            covered = self.weekly_facade.covered(real_intersection)
            if not covered:
                filtered_dates.append(date_obj)
        return filtered_dates

    def get_collision_detail(
        self,
        main_range: RangeDateTime,
        week_full_revision: Dict
    ) -> Dict:
        day_names = {}  # type: Dict
        for day_name in week_full_revision:
            dates = week_full_revision[day_name]
            intersection = self.check_prev_colision(
                day_name,
                main_range
            )
            if intersection:
                prev_day_name = self.weekly_facade.get_prev_day_number(
                    day_name)

                dates = self.filter_dates(dates, 'previous')
                dates = self.not_covered_dates(
                    dates,
                    intersection
                )
                if dates:
                    if prev_day_name not in day_names:
                        day_names[prev_day_name] = []
                    day_names[prev_day_name] += dates

            intersection = self.check_current_colision(
                day_name,
                main_range
            )
            if intersection:
                dates = self.filter_dates(dates, 'current')
                dates = self.not_covered_dates(
                    dates,
                    intersection
                )
                if dates:
                    if day_name not in day_names:
                        day_names[day_name] = []
                    day_names[day_name] += dates

            intersection = self.check_next_colision(
                day_name,
                main_range
            )
            if intersection:
                next_day_name = self.weekly_facade.get_next_day_number(
                    day_name)

                dates = self.filter_dates(dates, 'next')
                dates = self.not_covered_dates(
                    dates,
                    intersection
                )
                if dates:
                    if next_day_name not in day_names:
                        day_names[next_day_name] = []
                    day_names[next_day_name] += dates

        return day_names

    def resolve(self) -> Optional[Dict]:
        collision_detail = {}
        for day in self.cycle_facade.get_days():
            day_facade = DayFacade(day)
            if day_facade.is_working_day():

                cycle_day_range = Util.create_range_datetime(
                    day.starting_time,
                    day.ending_time,
                    self.base_current_date
                )

                begining_date = self.cycle_facade.get_first_date_of_day_number(
                    day.day_number)

                week_full_revision = {}  # type: Dict
                week_full_revision = self.cycle_week_day_full_revision(
                    begining_date)

                collision_day_detail = self.get_collision_detail(
                    cycle_day_range,
                    week_full_revision)
                day_str_number = "{}".format(day.day_number)
                if collision_day_detail:
                    collision_detail[day_str_number] = collision_day_detail

        if collision_detail:
            return collision_detail
        else:
            return None
