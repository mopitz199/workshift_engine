from datetime import datetime

from assignation.operators.range_operator import RangeOperator
from collisions.resolvers.constants import (
    BASE_PREV_DATE,
    BASE_CURRENT_DATE,
    BASE_NEXT_DATE
)
from collisions.utils import Util
from facades.day_facade import DayFacade


class CycleToManualCollision():

    def __init__(self, cycle_facade, manual_facade):
        self.base_prev_date = BASE_PREV_DATE
        self.base_current_date = BASE_CURRENT_DATE
        self.base_next_date = BASE_NEXT_DATE
        self.cycle_facade = cycle_facade
        self.manual_facade = manual_facade

    def resolver(self, detail=False):

        manual_days = self.manual_facade.get_days()
        for manual_day in manual_days:
            manual_day_facade = DayFacade(manual_day)
