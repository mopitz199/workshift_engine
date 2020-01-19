from datetime import datetime

from utils.date_util import DateUtil


class TestDateUtil(object):

    def test_str_to_date1(self):
        str_date = "2019-10-1"
        date_obj = DateUtil.str_to_date(str_date)
        assert date_obj == datetime.strptime(str_date, "%Y-%m-%d").date()

    def test_str_to_date2(self):
        str_date = "2019-10-01"
        date_obj = DateUtil.str_to_date(str_date)
        assert date_obj == datetime.strptime(str_date, "%Y-%m-%d").date()

    def test_str_to_date3(self):
        str_date = "2019-9-01"
        date_obj = DateUtil.str_to_date(str_date)
        assert date_obj == datetime.strptime(str_date, "%Y-%m-%d").date()

    def test_str_to_date4(self):
        str_date = "2019-09-01"
        date_obj = DateUtil.str_to_date(str_date)
        assert date_obj == datetime.strptime(str_date, "%Y-%m-%d").date()

    def test_str_to_date5(self):
        str_date = "2019-09-1"
        date_obj = DateUtil.str_to_date(str_date)
        assert date_obj == datetime.strptime(str_date, "%Y-%m-%d").date()

    def test_str_to_time1(self):
        str_time = "10:10"
        time_obj = DateUtil.str_to_time(str_time)
        assert time_obj == datetime.strptime(str_time, "%H:%M").time()

    def test_str_to_time2(self):
        str_time = "10:01"
        time_obj = DateUtil.str_to_time(str_time)
        assert time_obj == datetime.strptime(str_time, "%H:%M").time()

    def test_str_to_time3(self):
        str_time = "08:10"
        time_obj = DateUtil.str_to_time(str_time)
        assert time_obj == datetime.strptime(str_time, "%H:%M").time()

    def test_str_to_time4(self):
        str_time = "08:01"
        time_obj = DateUtil.str_to_time(str_time)
        assert time_obj == datetime.strptime(str_time, "%H:%M").time()

    def test_str_to_datetime1(self):
        str_datetime = "2019-10-10 08:01"
        datetime_obj = DateUtil.str_to_datetime(str_datetime)
        assert datetime_obj == datetime.strptime(
            str_datetime,
            '%Y-%m-%d %H:%M'
        )

    def test_str_to_datetime2(self):
        str_datetime = "2019-01-03 08:01"
        datetime_obj = DateUtil.str_to_datetime(str_datetime)
        assert datetime_obj == datetime.strptime(
            str_datetime,
            '%Y-%m-%d %H:%M'
        )

    def test_str_to_datetime3(self):
        str_datetime = "2019-10-10 8:1"
        datetime_obj = DateUtil.str_to_datetime(str_datetime)
        assert datetime_obj == datetime.strptime(
            str_datetime,
            '%Y-%m-%d %H:%M'
        )

    def test_time_to_str1(self):
        str_time = "8:1"
        time_obj = datetime.strptime(str_time, '%H:%M').time()
        assert "08:01" == DateUtil.time_to_str(time_obj)

    def test_time_to_str2(self):
        str_time = "08:01"
        time_obj = datetime.strptime(str_time, '%H:%M').time()
        assert "08:01" == DateUtil.time_to_str(time_obj)

    def test_time_to_str3(self):
        str_time = "10:10"
        time_obj = datetime.strptime(str_time, '%H:%M').time()
        assert "10:10" == DateUtil.time_to_str(time_obj)

    def test_date_to_str1(self):
        str_date = "2019-1-1"
        date_obj = datetime.strptime(str_date, '%Y-%m-%d').date()
        assert "2019-01-01" == DateUtil.date_to_str(date_obj)

    def test_date_to_str2(self):
        str_date = "2019-10-10"
        date_obj = datetime.strptime(str_date, '%Y-%m-%d').date()
        assert "2019-10-10" == DateUtil.date_to_str(date_obj)

    def test_join_date_and_time1(self):
        str_time = "10:10"
        time_obj = datetime.strptime(str_time, '%H:%M').time()

        str_date = "2019-1-1"
        date_obj = datetime.strptime(str_date, '%Y-%m-%d').date()

        result = DateUtil.join_date_and_time(date_obj, time_obj)
        expected = datetime.strptime("2019-1-1 10:10", '%Y-%m-%d %H:%M')
        assert result == expected

    def test_join_date_and_time2(self):
        str_time = "01:1"
        time_obj = datetime.strptime(str_time, '%H:%M').time()

        str_date = "2019-1-1"
        date_obj = datetime.strptime(str_date, '%Y-%m-%d').date()

        result = DateUtil.join_date_and_time(date_obj, time_obj)
        expected = datetime.strptime("2019-1-1 01:1", '%Y-%m-%d %H:%M')
        assert result == expected

    def test_join_date_and_time3(self):
        str_time = "1:1"
        time_obj = datetime.strptime(str_time, '%H:%M').time()

        str_date = "2019-01-10"
        date_obj = datetime.strptime(str_date, '%Y-%m-%d').date()

        result = DateUtil.join_date_and_time(date_obj, time_obj)
        expected = datetime.strptime("2019-1-10 1:1", '%Y-%m-%d %H:%M')
        assert result == expected
