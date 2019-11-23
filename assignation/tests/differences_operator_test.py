from datetime import datetime

from database.assignation_db import AssignationDB
from utils.range import Range
from assignation.operators.differences_operator import DifferencesOperator
from test_utils.utils import create_an_assignation


class TestDifferencesOperator(object):

    def test_process_differences1(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 16).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
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
                'starting_day': 2
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

    def test_process_differences2(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 16).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
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
                'starting_day': 5
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

        assert resp['1'] == [expected1]

    def test_process_differences3(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 16).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        assignations = [assign1]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 19).date(),
                'ending_date': datetime(2019, 2, 22).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 4
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        fake_assign = create_an_assignation(data)

        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 21).date(),
                'ending_date': datetime(2019, 2, 21).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 6
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignation_db.assignate(assign2)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected1 = Range(
            datetime(2019, 2, 19).date(),
            datetime(2019, 2, 20).date())

        expected2 = Range(
            datetime(2019, 2, 22).date(),
            datetime(2019, 2, 22).date())

        assert resp['1'] == [expected1, expected2]

    def test_process_differences4(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 10).date(),
                'ending_date': datetime(2019, 2, 15).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 2, 17).date(),
                'ending_date': datetime(2019, 2, 23).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 8
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 15).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 4
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        fake_assign = create_an_assignation(data)

        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 20).date(),
                'ending_date': datetime(2019, 2, 23).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 3
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        fake_assign = create_an_assignation(data)

        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 14).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 5
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign3 = create_an_assignation(data)

        assignation_db.assignate(assign3)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected1 = Range(
            datetime(2019, 2, 13).date(),
            datetime(2019, 2, 13).date())

        expected2 = Range(
            datetime(2019, 2, 16).date(),
            datetime(2019, 2, 16).date())

        expected3 = Range(
            datetime(2019, 2, 20).date(),
            datetime(2019, 2, 23).date())

        assert resp['1'] == [expected1, expected2, expected3]

    def test_process_differences5(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 10).date(),
                'ending_date': datetime(2019, 2, 15).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        assignations = [assign1]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 15).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 4
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        fake_assign = create_an_assignation(data)

        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 16).date(),
                'ending_date': datetime(2019, 2, 18).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 7
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignation_db.assignate(assign2)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected = Range(
            datetime(2019, 2, 13).date(),
            datetime(2019, 2, 18).date())

        assert resp['1'] == [expected]

    def test_process_differences6(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 10).date(),
                'ending_date': datetime(2019, 2, 15).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 2, 17).date(),
                'ending_date': datetime(2019, 2, 20).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 2
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign3 = create_an_assignation(data)
        assignation_db.assignate(assign3)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 18).date(),
                'ending_date': datetime(2019, 2, 20).date(),
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 3
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign4 = create_an_assignation(data)
        assignation_db.assignate(assign4)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected1 = Range(
            datetime(2019, 2, 13).date(),
            datetime(2019, 2, 16).date())

        assert resp['1'] == [expected1]

    def test_process_differences7(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 10).date(),
                'ending_date': datetime(2019, 2, 15).date(),
                'workshift_id': 1,
                'person_id': 1,
                'starting_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 20).date(),
                'workshift_id': 2,
                'person_id': 1,
                'starting_day': 4
            },
            'workshift': {
                'total_workshift_days': 4,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 14).date(),
                'ending_date': datetime(2019, 2, 14).date(),
                'workshift_id': 1,
                'person_id': 1,
                'starting_day': 3
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign3 = create_an_assignation(data)
        assignation_db.assignate(assign3)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 17).date(),
                'workshift_id': 2,
                'person_id': 1,
                'starting_day': 3
            },
            'workshift': {
                'total_workshift_days': 4,
            }}
        assign4 = create_an_assignation(data)
        assignation_db.assignate(assign4)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 14).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 1,
                'person_id': 1,
                'starting_day': 5
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        fake_assign = create_an_assignation(data)
        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 13).date(),
                'workshift_id': 2,
                'person_id': 1,
                'starting_day': 4
            },
            'workshift': {
                'total_workshift_days': 4,
            }}
        fake_assign = create_an_assignation(data)
        assignation_db.unassign(fake_assign)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected = Range(
            datetime(2019, 2, 13).date(),
            datetime(2019, 2, 17).date())

        assert resp['1'] == [expected]
