from datetime import datetime
from collisions.resolvers.cycle_and_week_resolver import CycleToWeeklyColission
from collisions.facades.cycle_assignation_facade import CycleAssignationFacade
from collisions.facades.weekly_assignation_facade import WeeklyAssignationFacade


def cycle_and_weekly_collision(assignation1, assignation2, detail=False):
    """This service is to check if an cycle assignation and a weekly
    assignation has some collision.

    :param assignation1: A cycle assignation proxy
    :type assignation1: AssignationProxy
    :param assignation2: A weekly assignation proxy
    :type assignation2: AssignationProxy
    :param detail: If you can to calculate the specific dates of collisions
    :type detail: bool
    :return: If has some collision or not and also the detail if the collision if it has
    :rtype: bool, dict
    """

    cycle_facade = CycleAssignationFacade(assignation1)
    weekly_facade = WeeklyAssignationFacade(assignation2)
    resolver = CycleToWeeklyColission(cycle_facade, weekly_facade)
    return resolver.resolve(detail)
