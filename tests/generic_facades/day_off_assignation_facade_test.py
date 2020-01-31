from datetime import datetime

from generic_facades.day_off_assignation_facade import DayOffAssignationFacade
from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts,
    create_proxy_day_off_assignation,
)
from utils.range_datetime import RangeDateTime


class TestDayOffAssignationFacade(object):

    def test_has_collision_1(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-1-2',
                'ending_date': '2019-1-4',
                'starting_time': '10:01',
                'ending_time': '12:00'
            }
        ]
        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )

        facade = DayOffAssignationFacade(day_off_assignations[0])

        range_datetime = RangeDateTime(
            datetime(2019, 1, 1, 10, 0),
            datetime(2019, 1, 2, 10, 0),
        )

        assert not facade.has_collision(range_datetime)

    def test_has_collision_2(self):

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
            datetime(2019, 1, 1, 10, 0),
            datetime(2019, 1, 2, 10, 0),
        )

        assert facade.has_collision(range_datetime)
