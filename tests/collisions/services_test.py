from datetime import datetime


from collisions.services import (
    cycle_and_weekly_collision,
    cycle_and_manually_collision,
    weekly_and_manually_collision,
    cycle_and_cycle_collision
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


class TestCycleAndWeeklyCollision():

    def test_cycle_and_weekly_collision1(self):

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

        assignation1 = {
            'assignation': {
                'starting_day': 2,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
                'workshift_id': 7
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        expected = {
            '0': {
                '3': [datetime(2019, 9, 5).date()],
                '1': [datetime(2019, 9, 10).date()],
                '4': [datetime(2019, 9, 20).date()],
                '2': [datetime(2019, 9, 25).date()],
                '0': [datetime(2019, 9, 30).date()]
            },
            '1': {
                '4': [datetime(2019, 9, 6).date()],
                '2': [datetime(2019, 9, 11).date()],
                '0': [datetime(2019, 9, 16).date()],
                '3': [datetime(2019, 9, 26).date()]
            },
            '3': {
                '1': [datetime(2019, 9, 3).date()],
                '4': [datetime(2019, 9, 13).date()],
                '2': [datetime(2019, 9, 18).date()],
                '0': [datetime(2019, 9, 23).date()]
            },
            '4': {
                '2': [datetime(2019, 9, 4).date()],
                '0': [datetime(2019, 9, 9).date()],
                '3': [datetime(2019, 9, 19).date()],
                '1': [datetime(2019, 9, 24).date()]
            }
        }
        assert detail == expected

    def test_cycle_and_weekly_collision2(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '03:00',
                        'ending_time': '04:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '03:00',
                        'ending_time': '04:00'
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

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2039-9-30',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert detail is None

    def test_cycle_and_weekly_collision3(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '06:00',
                        'ending_time': '14:00'
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

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'workshift_id': 7,
            },
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert detail is None

    def test_cycle_and_weekly_collision4(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '06:00',
                        'ending_time': '14:00'
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
                        'starting_time': '03:00',
                        'ending_time': '08:00'
                    }
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)
        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        expected = {
            '0': {
                    '6': [datetime(2019, 9, 1).date()]
                }
            }
        assert expected == detail

    def test_cycle_and_weekly_collision5(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '06:00',
                        'ending_time': '14:00'
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
                        'starting_time': '03:00',
                        'ending_time': '07:59'
                    }
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert detail is None

    def test_cycle_and_weekly_collision6(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '06:00',
                        'ending_time': '14:00'
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
                        'starting_time': '22:30',
                        'ending_time': '08:00'
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

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'workshift_id': 6
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'workshift_id': 7
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)
        assert detail is None

    def test_cycle_and_weekly_collision7(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '06:00',
                        'ending_time': '14:00'
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
                        'starting_time': '18:00',
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
                        'starting_time': '22:30',
                        'ending_time': '08:00'
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

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-10',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-10',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '0': {
                '3': [datetime(2019, 9, 5).date()],
                '0': [datetime(2019, 9, 9).date()]
            },
            '1': {
                '0': [datetime(2019, 9, 2).date()],
                '4': [datetime(2019, 9, 6).date()],
                '5': [datetime(2019, 9, 8).date()]
            }
        }

        assert detail == detail_expected

    def test_cycle_and_weekly_collision8(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '17:00',
                        'ending_time': '22:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '20:00',
                        'ending_time': '04:00'
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
                        'ending_time': '15:59'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '16:00',
                        'ending_time': '23:59'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '00:00',
                        'ending_time': '07:59'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '15:59'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '16:00',
                        'ending_time': '23:59'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '00:00',
                        'ending_time': '07:59'
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

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-10',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-10',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '0': {
                '1': [datetime(2019, 9, 3).date()]
            },
            '1': {
                '4': [datetime(2019, 9, 6).date()],
                '5': [datetime(2019, 9, 6).date()],
                '1': [datetime(2019, 9, 10).date()]
            }
        }

        assert detail == detail_expected

    def test_cycle_and_weekly_collision9(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '06:00',
                        'ending_time': '14:00'
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
                        'starting_time': '18:00',
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
                        'starting_time': '22:30',
                        'ending_time': '08:00'
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

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-10',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-8-31',
                'ending_date': '2019-9-10',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '0': {
                '5': [datetime(2019, 9, 1).date()],
                '3': [datetime(2019, 9, 5).date()],
                '0': [datetime(2019, 9, 9).date()]
            },
            '1': {
                '0': [datetime(2019, 9, 2).date()],
                '4': [datetime(2019, 9, 6).date()],
                '5': [datetime(2019, 9, 8).date()]
            }
        }

        assert detail == detail_expected

    def test_cycle_and_weekly_collision10(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '22:00',
                        'ending_time': '08:00'
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
                        'starting_time': '18:00',
                        'ending_time': '19:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '04:00',
                        'ending_time': '10:00'
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
                        'starting_time': '22:30',
                        'ending_time': '08:00'
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

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-10',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '0': {
                '3': [datetime(2019, 9, 5).date()],
                '0': [datetime(2019, 9, 9).date()]
            },
            '1': {
                '3': [datetime(2019, 9, 4).date()],
                '0': [datetime(2019, 9, 8).date()],
                '2': [datetime(2019, 9, 10).date()]
            }
        }

        assert detail == detail_expected

    def test_cycle_and_weekly_collision11(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '22:00',
                        'ending_time': '08:00'
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
                        'starting_time': '22:00',
                        'ending_time': '10:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '11:00',
                        'ending_time': '14:00'
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
                        'starting_time': '22:30',
                        'ending_time': '08:00'
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

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-10',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '0': {
                '3': [datetime(2019, 9, 5).date()],
                '0': [datetime(2019, 9, 9).date()],
                '1': [datetime(2019, 9, 11).date()]
            },
            '1': {
                '3': [datetime(2019, 9, 4).date()],
                '0': [datetime(2019, 9, 8).date()],
                '1': [datetime(2019, 9, 10).date()]
            }
        }

        assert detail == detail_expected

    def test_cycle_and_weekly_collision12(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '07:00',
                        'ending_time': '16:00'
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
                        'starting_time': '22:00',
                        'ending_time': '10:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '11:00',
                        'ending_time': '14:00'
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
                        'starting_time': '22:30',
                        'ending_time': '08:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '22:30',
                        'ending_time': '08:00'
                    }
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-2',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '0': {
                '6': [datetime(2019, 9, 2).date()],
                '0': [datetime(2019, 9, 2).date()],
                '1': [datetime(2019, 9, 4).date()],
                '2': [datetime(2019, 9, 4).date()],
                '4': [datetime(2019, 9, 6).date()],
                '5': [datetime(2019, 9, 8).date()]
            },
            '1': {
                '3': [datetime(2019, 9, 5).date()],
                '6': [datetime(2019, 9, 9).date()],
                '0': [datetime(2019, 9, 9).date()],
                '1': [datetime(2019, 9, 11).date()],
                '2': [datetime(2019, 9, 11).date()]
            }
        }

        assert detail == detail_expected

    def test_cycle_and_weekly_collision13(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '07:00',
                        'ending_time': '16:00'
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
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    }
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-15',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-15',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_weekly_collision14(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '17:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '07:00',
                        'ending_time': '16:00'
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
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '17:00',
                        'ending_time': '17:01'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '17:01',
                        'ending_time': '06:59'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2
        )
        import pdb; pdb.set_trace()
        detail_expected = {
            '0': {
                '2': [datetime(2019, 9, 11).date()]
            }
        }

        assert detail == detail_expected


class TestCycleAndManuallyCollision():

    def test_cycle_and_manually_collision1(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '2019-09-01': [0]
        }
        assert detail == detail_expected

    def test_cycle_and_manually_collision2(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '19:00',
                        'ending_time': '20:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_manually_collision3(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '19:00',
                        'ending_time': '13:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {'2019-09-01': [1]}

        assert detail == detail_expected

    def test_cycle_and_manually_collision4(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {'2019-09-01': [0, 1]}

        assert detail == detail_expected

    def test_cycle_and_manually_collision5(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-1-1',
                        'starting_time': '18:01',
                        'ending_time': '12:59'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_manually_collision6(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:01',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-2',
                        'starting_time': '20:01',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-3',
                        'starting_time': '18:01',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-4',
                        'starting_time': '20:01',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-5',
                        'starting_time': '18:01',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-6',
                        'starting_time': '20:01',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-7',
                        'starting_time': '18:01',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-8',
                        'starting_time': '20:01',
                        'ending_time': '06:59'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )
        assert detail is None

    def test_cycle_and_manually_collision7(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-2',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-3',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-4',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-5',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-6',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-7',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-8',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '2019-09-01': [0],
            '2019-09-02': [1],
            '2019-09-03': [0],
            '2019-09-04': [1],
            '2019-09-05': [0],
            '2019-09-06': [1],
            '2019-09-07': [0],
            '2019-09-08': [1]
        }

        assert detail == detail_expected

    def test_cycle_and_manually_collision8(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                    {
                        'date': '2019-9-2',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-9-3',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                    {
                        'date': '2019-9-4',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-9-5',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                    {
                        'date': '2019-9-6',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-9-7',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                    {
                        'date': '2019-9-8',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '2019-09-01': [0, 1],
            '2019-09-02': [1, 0],
            '2019-09-03': [0, 1],
            '2019-09-04': [1, 0],
            '2019-09-05': [0, 1],
            '2019-09-06': [1, 0],
            '2019-09-07': [0, 1],
            '2019-09-08': [1, 0]
        }

        assert detail == detail_expected

    def test_cycle_and_manually_collision9(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '06:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-9',
                        'starting_time': '06:00',
                        'ending_time': '07:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-9',
                'ending_date': '2019-9-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {'2019-09-09': [1]}
        assert detail == detail_expected

    def test_cycle_and_manually_collision10(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '06:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-10',
                        'starting_time': '06:00',
                        'ending_time': '07:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-9-10',
                'ending_date': '2019-9-10',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_manually_collision11(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '06:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-8-31',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-8-31',
                'ending_date': '2019-8-31',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {'2019-08-31': [0]}
        assert detail == detail_expected

    def test_cycle_and_manually_collision12(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '06:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-8-30',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-8-30',
                'ending_date': '2019-8-30',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_manually_collision13(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '06:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-8-30',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-8-31',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-9-2',
                        'starting_time': '20:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-9-5',
                        'starting_time': '11:30',
                        'ending_time': '17:00'
                    },
                    {
                        'date': '2019-9-6',
                        'starting_time': '05:00',
                        'ending_time': '12:00'
                    },
                    {
                        'date': '2019-9-8',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-9-10',
                        'starting_time': '20:00',
                        'ending_time': '07:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-8-30',
                'ending_date': '2019-9-10',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)
        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '2019-08-31': [0],
            '2019-09-02': [1, 0],
            '2019-09-05': [0],
            '2019-09-08': [1]
        }
        assert detail == detail_expected


class TestWeeklyAndManuallyCollision():

    def test_weekly_and_manually_collision1(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'date': '2019-12-4',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'date': '2019-12-6',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'date': '2019-12-8',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-02': [0],
            '2019-12-04': [2],
            '2019-12-06': [4],
            '2019-12-08': [6]
        }
        assert detail == expected_detail

    def test_weekly_and_manually_collision2(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-4',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-6',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'date': '2019-12-8',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-02': [1],
            '2019-12-04': [3],
            '2019-12-06': [4],
            '2019-12-08': [6]
        }

        assert detail == expected_detail

    def test_weekly_and_manually_collision3(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-1',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-4',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-6',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'date': '2019-12-9',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-01': [0],
            '2019-12-04': [3],
            '2019-12-06': [4],
            '2019-12-09': [6],
        }
        assert detail == expected_detail

    def test_weekly_and_manually_collision4(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '22:00',
                        'ending_time': '07:59'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-1',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-4',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-6',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'date': '2019-12-9',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-01': [0],
            '2019-12-04': [3],
            '2019-12-06': [4],
        }

        assert detail == expected_detail

    def test_weekly_and_manually_collision5(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '17:59'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '18:01',
                        'ending_time': '22:00'
                    },
                    {
                        'date': '2019-12-3',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-5',
                        'starting_time': '18:01',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-12-7',
                        'starting_time': '17:00',
                        'ending_time': '08:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-03': [2],
            '2019-12-07': [5, 6],
        }

        assert detail == expected_detail

    def test_weekly_and_manually_collision6(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '17:59'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '18:01',
                        'ending_time': '22:00'
                    },
                    {
                        'date': '2019-12-3',
                        'starting_time': '22:00',
                        'ending_time': '07:59'
                    },
                    {
                        'date': '2019-12-5',
                        'starting_time': '18:01',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-12-7',
                        'starting_time': '18:01',
                        'ending_time': '07:59'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_weekly_and_manually_collision7(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '17:59'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '18:01',
                        'ending_time': '22:00'
                    },
                    {
                        'date': '2019-12-3',
                        'starting_time': '22:00',
                        'ending_time': '07:59'
                    },
                    {
                        'date': '2019-12-5',
                        'starting_time': '18:01',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-12-7',
                        'starting_time': '18:01',
                        'ending_time': '07:59'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None


class TestWeeklyAndManuallyCollisionDayOffs():

    def test_weekly_and_manually_collision_day_off1(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-12-4',
                'ending_date': '2019-12-4',
                'starting_time': '07:00',
                'ending_time': '09:00'
            }
        ]
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
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '17:59'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '18:01',
                        'ending_time': '22:00'
                    },
                    {
                        'date': '2019-12-3',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-5',
                        'starting_time': '18:01',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-12-7',
                        'starting_time': '17:00',
                        'ending_time': '08:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-07': [5, 6],
        }

        assert detail == expected_detail

    def test_weekly_and_manually_collision_day_off2(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-12-4',
                'ending_date': '2019-12-4',
                'starting_time': '07:00',
                'ending_time': '09:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-12-7',
                'ending_date': '2019-12-7',
                'starting_time': '17:00',
                'ending_time': '18:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-12-8',
                'ending_date': '2019-12-8',
                'starting_time': '08:00',
                'ending_time': '08:00'
            }
        ]
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
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '17:59'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '18:01',
                        'ending_time': '22:00'
                    },
                    {
                        'date': '2019-12-3',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-5',
                        'starting_time': '18:01',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-12-7',
                        'starting_time': '17:00',
                        'ending_time': '08:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_weekly_and_manually_collision_day_off3(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-12-4',
                'ending_date': '2019-12-4',
                'starting_time': '07:00',
                'ending_time': '09:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-12-7',
                'ending_date': '2019-12-7',
                'starting_time': '17:00',
                'ending_time': '18:00'
            }
        ]
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
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '17:59'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '18:01',
                        'ending_time': '22:00'
                    },
                    {
                        'date': '2019-12-3',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-5',
                        'starting_time': '18:01',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-12-7',
                        'starting_time': '17:00',
                        'ending_time': '08:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-07': [6],
        }
        assert detail == expected_detail

    def test_weekly_and_manually_collision_day_off4(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-12-4',
                'ending_date': '2019-12-4',
                'starting_time': '07:00',
                'ending_time': '09:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-12-8',
                'ending_date': '2019-12-8',
                'starting_time': '08:00',
                'ending_time': '08:00'
            }
        ]
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
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '17:59'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '18:01',
                        'ending_time': '22:00'
                    },
                    {
                        'date': '2019-12-3',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-5',
                        'starting_time': '18:01',
                        'ending_time': '07:00'
                    },
                    {
                        'date': '2019-12-7',
                        'starting_time': '17:00',
                        'ending_time': '08:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-1',
                'ending_date': '2019-12-9',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-07': [5],
        }
        assert detail == expected_detail

    def test_weekly_and_manually_collision_day_off5(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-12-3',
                'ending_date': '2019-12-3',
                'starting_time': '08:00',
                'ending_time': '08:00'
            }
        ]
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
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-4',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-6',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'date': '2019-12-8',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-04': [3],
            '2019-12-06': [4],
            '2019-12-08': [6]
        }

        assert detail == expected_detail

    def test_weekly_and_manually_collision_day_off6(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-12-3',
                'ending_date': '2019-12-3',
                'starting_time': '08:00',
                'ending_time': '08:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-12-6',
                'ending_date': '2019-12-6',
                'starting_time': '08:00',
                'ending_time': '18:00'
            }
        ]
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
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 2,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 3,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 4,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 5,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 6,
                        'starting_time': '08:00',
                        'ending_time': '18:00'
                    }
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-12-2',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-4',
                        'starting_time': '22:00',
                        'ending_time': '08:00'
                    },
                    {
                        'date': '2019-12-6',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                    {
                        'date': '2019-12-8',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-12-2',
                'ending_date': '2019-12-8',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = weekly_and_manually_collision(
            assignation1,
            assignation2
        )

        expected_detail = {
            '2019-12-04': [3],
            '2019-12-08': [6]
        }

        assert detail == expected_detail


class TestCycleAndManuallyCollisionDayOffs():

    def test_cycle_and_manually_collision1_day_off1(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'starting_time': '08:00',
                'ending_time': '18:00'
            }
        ]
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
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '08:00',
                        'ending_time': '19:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_manually_collision1_day_off2(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-2',
                'ending_date': '2019-9-2',
                'starting_time': '13:00',
                'ending_time': '13:00'
            }
        ]
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
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '19:00',
                        'ending_time': '13:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_manually_collision1_day_off3(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'starting_time': '18:00',
                'ending_time': '18:00'
            }
        ]
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
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {'2019-09-01': [1]}
        assert detail == detail_expected

    def test_cycle_and_manually_collision1_day_off4(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-2',
                'ending_date': '2019-9-2',
                'starting_time': '13:00',
                'ending_time': '13:00'
            }
        ]
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
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {'2019-09-01': [0]}
        assert detail == detail_expected

    def test_cycle_and_manually_collision1_day_off5(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'starting_time': '18:00',
                'ending_time': '18:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-9-2',
                'ending_date': '2019-9-2',
                'starting_time': '13:00',
                'ending_time': '13:00'
            }
        ]
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
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_manually_collision1_day_off6(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-5',
                'starting_time': '18:00',
                'ending_time': '18:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-5',
                'starting_time': '13:00',
                'ending_time': '13:00'
            }
        ]
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
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '13:00'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        assert detail is None

    def test_cycle_and_manually_collision1_day_off7(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'starting_time': '18:00',
                'ending_time': '18:00'
            }
        ]
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
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-2',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-3',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-4',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-5',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-6',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-7',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-8',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '2019-09-02': [1],
            '2019-09-03': [0],
            '2019-09-04': [1],
            '2019-09-05': [0],
            '2019-09-06': [1],
            '2019-09-07': [0],
            '2019-09-08': [1]
        }

        assert detail == detail_expected

    def test_cycle_and_manually_collision1_day_off8(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-1',
                'starting_time': '18:00',
                'ending_time': '18:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-9-6',
                'ending_date': '2019-9-6',
                'starting_time': '20:00',
                'ending_time': '20:00'
            }
        ]
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
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '07:00',
                        'ending_time': '18:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '13:00',
                        'ending_time': '20:00'
                    },
                ]
            },
            {
                'id': 7,
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': '2019-9-1',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-2',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-3',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-4',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-5',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-6',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                    {
                        'date': '2019-9-7',
                        'starting_time': '18:00',
                        'ending_time': '12:59'
                    },
                    {
                        'date': '2019-9-8',
                        'starting_time': '20:00',
                        'ending_time': '06:59'
                    },
                ]
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 1,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-11',
                'workshift_id': 7,
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_manually_collision(
            assignation1,
            assignation2
        )

        detail_expected = {
            '2019-09-02': [1],
            '2019-09-03': [0],
            '2019-09-04': [1],
            '2019-09-05': [0],
            '2019-09-07': [0],
            '2019-09-08': [1]
        }

        assert detail == detail_expected


class TestCycleAndWeeklyCollisionDayOffs():

    def test_cycle_and_weekly_collision_day_off1(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-4',
                'ending_date': '2019-9-4',
                'starting_time': '19:00',
                'ending_time': '19:00'
            }
        ]
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

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 2,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
                'workshift_id': 7
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        expected = {
            '0': {
                '3': [datetime(2019, 9, 5).date()],
                '1': [datetime(2019, 9, 10).date()],
                '4': [datetime(2019, 9, 20).date()],
                '2': [datetime(2019, 9, 25).date()],
                '0': [datetime(2019, 9, 30).date()]
            },
            '1': {
                '4': [datetime(2019, 9, 6).date()],
                '2': [datetime(2019, 9, 11).date()],
                '0': [datetime(2019, 9, 16).date()],
                '3': [datetime(2019, 9, 26).date()]
            },
            '3': {
                '1': [datetime(2019, 9, 3).date()],
                '4': [datetime(2019, 9, 13).date()],
                '2': [datetime(2019, 9, 18).date()],
                '0': [datetime(2019, 9, 23).date()]
            },
            '4': {
                '0': [datetime(2019, 9, 9).date()],
                '3': [datetime(2019, 9, 19).date()],
                '1': [datetime(2019, 9, 24).date()]
            }
        }

        assert detail == expected

    def test_cycle_and_weekly_collision_day_off2(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-4',
                'ending_date': '2019-9-4',
                'starting_time': '19:00',
                'ending_time': '19:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-9-10',
                'ending_date': '2019-9-10',
                'starting_time': '10:00',
                'ending_time': '11:00'
            }
        ]
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

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 2,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
                'workshift_id': 7
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)
        expected = {
            '0': {
                '3': [datetime(2019, 9, 5).date()],
                '1': [datetime(2019, 9, 10).date()],
                '4': [datetime(2019, 9, 20).date()],
                '2': [datetime(2019, 9, 25).date()],
                '0': [datetime(2019, 9, 30).date()]
            },
            '1': {
                '4': [datetime(2019, 9, 6).date()],
                '2': [datetime(2019, 9, 11).date()],
                '0': [datetime(2019, 9, 16).date()],
                '3': [datetime(2019, 9, 26).date()]
            },
            '3': {
                '1': [datetime(2019, 9, 3).date()],
                '4': [datetime(2019, 9, 13).date()],
                '2': [datetime(2019, 9, 18).date()],
                '0': [datetime(2019, 9, 23).date()]
            },
            '4': {
                '0': [datetime(2019, 9, 9).date()],
                '3': [datetime(2019, 9, 19).date()],
                '1': [datetime(2019, 9, 24).date()]
            }
        }

        assert detail == expected

    def test_cycle_and_weekly_collision_day_off3(self):

        day_off_assignations_data = [
            {
                'person_id': 1,
                'starting_date': '2019-9-4',
                'ending_date': '2019-9-4',
                'starting_time': '19:00',
                'ending_time': '19:00'
            },
            {
                'person_id': 1,
                'starting_date': '2019-9-10',
                'ending_date': '2019-9-10',
                'starting_time': '08:00',
                'ending_time': '19:00'
            }
        ]
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

        assignation1 = {
            'assignation': {
                'person_id': 1,
                'starting_day': 2,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
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
                'person_id': 1,
                'starting_day': None,
                'starting_date': '2019-9-1',
                'ending_date': '2019-9-30',
                'workshift_id': 7
            }
        }
        assignation2 = create_an_assignation(
            assignation2,
            workshift_db,
            day_off_assignations_db
        )

        detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        expected = {
            '0': {
                '3': [datetime(2019, 9, 5).date()],
                '4': [datetime(2019, 9, 20).date()],
                '2': [datetime(2019, 9, 25).date()],
                '0': [datetime(2019, 9, 30).date()]
            },
            '1': {
                '4': [datetime(2019, 9, 6).date()],
                '2': [datetime(2019, 9, 11).date()],
                '0': [datetime(2019, 9, 16).date()],
                '3': [datetime(2019, 9, 26).date()]
            },
            '3': {
                '1': [datetime(2019, 9, 3).date()],
                '4': [datetime(2019, 9, 13).date()],
                '2': [datetime(2019, 9, 18).date()],
                '0': [datetime(2019, 9, 23).date()]
            },
            '4': {
                '0': [datetime(2019, 9, 9).date()],
                '3': [datetime(2019, 9, 19).date()],
                '1': [datetime(2019, 9, 24).date()]
            }
        }
        assert detail == expected

"""
class TestCycleAndCycleCollision():

    def test_cycle_and_cycle_collision1(self):
        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 2,
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
                    }
                ]
            },
            {
                'id': 7,
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': '15:00',
                        'ending_time': '23:00'
                    },
                    {
                        'day_number': 1,
                        'starting_time': '15:00',
                        'ending_time': '23:00'
                    }
                ]
            },
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2020-2-1',
                'ending_date': '2020-2-10',
                'workshift_id': 6,
            }
        }
        assignation1 = create_an_assignation(assignation1, workshift_db)

        assignation2 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': '2020-2-1',
                'ending_date': '2020-2-10',
                'workshift_id': 7
            }
        }
        assignation2 = create_an_assignation(assignation2, workshift_db)

        detail = cycle_and_cycle_collision(
            assignation1,
            assignation2)

        expected = {
            '0': {
                '2': [datetime(2019, 9, 4).date()],
                '0': [datetime(2019, 9, 9).date()],
                '3': [datetime(2019, 9, 19).date()],
                '1': [datetime(2019, 9, 24).date()]
            },
            '1': {
                '3': [datetime(2019, 9, 5).date()],
                '1': [datetime(2019, 9, 10).date()],
                '4': [datetime(2019, 9, 20).date()],
                '2': [datetime(2019, 9, 25).date()],
                '0': [datetime(2019, 9, 30).date()]
            },
            '3': {
                '0': [datetime(2019, 9, 2).date()],
                '3': [datetime(2019, 9, 12).date()],
                '1': [datetime(2019, 9, 17).date()],
                '4': [datetime(2019, 9, 27).date()]
            },
            '4': {
                '1': [datetime(2019, 9, 3).date()],
                '4': [datetime(2019, 9, 13).date()],
                '2': [datetime(2019, 9, 18).date()],
                '0': [datetime(2019, 9, 23).date()]
            }
        }
        assert detail == expected        
"""