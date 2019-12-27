from datetime import datetime
from collisions.services import (
    cycle_and_weekly_collision,
    cycle_and_manually_collision,
    weekly_and_manually_collision
)
from test_utils.utils import create_an_assignation


class TestCycleAndWeeklyCollision():

    def test_cycle_and_weekly_collision1(self):

        assignation1 = {
            'assignation': {
                'starting_day': 2,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 30).date(),
            },
            'workshift': {
                'total_workshift_days': 5,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    }

                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 30).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
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
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert has_collision and not detail

    def test_cycle_and_weekly_collision2(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2039, 9, 30).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '03:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '04:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '03:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '04:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 30).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
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
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert not has_collision and not detail

    def test_cycle_and_weekly_collision3(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '06:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '14:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
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
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert not has_collision and not detail

    def test_cycle_and_weekly_collision4(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '06:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '14:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 6,
                        'starting_time': datetime.strptime(
                            '03:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert has_collision and not detail

    def test_cycle_and_weekly_collision5(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '06:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '14:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': None,
                        'ending_time': None
                    },
                    {
                        'day_number': 6,
                        'starting_time': datetime.strptime(
                            '03:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:59', '%H:%M').time()
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert not has_collision and not detail

    def test_cycle_and_weekly_collision6(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '06:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '14:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '22:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2)

        assert has_collision and not detail

    def test_cycle_and_weekly_collision7(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '06:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '14:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '22:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

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

        assert has_collision and detail == detail_expected

    def test_cycle_and_weekly_collision8(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '17:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '04:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '15:59', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '16:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '23:59', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '00:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:59', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '15:59', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '16:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '23:59', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '00:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:59', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

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

        assert has_collision and detail == detail_expected

    def test_cycle_and_weekly_collision9(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '06:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '14:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 8, 31).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '22:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

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

        assert has_collision and detail == detail_expected

    def test_cycle_and_weekly_collision10(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '22:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '04:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '10:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '22:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

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

        assert has_collision and detail == detail_expected

    def test_cycle_and_weekly_collision11(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '22:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '22:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '10:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '11:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '14:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '22:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': None,
                        'ending_time': None
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

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

        assert has_collision and detail == detail_expected

    def test_cycle_and_weekly_collision12(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 2).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '16:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '22:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '10:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '11:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '14:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '22:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': datetime.strptime(
                            '22:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

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

        assert has_collision and detail == detail_expected

    def test_cycle_and_weekly_collision13(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 15).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '16:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 15).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    }
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {'0': {}, '1': {}}

        assert not has_collision and detail == detail_expected

    def test_cycle_and_weekly_collision14(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '16:00', '%H:%M').time()
                    }
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '17:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:01', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 5,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'day_number': 6,
                        'starting_time': datetime.strptime(
                            '17:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {
            '0': {
                '2': [datetime(2019, 9, 11).date()]
            },
            '1': {}
        }

        assert has_collision and detail == detail_expected


class TestCycleAndManuallyCollision():

    def test_cycle_and_manually_collision1(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 1).date(),
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {
            '2019-09-01': [0]
        }
        assert has_collision and detail == detail_expected

    def test_cycle_and_manually_collision2(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 1).date(),
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {}

        assert not has_collision and detail == detail_expected

    def test_cycle_and_manually_collision3(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 1).date(),
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '13:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {'2019-09-01': [1]}

        assert has_collision and detail == detail_expected

    def test_cycle_and_manually_collision4(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 1).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '13:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {'2019-09-01': [0, 1]}

        assert has_collision and detail == detail_expected

    def test_cycle_and_manually_collision5(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 1, 1).date(),
                        'starting_time': datetime.strptime(
                            '18:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {}

        assert not has_collision and detail == detail_expected

    def test_cycle_and_manually_collision6(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 1).date(),
                        'starting_time': datetime.strptime(
                            '18:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 2).date(),
                        'starting_time': datetime.strptime(
                            '20:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 3).date(),
                        'starting_time': datetime.strptime(
                            '18:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 4).date(),
                        'starting_time': datetime.strptime(
                            '20:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 5).date(),
                        'starting_time': datetime.strptime(
                            '18:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 6).date(),
                        'starting_time': datetime.strptime(
                            '20:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 7).date(),
                        'starting_time': datetime.strptime(
                            '18:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 8).date(),
                        'starting_time': datetime.strptime(
                            '20:01', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {}

        assert not has_collision and detail == detail_expected

    def test_cycle_and_manually_collision7(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 1).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 2).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 3).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 4).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 5).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 6).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 7).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:59', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 8).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:59', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

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

        assert has_collision and detail == detail_expected

    def test_cycle_and_manually_collision8(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '20:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 1).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '13:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 2).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 3).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '13:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 4).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 5).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '13:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 6).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 7).date(),
                        'starting_time': datetime.strptime(
                            '18:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '13:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 8).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

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

        assert has_collision and detail == detail_expected

    def test_cycle_and_manually_collision9(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 8).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 9).date(),
                'ending_date': datetime(2019, 9, 9).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 9).date(),
                        'starting_time': datetime.strptime(
                            '06:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {'2019-09-09': [1]}
        assert has_collision and detail == detail_expected

    def test_cycle_and_manually_collision10(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 8).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 10).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 10).date(),
                        'starting_time': datetime.strptime(
                            '06:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {}
        assert not has_collision and detail == detail_expected

    def test_cycle_and_manually_collision11(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 8).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 8, 31).date(),
                'ending_date': datetime(2019, 8, 31).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 8, 31).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {'2019-08-31': [0]}
        assert has_collision and detail == detail_expected

    def test_cycle_and_manually_collision12(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 8).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 8, 30).date(),
                'ending_date': datetime(2019, 8, 30).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 8, 30).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {}
        assert not has_collision and detail == detail_expected

    def test_cycle_and_manually_collision13(self):

        assignation1 = {
            'assignation': {
                'starting_day': 1,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 8).date(),
            },
            'workshift': {
                'total_workshift_days': 2,
                'workshift_type': 'cyclic',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '07:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '18:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '13:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '06:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 8, 30).date(),
                'ending_date': datetime(2019, 9, 10).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 8, 30).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 8, 31).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 2).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '08:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 5).date(),
                        'starting_time': datetime.strptime(
                            '11:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '17:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 6).date(),
                        'starting_time': datetime.strptime(
                            '05:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '12:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 8).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                    {
                        'date': datetime(2019, 9, 10).date(),
                        'starting_time': datetime.strptime(
                            '20:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '07:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = cycle_and_manually_collision(
            assignation1,
            assignation2,
            detail=True)

        detail_expected = {
            '2019-08-31': [0],
            '2019-09-02': [1, 0],
            '2019-09-05': [0],
            '2019-09-08': [1]
        }
        assert has_collision and detail == detail_expected


class TestWeeklyAndManuallyCollision():

    def test_weekly_and_manually_collision1(self):

        assignation1 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 30).date(),
            },
            'workshift': {
                'total_workshift_days': 7,
                'workshift_type': 'weekly',
                'days': [
                    {
                        'day_number': 0,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 1,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 2,
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    {
                        'day_number': 3,
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    {
                        'day_number': 4,
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
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
        }
        assignation1 = create_an_assignation(assignation1)

        assignation2 = {
            'assignation': {
                'starting_day': None,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 11).date(),
            },
            'workshift': {
                'workshift_type': 'manually',
                'days': [
                    {
                        'date': datetime(2019, 9, 1).date(),
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                ]
            }
        }
        assignation2 = create_an_assignation(assignation2)

        has_collision, detail = weekly_and_manually_collision(
            assignation1,
            assignation2)

        assert has_collision and not detail
