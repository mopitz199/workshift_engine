from datetime import datetime

from database.assignation_db import AssignationDB
from mappers.range_mapper import Range
from operators.differences_operator import DifferencesOperator
from test_utils.utils import create_an_assignation


class TestDifferencesOperator(object):
    
    """
    def test_process_differences1(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 16).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        assignations = [assign1]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 17).date(),
                'ending_date': datetime(2019, 2, 20).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 2
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignation_db.assignate(assign2)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected = Range(
            datetime(2019, 2, 17).date(),
            datetime(2019, 2, 20).date())

        assert resp['1'] == [expected]
    """

    def test_process_differences2(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 16).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        assignations = [assign1]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 20).date(),
                'ending_date': datetime(2019, 2, 22).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 5
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        fake_assign = create_an_assignation(data)

        assignation_db.unassign(fake_assign)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected1 = Range(
            datetime(2019, 2, 20).date(),
            datetime(2019, 2, 22).date())

        expected2 = Range(
            datetime(2019, 2, 23).date(),
            datetime(2019, 2, 25).date())

        assert resp['1'] == [expected1, expected2]
