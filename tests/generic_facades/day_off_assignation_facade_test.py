from datetime import datetime

from generic_facades.day_off_assignation_facade import DayOffAssignationFacade
from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts,
    create_proxy_day_off_assignation,
)
from utils.range_datetime import RangeDateTime


class TestDayOffAssignationFacade(object):

    def test_is_in_1(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-2',
                'ending_date': '2019-1-4',
                'starting_time': '10:00',
                'ending_time': '12:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 2, 10, 10),
            datetime(2019, 1, 2, 11, 10),
        )

        assert facade.is_in(range_datetime)

    def test_is_in_2(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-2',
                'ending_date': '2019-1-2',
                'starting_time': '10:00',
                'ending_time': '12:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 2, 10, 10),
            datetime(2019, 1, 2, 11, 10),
        )

        assert facade.is_in(range_datetime)

    def test_is_in_3(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-2',
                'ending_date': '2019-1-3',
                'starting_time': '20:00',
                'ending_time': '04:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 4, 1, 10),
            datetime(2019, 1, 4, 2, 10),
        )

        assert facade.is_in(range_datetime)

    def test_is_in_4(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-6',
                'starting_time': '00:00',
                'ending_time': '23:59'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 2, 1, 10),
            datetime(2019, 1, 4, 2, 10),
        )

        assert facade.is_in(range_datetime)

    def test_is_in_5(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-6',
                'starting_time': '06:00',
                'ending_time': '05:59'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 2, 1, 10),
            datetime(2019, 1, 4, 2, 10),
        )

        assert facade.is_in(range_datetime)

    def test_is_in_6(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-6',
                'starting_time': '20:00',
                'ending_time': '05:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 5, 20, 00),
            datetime(2019, 1, 6, 5, 00),
        )

        assert facade.is_in(range_datetime)

    def test_is_not_in_1(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-3',
                'starting_time': '08:00',
                'ending_time': '12:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 1, 7, 0),
            datetime(2019, 1, 1, 9, 0),
        )

        assert not facade.is_in(range_datetime)

    def test_is_not_in_2(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-3',
                'starting_time': '08:00',
                'ending_time': '12:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 1, 7, 59),
            datetime(2019, 1, 1, 8, 0),
        )

        assert not facade.is_in(range_datetime)

    def test_is_not_in_3(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-3',
                'starting_time': '08:00',
                'ending_time': '12:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 1, 9, 0),
            datetime(2019, 1, 1, 12, 1),
        )

        assert not facade.is_in(range_datetime)

    def test_is_not_in_4(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-9',
                'starting_time': '08:00',
                'ending_time': '12:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 2, 9, 0),
            datetime(2019, 1, 4, 12, 1),
        )

        assert not facade.is_in(range_datetime)

    def test_is_not_in_5(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-9',
                'starting_time': '20:00',
                'ending_time': '08:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 2, 19, 59),
            datetime(2019, 1, 3, 8, 0),
        )

        assert not facade.is_in(range_datetime)

    def test_is_not_in_6(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-9',
                'starting_time': '20:00',
                'ending_time': '08:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 2, 20, 59),
            datetime(2019, 1, 3, 8, 1),
        )

        assert not facade.is_in(range_datetime)

    def test_is_not_in_7(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-3',
                'starting_time': '00:00',
                'ending_time': '23:59'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 4, 10, 0),
            datetime(2019, 1, 4, 10, 1),
        )

        assert not facade.is_in(range_datetime)

    """
    def test_is_not_in_8(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-4',
                'starting_time': '9:00',
                'ending_time': '11:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 4, 10, 0),
            datetime(2019, 1, 4, 10, 0),
        )

        assert facade.is_in(range_datetime)
    """