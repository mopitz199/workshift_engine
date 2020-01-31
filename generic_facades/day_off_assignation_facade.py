from datetime import datetime, timedelta

from utils.range_datetime_operator import RangeDateTimeOperator
from utils.range import Range
from utils.range_datetime import RangeDateTime
from utils.range_operator import RangeOperator


class DayOffAssignationFacade(object):

    def __init__(self, day_off_assignation):
        self.day_off_assignation = day_off_assignation

    def has_collision(self, range_datetime):
        split_data = RangeDateTimeOperator.split_borders(
            range_datetime
        )

        left_range_datetime = split_data[0]
        body = split_data[1]
        right_range_datetime = split_data[2]

        if right_range_datetime and not body:
            joined_range_datetime = RangeDateTime(
                left_range_datetime.starting_datetime,
                right_range_datetime.ending_datetime
            )
        else:
            joined_range_datetime = left_range_datetime

        if body:
            r1 = Range(
                self.day_off_assignation.starting_date,
                self.day_off_assignation.ending_date
            )
            if RangeOperator.are_intersection(body, r1):
                return True

        if joined_range_datetime:
            aux_starting_date = joined_range_datetime.starting_datetime.date()
            if self.date_is_in(aux_starting_date):
                if self.one_day_to_another():
                    ending_date = aux_starting_date + timedelta(days=1)
                else:
                    ending_date = aux_starting_date

                day_off_range = RangeDateTime(
                    datetime.combine(
                        aux_starting_date,
                        self.day_off_assignation.starting_time
                    ),
                    datetime.combine(
                        ending_date,
                        self.day_off_assignation.ending_time
                    )
                )

                return RangeDateTimeOperator.are_intersection(
                    joined_range_datetime,
                    day_off_range
                )

            aux_ending_date = joined_range_datetime.ending_datetime.date()
            if self.date_is_in(aux_ending_date):
                if self.one_day_to_another():
                    ending_date = aux_ending_date + timedelta(days=1)
                else:
                    ending_date = aux_ending_date

                day_off_range = RangeDateTime(
                    datetime.combine(
                        aux_ending_date,
                        self.day_off_assignation.starting_time
                    ),
                    datetime.combine(
                        ending_date,
                        self.day_off_assignation.ending_time
                    )
                )

                return RangeDateTimeOperator.are_intersection(
                    joined_range_datetime,
                    day_off_range
                )

        return False

    def date_is_in(self, date_obj):
        starting_date = self.day_off_assignation.starting_date
        ending_date = self.day_off_assignation.ending_date
        return starting_date <= date_obj <= ending_date

    def one_day_to_another(self):
        starting_time = self.day_off_assignation.starting_time
        ending_time = self.day_off_assignation.ending_time
        return starting_time > ending_time
