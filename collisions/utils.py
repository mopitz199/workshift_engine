from datetime import datetime, timedelta, time, date as dateclass
from utils.range import Range


class Util(object):

    @staticmethod
    def create_range(
        starting_time: time,
        ending_time: time,
        base_date: dateclass
    ) -> Range:
        starting_datetime = datetime.combine(base_date, starting_time)
        if starting_time > ending_time:
            next_base_date = base_date + timedelta(days=1)
            ending_datetime = datetime.combine(next_base_date, ending_time)
        else:
            ending_datetime = datetime.combine(base_date, ending_time)
        return Range(starting_datetime, ending_datetime)
