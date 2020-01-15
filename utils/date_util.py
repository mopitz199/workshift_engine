from datetime import (
    datetime,
    date as dateclass,
    time as timeclass,
)


class DateUtil:

    @staticmethod
    def str_to_date(str_date: str) -> dateclass:
        return datetime.strptime(str_date, '%Y-%m-%d').date()

    @staticmethod
    def str_to_time(str_time: str) -> timeclass:
        return datetime.strptime(str_time, '%H:%M').time()

    @staticmethod
    def str_to_datetime(str_datetime: str) -> datetime:
        return datetime.strptime(str_datetime, '%Y-%m-%d %H:%M')

    @staticmethod
    def time_to_str(time_obj) -> str:
        return time_obj.strftime('%H:%M')

    @staticmethod
    def date_to_str(date_obj) -> str:
        return date_obj.strftime('%Y-%m-%d')

    @staticmethod
    def join_date_and_time(date_obj, time_obj):
        str_date = DateUtil.date_to_str(date_obj)
        str_time = DateUtil.time_to_str(time_obj)
        str_datetime = "{} {}".format(str_date, str_time)
        return DateUtil.str_to_datetime(str_datetime)
