# make all type hints be strings and skip evaluating them
from __future__ import annotations

from datetime import datetime, timedelta, date as dateclass
from typing import Any, List, Optional, TYPE_CHECKING

from generic_facades.generic_assignation_facade import GenericAssignationFacade
from collisions.utils import Util

if TYPE_CHECKING:
    from proxies.assignation_proxy import AssignationProxy
    from utils.range import Range


class ManualAssignationFacade(GenericAssignationFacade):

    def __init__(
        self,
        assignation: AssignationProxy
    ) -> None:
        self.assignation = assignation

    def get_days(
        self
    ) -> List[Any]:
        return self.assignation.workshift_proxy.get_days()

    def range_obj_from_day(
        self,
        manually_day: Any,
        base_date: dateclass
    ) -> Optional[Range]:
        starting_time = manually_day.starting_time
        ending_time = manually_day.ending_time
        if starting_time is not None and ending_time is not None:
            return Util.create_range(starting_time, ending_time, base_date)
        else:
            return None
