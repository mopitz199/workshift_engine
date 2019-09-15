from datetime import datetime
from collisions.resolvers.cycle_to_week_resolver import CycleToWeeklyColission
from collisions.facades.cycle_assignation_facade import CycleAssignationFacade
from collisions.facades.weekly_assignation_facade import WeeklyAssignationFacade


def check(assignation1, assignation2):
    weekly_facade = WeeklyAssignationFacade(assignation1)
    cycle_facade = CycleAssignationFacade(assignation2)
    resolver = CycleToWeeklyColission(cycle_facade, weekly_facade)
    return resolver.cycle_to_weekly_colision()
