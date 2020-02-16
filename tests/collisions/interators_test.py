from datetime import datetime

from collisions.iterators import CycleDateIterator
from database.workshift_db import WorkShiftDB
from proxies.workshift_proxy import WorkShiftProxy
from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts,
    create_proxy_day_off_assignation,
)


class TestCycleDateIterator:

    def test_cycle_date_iterator_1(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 3,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2020-2-1',
                'ending_date': '2020-2-10',
                'workshift_id': 6,
            }
        }
        assignation = create_an_assignation(
            assignation,
            workshift_db,
            None
        )

        iterator = CycleDateIterator(assignation, 0)

        dates = []
        for date_obj in iterator:
            dates.append(date_obj)

        expected = [
            datetime(2020, 2, 1).date(),
            datetime(2020, 2, 4).date(),
            datetime(2020, 2, 7).date(),
            datetime(2020, 2, 10).date(),
        ]
        assert expected == dates

    def test_cycle_date_iterator_2(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 3,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation = {
            'assignation': {
                'person_id': 1,
                'starting_day': 2,
                'starting_date': '2020-2-1',
                'ending_date': '2020-2-10',
                'workshift_id': 6,
            }
        }
        assignation = create_an_assignation(
            assignation,
            workshift_db,
            None
        )

        iterator = CycleDateIterator(assignation, 0)

        dates = []
        for date_obj in iterator:
            dates.append(date_obj)

        expected = [
            datetime(2020, 2, 3).date(),
            datetime(2020, 2, 6).date(),
            datetime(2020, 2, 9).date()
        ]
        assert expected == dates

    def test_cycle_date_iterator_3(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 3,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation = {
            'assignation': {
                'person_id': 1,
                'starting_day': 2,
                'starting_date': '2020-2-1',
                'ending_date': '2020-2-10',
                'workshift_id': 6,
            }
        }
        assignation = create_an_assignation(
            assignation,
            workshift_db,
            None
        )

        iterator = CycleDateIterator(assignation, 1)

        dates = []
        for date_obj in iterator:
            dates.append(date_obj)

        expected = [
            datetime(2020, 2, 1).date(),
            datetime(2020, 2, 4).date(),
            datetime(2020, 2, 7).date(),
            datetime(2020, 2, 10).date(),
        ]
        assert expected == dates
