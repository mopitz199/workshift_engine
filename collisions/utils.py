from datetime import datetime, timedelta
from utils.range import Range


class Util(object):

    @staticmethod
    def create_range(starting_time, ending_time, base_date):
        starting_datetime = datetime.combine(base_date, starting_time)
        if starting_time > ending_time:
            next_base_date = base_date + timedelta(days=1)
            ending_datetime = datetime.combine(base_date, next_base_date)
        else:
            ending_datetime = datetime.combine(base_date, ending_time)
        return Range(starting_datetime, ending_datetime)
