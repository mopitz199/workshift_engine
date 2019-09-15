from datetime import datetime
from collisions.resolvers.cycle_to_week_resolver import CycleToWeeklyColission
from collisions.facades.cycle_assignation_facade import CycleAssignationFacade
from collisions.facades.weekly_assignation_facade import WeeklyAssignationFacade


def cycle_to_weekly_collision(assignation1, assignation2):
    cycle_facade = CycleAssignationFacade(assignation1)
    weekly_facade = WeeklyAssignationFacade(assignation2)
    resolver = CycleToWeeklyColission(cycle_facade, weekly_facade)
    return resolver.resolve()
