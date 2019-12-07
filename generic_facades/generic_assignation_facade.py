# make all type hints be strings and skip evaluating them
from __future__ import annotations

import copy

from datetime import datetime, timedelta
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from proxies.assignation_proxy import AssignationProxy


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
        copied.workshift = assign.workshift
        copied.person = assign.person
        copied.obj.id = None
        return copied
