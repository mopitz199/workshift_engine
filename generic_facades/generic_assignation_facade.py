# make all type hints be strings and skip evaluating them
from __future__ import annotations

import copy

from datetime import datetime, timedelta
from typing import Any, TYPE_CHECKING, List

from generic_facades.day_off_assignation_facade import DayOffAssignationFacade
from utils.range_datetime_operator import RangeDateTimeOperator

if TYPE_CHECKING:
    from proxies.assignation_proxy import AssignationProxy
    from utils.range_datetime import RangeDateTime
    from utils.range import Range


class GenericAssignationFacade():

    def __init__(
        self,
        assignation: AssignationProxy
    ) -> None:
        self.assignation = assignation

    def copy(
        self
    ) -> AssignationProxy:
        """
        To create a deep copy of a given assign

        :param assign: An assign proxy object
        :type assign: AssignationProxy

        :rtype: AssignationProxy
        """
        assign = self.assignation
        copied = copy.copy(assign)
        copied.obj = copy.deepcopy(assign.obj)
        copied.range_obj = copy.deepcopy(assign.range_obj)
        copied.workshift_proxy = assign.workshift_proxy
        copied.person = assign.person
        copied.obj.id = None
        return copied

    def get_day_off_assignations(self) -> List:
        assignation = self.assignation
        if hasattr(assignation, 'day_off_assignations'):
            return assignation.day_off_assignations
        else:
            return []

    def is_cover_by_a_day_off_assignation(
        self,
        range_obj: RangeDateTime
    ) -> bool:
        day_off_assignations = self.get_day_off_assignations()
        for day_off_assignation in day_off_assignations:
            day_off_assignation_facade = DayOffAssignationFacade(
                day_off_assignation
            )
            if day_off_assignation_facade.is_in(range_obj):
                return True
        return False
