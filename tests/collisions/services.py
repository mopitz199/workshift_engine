from datetime import datetime
from collisions.services import check


class TestServices(object):

    def test1(self):

        assignation1 = {
            'starting_day': None,
            'starting_date': datetime(2019, 9, 1).date(),
            'ending_date': datetime(2019, 9, 30).date(),
            'workshift': {
                'total_days': 7,
                'days': {
                    'monday': {
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    'tuesday': {
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    'wednesday': {
                        'starting_time': datetime.strptime(
                            '19:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '22:00', '%H:%M').time()
                    },
                    'thursday': {
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    'friday': {
                        'starting_time': datetime.strptime(
                            '08:30', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    'saturday': {
                        'starting_time': None,
                        'ending_time': None
                    },
                    'sunday': {
                        'starting_time': None,
                        'ending_time': None
                    }
                }
            }
        }

        assignation2 = {
            'starting_day': 2,
            'starting_date': datetime(2019, 9, 1).date(),
            'ending_date': datetime(2019, 9, 30).date(),
            'workshift': {
                'total_days': 5,
                'days': {
                    '0': {
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    '1': {
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    '2': {
                        'starting_time': None,
                        'ending_time': None
                    },
                    '3': {
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                    '4': {
                        'starting_time': datetime.strptime(
                            '08:00', '%H:%M').time(),
                        'ending_time': datetime.strptime(
                            '19:00', '%H:%M').time()
                    },
                }
            }
        }

        assert check(assignation1, assignation2)
