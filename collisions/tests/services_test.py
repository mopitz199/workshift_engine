from datetime import datetime
from collisions.services import cycle_and_weekly_collision
from test_utils.utils import create_an_assignation


class TestServices(object):

    def test_cycle_and_weekly_collision1(self):

        assignation1 = {
            'assignation': {
                'starting_day': 2,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 30).date(),
            },
            'workshift': {
                'total_days': 5,
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
                'total_days': 7,
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

        assert cycle_and_weekly_collision(assignation1, assignation2)[0]

    def test_cycle_and_weekly_collision2(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2039, 9, 30).date(),
            },
            'workshift': {
                'total_days': 2,
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
                'total_days': 7,
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

        assert not cycle_and_weekly_collision(assignation1, assignation2)[0]

    def test_cycle_and_weekly_collision3(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_days': 2,
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
                'total_days': 7,
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

        assert not cycle_and_weekly_collision(assignation1, assignation2)[0]

    def test_cycle_and_weekly_collision4(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_days': 2,
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
                'total_days': 7,
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

        assert cycle_and_weekly_collision(assignation1, assignation2)[0]

    def test_cycle_and_weekly_collision5(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_days': 2,
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
                'total_days': 7,
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

        assert not cycle_and_weekly_collision(assignation1, assignation2)[0]

    def test_cycle_and_weekly_collision6(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 1).date(),
            },
            'workshift': {
                'total_days': 2,
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
                'total_days': 7,
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

        assert cycle_and_weekly_collision(assignation1, assignation2)[0]

    def test_cycle_and_weekly_collision7(self):

        assignation1 = {
            'assignation': {
                'starting_day': 0,
                'starting_date': datetime(2019, 9, 1).date(),
                'ending_date': datetime(2019, 9, 28).date(),
            },
            'workshift': {
                'total_days': 2,
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
                'total_days': 7,
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

        has_collisions, detail = cycle_and_weekly_collision(
            assignation1,
            assignation2,
            detail=True)

        assert has_collisions
