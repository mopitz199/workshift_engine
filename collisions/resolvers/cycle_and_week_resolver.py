from datetime import datetime, timedelta
from assignation.operators.range_operator import RangeOperator
from collisions.facades.day_facade import DayFacade
from collisions.utils import Util


class CycleToWeeklyColission(object):

    def __init__(self, cycle_facade, weekly_facade):
        self.base_prev_date = datetime(2000, 5, 5)
        self.base_current_date = datetime(2000, 5, 6)
        self.base_next_date = datetime(2000, 5, 7)
        self.cycle_facade = cycle_facade
        self.weekly_facade = weekly_facade

    def week_is_full(self, week):
        return len(week) == 7

    def cycle_week_day_revision(self, begining_date):
        """To check which days of the week this
        cycle day of the assignation pass through"""

        ending_date = self.cycle_facade.assignation.ending_date
        total_days = self.cycle_facade.get_total_days()

        week_days = []

        current_date = begining_date
        while current_date <= ending_date:
            weekday = current_date.weekday()
            weekday_str = "{}".format(weekday)
            if weekday_str not in week_days:
                week_days.append(weekday_str)

            if self.week_is_full(week_days):
                return week_days

            current_date += timedelta(days=total_days)

        return week_days

    def cycle_week_day_full_revision(self, begining_date):
        """To classify which dates this
        cycle day of the assignation pass through"""

        ending_date = self.cycle_facade.assignation.ending_date
        total_days = self.cycle_facade.get_total_days()

        week = {
            '0': [], '1': [], '2': [],
            '3': [], '4': [], '5': [],
            '6': []}

        current_date = begining_date
        while current_date <= ending_date:
            weekday = current_date.weekday()
            weekday_str = "{}".format(weekday)
            week[weekday_str].append(current_date)
            current_date += timedelta(days=total_days)

        return week

    def check_prev_colision(self, current_day_name, main_range):
        prev_day_name = self.weekly_facade.get_prev_day_number(
            current_day_name)

        prev_range = self.weekly_facade.range_obj_from_day_number(
                    prev_day_name,
                    self.base_prev_date)

        if not prev_range:
            return False

        return RangeOperator.are_intersection(prev_range, main_range)

    def check_current_colision(self, current_day_name, main_range):
        current_range = self.weekly_facade.range_obj_from_day_number(
                    current_day_name,
                    self.base_current_date)

        if not current_range:
            return False

        return RangeOperator.are_intersection(current_range, main_range)

    def check_next_colision(self, current_day_name, main_range):
        next_day_name = self.weekly_facade.get_next_day_number(
            current_day_name)

        next_range = self.weekly_facade.range_obj_from_day_number(
                    next_day_name,
                    self.base_next_date)

        if not next_range:
            return False

        return RangeOperator.are_intersection(next_range, main_range)

    def get_colisions(self, main_range, week_revision):
        day_names = []
        for day_name in week_revision:
            if self.check_prev_colision(day_name, main_range):
                prev_day_name = self.weekly_facade.get_prev_day_number(
                    day_name)
                if prev_day_name not in day_names:
                    day_names.append(prev_day_name)
            elif self.check_current_colision(day_name, main_range):
                if day_name not in day_names:
                    day_names.append(day_name)
            elif self.check_next_colision(day_name, main_range):
                next_day_name = self.weekly_facade.get_next_day_number(
                    day_name)
                if next_day_name not in day_names:
                    day_names.append(next_day_name)
        return day_names

    def resolve(self, detail=False):
        for day in self.cycle_facade.get_days():
            day_facade = DayFacade(day)
            if day_facade.is_working_day():
                main_range = Util.create_range(
                    day.starting_time,
                    day.ending_time,
                    self.base_current_date
                )

                begining_date = self.cycle_facade.get_first_date_of_day_number(
                    day.day_number)

                week_revision = self.cycle_week_day_revision(begining_date)
                week_full_revision = {}
                if detail:
                    week_full_revision = self.cycle_week_day_full_revision(
                        begining_date)

                collisions = self.get_colisions(main_range, week_revision)
                import pdb; pdb.set_trace()
                if collisions:
                    return True, week_full_revision
        return False, week_full_revision
