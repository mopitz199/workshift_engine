from datetime import datetime, timedelta
from assignation.operators.range_operator import RangeOperator
from collisions.utils import Util


class CycleToWeeklyColission(object):

    def __init__(self, cycle_facade, weekly_facade):
        self.base_prev_date = datetime(2000, 5, 5).date()
        self.base_current_date = datetime(2000, 5, 6).date()
        self.base_next_date = datetime(2000, 5, 7).date()
        self.cycle_facade = cycle_facade
        self.weekly_facade = weekly_facade

    def week_is_full(self, week):
        for key in week:
            if not week[key]:
                return False
        return True

    def cycle_day_revision(self, begining_date):
        ending_date = self.cycle_facade.get_ending_date()
        total_days = self.cycle_facade.get_total_days()

        week = {
            '0': False,
            '1': False,
            '2': False,
            '3': False,
            '4': False,
            '5': False,
            '6': False
        }

        current_date = begining_date
        while current_date <= ending_date:
            weekday = current_date.weekday()
            weekday_str = "{}".format(weekday)
            if not week[weekday_str]:
                week[weekday_str] = True

            if self.week_is_full(week):
                return week

            current_date += timedelta(days=total_days+1)

        return week

    def cycle_day_full_revision(self, begining_date):
        ending_date = self.cycle_facade.get_ending_date()
        total_days = self.cycle_facade.get_total_days()

        week = {
            '0': [],
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': []
        }

        current_date = begining_date
        while current_date <= ending_date:
            weekday = current_date.weekday()
            weekday_str = "{}".format(weekday)
            week[weekday_str].append(current_date)
            current_date += timedelta(days=total_days)

        return week

    def check_prev_colision(self, current_day_name, main_range):
        prev_day_name = self.weekly_facade.get_prev_day_name(current_day_name)
        prev_range = self.weekly_facade.range_obj_from_day_name(
                    prev_day_name,
                    self.base_prev_date)

        if not prev_range:
            return False

        return RangeOperator.are_intersection(prev_range, main_range)

    def check_current_colision(self, current_day_name, main_range):
        current_range = self.weekly_facade.range_obj_from_day_name(
                    current_day_name,
                    self.base_current_date)

        if not current_range:
            return False

        return RangeOperator.are_intersection(current_range, main_range)

    def check_next_colision(self, current_day_name, main_range):
        next_day_name = self.weekly_facade.get_next_day_name(current_day_name)
        next_range = self.weekly_facade.range_obj_from_day_name(
                    next_day_name,
                    self.base_next_date)

        if not next_range:
            return False

        return RangeOperator.are_intersection(next_range, main_range)

    def check_colisions(self, main_range, week_revision):
        for day_name in week_revision:
            if week_revision[day_name]:
                if self.check_prev_colision(day_name, main_range):
                    return True
                if self.check_current_colision(day_name, main_range):
                    return True
                if self.check_next_colision(day_name, main_range):
                    return True
                return False

    def resolve(self):

        for main_day in self.cycle_facade.get_days():

            if main_day.starting_time is not None and main_day.ending_time is not None:
                main_range = Util.create_range(
                    main_day.starting_time,
                    main_day.ending_time,
                    self.base_current_date
                )

                begining_date = self.cycle_facade.get_first_date_of_day_number(
                    main_day.day_number)

                week_revision = self.cycle_day_revision(begining_date)
                week_full_revision = self.cycle_day_full_revision(
                    begining_date)
                has_collision = self.check_colisions(main_range, week_revision)
                if has_collision:
                    return True
        return False
