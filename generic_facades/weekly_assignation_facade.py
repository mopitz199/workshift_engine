# make all type hints be strings and skip evaluating them
from __future__ import annotations

from datetime import date as dateclass
from typing import Any, List, Union, Optional, TYPE_CHECKING

from collisions.utils import Util
from generic_facades.generic_assignation_facade import GenericAssignationFacade

if TYPE_CHECKING:
    from proxies.assignation_proxy import AssignationProxy
    from utils.range_datetime import RangeDateTime


class WeeklyAssignationFacade(GenericAssignationFacade):

    def __init__(
        self,
        assignation: AssignationProxy
    ) -> None:
        self.assignation = assignation

    def get_day(
        self,
        day_number: str
    ) -> Any:
        day_number = f'{day_number}'
        dict_days = self.assignation.workshift_proxy.get_dict_days()
        return dict_days[day_number]

    def get_next_day_number(
        self,
        day_number: Union[int, str]
    ) -> str:
        day_number = int(day_number)
        if day_number == 6:
            return '0'
        else:
            return '{}'.format(day_number + 1)

    def get_next_day(self, weekly_day):
        day_number = weekly_day.day_number
        next_day_number = self.get_next_day_number(day_number)
        return self.get_day(next_day_number)

    def get_prev_day_number(
        self,
        day_number: Union[str, int]
    ) -> str:
        day_number = int(day_number)
        if day_number == 0:
            return '6'
        else:
            return '{}'.format(day_number - 1)

    def get_prev_day(self, weekly_day):
        day_number = weekly_day.day_number
        prev_day_number = self.get_prev_day_number(day_number)
        return self.get_day(prev_day_number)

    def range_datetime_obj_from_day_number(
        self,
        day_number: str,
        base_date: dateclass
    ) -> Optional[RangeDateTime]:
        day = self.get_day(day_number)
        starting_time = day.starting_time
        ending_time = day.ending_time
        if starting_time is not None and ending_time is not None:
            range_datetime = Util.create_range_datetime(
                starting_time,
                ending_time,
                base_date
            )
            return range_datetime
        else:
            return None

    def range_datetime_from_weekly_day(
        self,
        weekly_day: Any,
        base_date: dateclass
    ) -> Optional[RangeDateTime]:
        day_number = weekly_day.day_number
        str_day_number = str(day_number)
        range_datetime = self.range_datetime_obj_from_day_number(
            str_day_number,
            base_date
        )
        return range_datetime
