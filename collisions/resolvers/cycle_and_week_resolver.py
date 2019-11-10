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

        week = {}
        current_date = begining_date
        while current_date <= ending_date:
            weekday = current_date.weekday()
            weekday_str = "{}".format(weekday)
            if weekday_str not in week:
                week[weekday_str] = []

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

    def has_collision(self, main_range, week_revision):
        for day_name in week_revision:
            if self.check_prev_colision(day_name, main_range):
                return True
            if self.check_current_colision(day_name, main_range):
                return True
            if self.check_next_colision(day_name, main_range):
                return True
        return False

    def filter_dates(self, dates, collision_type):
        ending_date = self.weekly_facade.assignation.ending_date
        starting_date = self.weekly_facade.assignation.starting_date

        if collision_type == 'previous':
            return list(filter(lambda d: d > starting_date, dates))

        if collision_type == 'next':
            return list(filter(lambda d: d < ending_date, dates))

        return dates

    def get_collision_detail(self, main_range, week_full_revision):
        day_names = {}
        for day_name in week_full_revision:
            dates = week_full_revision[day_name]
            if self.check_prev_colision(day_name, main_range):
                prev_day_name = self.weekly_facade.get_prev_day_number(
                    day_name)

                dates = self.filter_dates(dates, 'previous')
                if dates:
                    if prev_day_name not in day_names:
                        day_names[prev_day_name] = []
                    day_names[prev_day_name] += dates

            if self.check_current_colision(day_name, main_range):
                if day_name not in day_names:
                    day_names[day_name] = []
                day_names[day_name] += dates
            if self.check_next_colision(day_name, main_range):
                next_day_name = self.weekly_facade.get_next_day_number(
                    day_name)

                dates = self.filter_dates(dates, 'next')
                if dates:
                    if next_day_name not in day_names:
                        day_names[next_day_name] = []
                    day_names[next_day_name] += dates

            # import pdb; pdb.set_trace()
        return day_names

    def resolve(self, detail=False):
        collision_detail = {}
        has_collisions = False
        for day in self.cycle_facade.get_days():
            day_facade = DayFacade(day)
            if day_facade.is_working_day():

                cycle_day_range = Util.create_range(
                    day.starting_time,
                    day.ending_time,
                    self.base_current_date
                )

                begining_date = self.cycle_facade.get_first_date_of_day_number(
                    day.day_number)

                # Get which days of a week are use by the cycle assignation
                week_revision = self.cycle_week_day_revision(begining_date)

                # The same as week revision but with the detail of each cycle date
                week_full_revision = {}
                if detail:
                    week_full_revision = self.cycle_week_day_full_revision(
                        begining_date)

                if detail:
                    # Get the collsion detail of each cycle date
                    collision_day_detail = self.get_collision_detail(
                        cycle_day_range,
                        week_full_revision)
                    day_str_number = "{}".format(day.day_number)
                    collision_detail[day_str_number] = collision_day_detail

                # Get a ligher way to check if there's some collision
                collisions = self.has_collision(cycle_day_range, week_revision)

                if collisions and not has_collisions:
                    has_collisions = True

                if has_collisions and not detail:
                    return True, collision_detail
        return has_collisions, collision_detail
