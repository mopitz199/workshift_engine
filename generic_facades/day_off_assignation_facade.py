from typing import Optional

from datetime import datetime, timedelta, date as dateclass

from utils.range_datetime_operator import RangeDateTimeOperator
from utils.range import Range
from utils.range_datetime import RangeDateTime
from utils.range_operator import RangeOperator


class DayOffAssignationFacade(object):

    def __init__(self, day_off_assignation):
        self.day_off_assignation = day_off_assignation

    def get_as_a_range_datetime(self) -> RangeDateTime:
        starting_date = self.day_off_assignation.starting_date
        starting_time = self.day_off_assignation.starting_time
        ending_date = self.day_off_assignation.ending_date
        ending_time = self.day_off_assignation.ending_time
        return RangeDateTime(
            datetime.combine(starting_date, starting_time),
            datetime.combine(ending_date, ending_time)
        )

    def covers_a_whole_day(self):
        starting_time = self.day_off_assignation.starting_time
        ending_time = self.day_off_assignation.ending_time

        current_date = datetime(2000, 1, 1).date()
        next_date = datetime(2000, 1, 2).date()

        if starting_time > ending_time:
            starting_date = datetime.combine(current_date, starting_time)
            ending_date = datetime.combine(next_date, ending_time)
        else:
            starting_date = datetime.combine(current_date, starting_time)
            ending_date = datetime.combine(current_date, ending_time)

        return (ending_date - starting_date).seconds == 86340

    def one_day_to_another(self):
        starting_time = self.day_off_assignation.starting_time
        ending_time = self.day_off_assignation.ending_time
        return starting_time > ending_time

    def _build_example_from_date(
        self,
        date_obj: dateclass
    ) -> Optional[RangeDateTime]:

        starting_date = self.day_off_assignation.starting_date
        ending_date = self.day_off_assignation.ending_date

        if starting_date <= date_obj <= ending_date:
            example_starting_datetime = datetime.combine(
                date_obj,
                self.day_off_assignation.starting_time
            )

            if self.one_day_to_another():
                example_ending_datetime = datetime.combine(
                    date_obj + timedelta(days=1),
                    self.day_off_assignation.ending_time
                )
            else:
                example_ending_datetime = datetime.combine(
                    date_obj,
                    self.day_off_assignation.ending_time
                )

            return RangeDateTime(
                example_starting_datetime,
                example_ending_datetime
            )
        else:
            return None

    def _check_border_range(
        self,
        border_range_datetime: RangeDateTime
    ) -> bool:
        if not self.covers_a_whole_day():
            starting_date = border_range_datetime.starting_datetime.date()

            previous_date = starting_date - timedelta(days=1)
            current_date = starting_date

            range_datetime = self._build_example_from_date(previous_date)
            if range_datetime:
                if RangeDateTimeOperator.is_in(
                    border_range_datetime,
                    range_datetime
                ):
                    return True

            range_datetime = self._build_example_from_date(current_date)
            if range_datetime:
                if RangeDateTimeOperator.is_in(
                    border_range_datetime,
                    range_datetime
                ):
                    return True
        else:
            range_datetime = self.get_as_a_range_datetime()
            if RangeDateTimeOperator.is_in(
                border_range_datetime,
                range_datetime
            ):
                return True
        return False

    def _check_body(
        self,
        body_range: Range
    ) -> bool:
        r1 = Range(
            self.day_off_assignation.starting_date,
            self.day_off_assignation.ending_date
        )
        return (
            RangeOperator.is_in(body_range, r1) and
            self.covers_a_whole_day()
        )

    def is_in(self, range_datetime):
        split_data = RangeDateTimeOperator.split_borders(
            range_datetime
        )

        left_range_datetime = split_data[0]
        body = split_data[1]
        right_range_datetime = split_data[2]

        left_response = True
        if left_range_datetime:
            left_response = self._check_border_range(left_range_datetime)

        right_response = True
        if right_range_datetime:
            right_response = self._check_border_range(right_range_datetime)

        body_response = True
        if body:
            body_response = self._check_body(body)

        return left_response and right_response and body_response
