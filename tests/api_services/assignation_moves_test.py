from api_services.assignation_moves import AssignationMoves

"""
class TestAssignationMoves:

    def test_assignation_moves(self):
        data = {
            'workshifts': [
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
            ],
            'days_off': [
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
            ],
            'assignations_database': [
                {
                    'starting_date': '2019-2-14',
                    'ending_date': '2019-2-16',
                    'workshift_id': 6,
                    'person_id': 1,
                    'starting_day': 5
                },
                {
                    'starting_date': '2019-2-14',
                    'ending_date': '2019-2-16',
                    'workshift_id': 6,
                    'person_id': 1,
                    'starting_day': 5
                }
            ],
            'moves': {
                'assignations': [
                    {
                        'starting_date': '2019-2-13',
                        'ending_date': '2019-2-15',
                        'workshift_id': 6,
                        'person_id': 1,
                        'starting_day': 4
                    }
                ],
                'deallocates': [
                    {
                        'starting_date': '2019-2-13',
                        'ending_date': '2019-2-15',
                        'workshift_id': 6,
                        'person_id': 1,
                        'starting_day': 4
                    }
                ]
            }
        }
        assignation_moves = AssignationMoves(data)
        assignation_moves.run()
        import pdb; pdb.set_trace()
        assert True
"""
