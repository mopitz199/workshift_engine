from datetime import datetime

from assignation.operators.differences_operator import DifferencesOperator
from database.assignation_db import AssignationDB
from database.workshift_db import WorkShiftDB
from proxies.workshift_proxy import WorkShiftProxy
from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts,
)
from utils.range import Range


class TestDifferencesOperator(object):

    def test_process_differences1(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'id': 1,
                'starting_date': '2019-2-16',
                'ending_date': '2019-2-16',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        assignations = [assign1]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': '2019-2-17',
                'ending_date': '2019-2-20',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 2
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assignation_db.assignate(assign2)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected = Range(
            datetime(2019, 2, 17).date(),
            datetime(2019, 2, 20).date())

        assert resp['1'] == [expected]

    def test_process_differences2(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'id': 1,
                'starting_date': '2019-2-16',
                'ending_date': '2019-2-25',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        assignations = [assign1]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': '2019-2-20',
                'ending_date': '2019-2-22',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 5
            }
        }
        fake_assign = create_an_assignation(data, workshift_db)

        assignation_db.unassign(fake_assign)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected1 = Range(
            datetime(2019, 2, 20).date(),
            datetime(2019, 2, 22).date())

        assert resp['1'] == [expected1]

    def test_process_differences3(self):

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'id': 1,
                'starting_date': '2019-2-16',
                'ending_date': '2019-2-25',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        assignations = [assign1]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': '2019-2-19',
                'ending_date': '2019-2-22',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 4
            }
        }
        fake_assign = create_an_assignation(data, workshift_db)

        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': '2019-2-21',
                'ending_date': '2019-2-21',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

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

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'id': 1,
                'starting_date': '2019-2-10',
                'ending_date': '2019-2-15',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': '2019-2-17',
                'ending_date': '2019-2-23',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assignations = [assign1, assign2]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': '2019-2-13',
                'ending_date': '2019-2-15',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 4
            }
        }
        fake_assign = create_an_assignation(data, workshift_db)

        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': '2019-2-20',
                'ending_date': '2019-2-23',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 3
            }
        }
        fake_assign = create_an_assignation(data, workshift_db)

        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': '2019-2-14',
                'ending_date': '2019-2-16',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 5
            }
        }
        assign3 = create_an_assignation(data, workshift_db)

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

        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'id': 1,
                'starting_date': '2019-2-10',
                'ending_date': '2019-2-15',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        assignations = [assign1]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': '2019-2-13',
                'ending_date': '2019-2-15',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 4
            }
        }
        fake_assign = create_an_assignation(data, workshift_db)

        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': '2019-2-16',
                'ending_date': '2019-2-18',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 7
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assignation_db.assignate(assign2)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected = Range(
            datetime(2019, 2, 13).date(),
            datetime(2019, 2, 18).date())

        assert resp['1'] == [expected]

    def test_process_differences6(self):
        
        workshifts_data = [
            {
                'id': 6,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'id': 1,
                'starting_date': '2019-2-10',
                'ending_date': '2019-2-15',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': '2019-2-17',
                'ending_date': '2019-2-20',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 2
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assignations = [assign1, assign2]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': '2019-2-13',
                'ending_date': '2019-2-16',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign3 = create_an_assignation(data, workshift_db)
        assignation_db.assignate(assign3)

        data = {
            'assignation': {
                'starting_date': '2019-2-18',
                'ending_date': '2019-2-20',
                'workshift_id': 6,
                'person_id': 1,
                'starting_day': 3
            }
        }
        assign4 = create_an_assignation(data, workshift_db)
        assignation_db.assignate(assign4)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected1 = Range(
            datetime(2019, 2, 13).date(),
            datetime(2019, 2, 16).date())

        assert resp['1'] == [expected1]

    def test_process_differences7(self):

        workshifts_data = [
            {
                'id': 1,
                'total_workshift_days': 8
            },
            {
                'id': 2,
                'total_workshift_days': 4
            },
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'id': 1,
                'starting_date': '2019-2-10',
                'ending_date': '2019-2-15',
                'workshift_id': 1,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': '2019-2-13',
                'ending_date': '2019-2-20',
                'workshift_id': 2,
                'person_id': 1,
                'starting_day': 4
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assignations = [assign1, assign2]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': '2019-2-14',
                'ending_date': '2019-2-14',
                'workshift_id': 1,
                'person_id': 1,
                'starting_day': 3
            }
        }
        assign3 = create_an_assignation(data, workshift_db)
        assignation_db.assignate(assign3)

        data = {
            'assignation': {
                'starting_date': '2019-2-13',
                'ending_date': '2019-2-17',
                'workshift_id': 2,
                'person_id': 1,
                'starting_day': 3
            }
        }
        assign4 = create_an_assignation(data, workshift_db)
        assignation_db.assignate(assign4)

        data = {
            'assignation': {
                'starting_date': '2019-2-14',
                'ending_date': '2019-2-16',
                'workshift_id': 1,
                'person_id': 1,
                'starting_day': 5
            }
        }
        fake_assign = create_an_assignation(data, workshift_db)
        assignation_db.unassign(fake_assign)

        data = {
            'assignation': {
                'starting_date': '2019-2-13',
                'ending_date': '2019-2-13',
                'workshift_id': 2,
                'person_id': 1,
                'starting_day': 4
            }
        }
        fake_assign = create_an_assignation(data, workshift_db)
        assignation_db.unassign(fake_assign)

        differences_operator = DifferencesOperator(assignation_db)
        resp = differences_operator.process_differences()

        expected = Range(
            datetime(2019, 2, 13).date(),
            datetime(2019, 2, 17).date())

        assert resp['1'] == [expected]
