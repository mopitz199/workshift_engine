# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime

from collisions.resolvers.cycle_and_week_resolver import CycleToWeeklyColission
from collisions.resolvers.cycle_and_manually_resolver import (
    CycleToManuallyCollision
)
from collisions.resolvers.week_and_manually_resolver import (
    WeeklyAndManuallyCollision
)
from generic_facades.cycle_assignation_facade import CycleAssignationFacade
from generic_facades.weekly_assignation_facade import WeeklyAssignationFacade
from generic_facades.manually_assignation_facade import ManualAssignationFacade

if TYPE_CHECKING:
    from collisions.custom_typings import (
        CToWResolverType,
        CToMResolverType,
        WToMResolverType,
    )
    from proxies.assignation_proxy import AssignationProxy


def cycle_and_weekly_collision(
    assignation1: AssignationProxy,
    assignation2: AssignationProxy,
    detail=False
) -> CToWResolverType:
    """This service is to check if an cycle assignation and a weekly
    assignation has some collision. """

    cycle_facade = CycleAssignationFacade(assignation1)
    weekly_facade = WeeklyAssignationFacade(assignation2)
    resolver = CycleToWeeklyColission(cycle_facade, weekly_facade)
    return resolver.resolve()


def cycle_and_manually_collision(
    assignation1: AssignationProxy,
    assignation2: AssignationProxy,
    detail=False
) -> CToMResolverType:
    """ This service is to check if an cycle assignation and a manual
    assignation has some collision. """

    cycle_facade = CycleAssignationFacade(assignation1)
    manually_facade = ManualAssignationFacade(assignation2)
    resolver = CycleToManuallyCollision(cycle_facade, manually_facade)
    return resolver.resolve(detail)


def weekly_and_manually_collision(
    assignation1: AssignationProxy,
    assignation2: AssignationProxy,
    detail=False
) -> WToMResolverType:
    """ This service is to check if an cycle assignation and a manual
    assignation has some collision. """

    weekly_facade = WeeklyAssignationFacade(assignation1)
    manually_facade = ManualAssignationFacade(assignation2)
    resolver = WeeklyAndManuallyCollision(weekly_facade, manually_facade)
    return resolver.resolve(detail)
