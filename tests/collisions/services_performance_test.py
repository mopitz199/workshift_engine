from datetime import datetime
import time

import multiprocessing
import threading

import concurrent
import concurrent.futures

from collisions.services import (
    cycle_and_weekly_collision,
    cycle_and_manually_collision,
    weekly_and_manually_collision
)
from database.workshift_db import WorkShiftDB
from database.day_off_assignation_db import DayOffAssignationDB
from proxies.workshift_proxy import WorkShiftProxy
from proxies.day_off_assignation_proxy import DayOffAssignationProxy
from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts,
    create_proxy_day_off_assignation,
)

"""
class TestCycleAndWeeklyCollisionDayOffsPerformance:

    def test_cycle_and_weekly_collision_day_off1(self):

        day_off_assignations_data = []
        for i in range(4000):
            day_off_assignations_data.append(
                {
                    'person_id': i,
                    'starting_date': '2019-1-4',
                    'ending_date': '2025-1-4',
                    'starting_time': '00:00',
                    'ending_time': '00:10'
                }
            )

        day_off_assignations = create_proxy_day_off_assignation(
            day_off_assignations_data
        )
        day_off_assignations_db = DayOffAssignationDB(
            day_off_assignations,
            DayOffAssignationProxy
        )

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 5,
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
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    }

                ]
            },
            {
                'id': 7,
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
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
                        'starting_time': '19:00',
                        'ending_time': '22:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '08:30',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 5,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 6,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignations = []
        for i in range(4000):
            assignation1 = {
                'assignation': {
                    'person_id': i,
                    'starting_day': 2,
                    'starting_date': '2019-9-1',
                    'ending_date': '2025-9-30',
                    'workshift_id': 6,
                }
            }
            assignation1 = create_an_assignation(
                assignation1,
                workshift_db,
                day_off_assignations_db
            )

            assignation2 = {
                'assignation': {
                    'person_id': i,
                    'starting_day': None,
                    'starting_date': '2019-9-1',
                    'ending_date': '2025-9-30',
                    'workshift_id': 7
                }
            }
            assignation2 = create_an_assignation(
                assignation2,
                workshift_db,
                day_off_assignations_db
            )

            assignations.append(
                (assignation1, assignation2)
            )

        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            functions = []
            for params in assignations:
                f = executor.submit(
                    cycle_and_weekly_collision,
                    params[0],
                    params[1]
                )
                functions.append(f)

            responses = []
            for f in concurrent.futures.as_completed(functions):
                responses.append(f.result())

        end = time.time()
        total = end - start
        assert total < 30
"""
