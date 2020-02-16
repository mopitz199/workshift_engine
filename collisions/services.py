# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional, Any, List
from datetime import datetime

from collisions.resolvers.cycle_and_week_resolver import CycleToWeeklyColission
from collisions.resolvers.cycle_and_manually_resolver import (
    CycleToManuallyCollision
)
from collisions.resolvers.week_and_manually_resolver import (
    WeeklyAndManuallyCollision
)
from collisions.resolvers.cycle_and_cycle_resolver import CycleToCycleColission
from generic_facades.cycle_assignation_facade import CycleAssignationFacade
from generic_facades.weekly_assignation_facade import WeeklyAssignationFacade
from generic_facades.manually_assignation_facade import ManualAssignationFacade

if TYPE_CHECKING:
    from collisions.custom_typings import (
        CToWResolverType,
        CToMResolverType,
        WToMResolverType,
    )
    from database.assignation_db import AssignationDB
    from proxies.assignation_proxy import AssignationProxy


def cycle_and_weekly_collision(
    assignation1: AssignationProxy,
    assignation2: AssignationProxy
) -> Optional[Dict]:
    """This service is to check if an cycle assignation and a weekly
    assignation has some collision. """

    cycle_facade = CycleAssignationFacade(assignation1)
    weekly_facade = WeeklyAssignationFacade(assignation2)
    resolver = CycleToWeeklyColission(cycle_facade, weekly_facade)
    return resolver.resolve()


def cycle_and_manually_collision(
    assignation1: AssignationProxy,
    assignation2: AssignationProxy
) -> Optional[Dict]:
    """ This service is to check if an cycle assignation and a manual
    assignation has some collision. """

    cycle_facade = CycleAssignationFacade(assignation1)
    manually_facade = ManualAssignationFacade(assignation2)
    resolver = CycleToManuallyCollision(cycle_facade, manually_facade)
    return resolver.resolve()


def weekly_and_manually_collision(
    assignation1: AssignationProxy,
    assignation2: AssignationProxy
) -> Optional[Dict]:
    """ This service is to check if an cycle assignation and a manual
    assignation has some collision. """

    weekly_facade = WeeklyAssignationFacade(assignation1)
    manually_facade = ManualAssignationFacade(assignation2)
    resolver = WeeklyAndManuallyCollision(weekly_facade, manually_facade)
    return resolver.resolve()


def cycle_and_cycle_collision(
    assignation1: AssignationProxy,
    assignation2: AssignationProxy
) -> Optional[Dict]:
    cycle_facade_1 = CycleAssignationFacade(assignation1)
    cycle_facade_2 = CycleAssignationFacade(assignation2)
    resolver = CycleToCycleColission(cycle_facade_1, cycle_facade_2)
    return resolver.resolve()


def check_collisions(
    main_assignation: AssignationProxy,
    assignation_db: AssignationDB
) -> Any:
    assignations: List = []
    for key in assignation_db.db:
        person_id = main_assignation.person_id
        key_to_search = f"_{person_id}"
        if key.endswith(key_to_search):
            assignations += assignation_db.db[key]

    main_workshift_type = main_assignation.workshift_proxy.workshift_type
    for assignation in assignations:
        workshift_type = assignation.workshift_proxy.workshift_type
        if main_workshift_type == 'weekly' and workshift_type == 'manually':
            collisions = weekly_and_manually_collision(
                main_assignation,
                assignation
            )
        elif main_workshift_type == 'manually' and workshift_type == 'weekly':
            collisions = weekly_and_manually_collision(
                assignation,
                main_assignation
            )
        elif main_workshift_type == 'cyclic' and workshift_type == 'manually':
            collisions = cycle_and_manually_collision(
                main_assignation,
                assignation
            )
        elif main_workshift_type == 'manually' and workshift_type == 'cyclic':
            collisions = cycle_and_manually_collision(
                assignation,
                main_assignation
            )
        elif main_workshift_type == 'cyclic' and workshift_type == 'weekly':
            collisions = cycle_and_weekly_collision(
                main_assignation,
                assignation
            )
        elif main_workshift_type == 'weekly' and workshift_type == 'cyclic':
            collisions = cycle_and_weekly_collision(
                assignation,
                main_assignation
            )
        else:
            raise Exception('No workshift type case')

        if collisions:
            return True
        else:
            return False
