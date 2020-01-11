import types
from datetime import datetime

from database.workshift_db import WorkShiftDB
from proxies.workshift_proxy import WorkShiftProxy
from proxies.assignation_proxy import AssignationProxy
from utils.range import Range
from assignation.operators.assignation_operator import AssignationOperator
from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts
)


class TestAssignationProxyAdd(object):
    """Class to test if the assignation proxy add method works well"""

    def test_add1(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-22',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-23',
                'ending_date': '2019-1-28',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assign1 += assign2

        range_obj = assign1.range_obj
        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
                assign1.ending_date == datetime(2019, 1, 28).date() and
                range_obj.starting_date == datetime(2019, 1, 1).date() and
                range_obj.ending_date == datetime(2019, 1, 28).date())

    def test_add2(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-22',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-24',
                'ending_date': '2019-1-28',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assign1 += assign2

        range_obj = assign1.range_obj
        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
                assign1.ending_date == datetime(2019, 1, 22).date() and
                range_obj.starting_date == datetime(2019, 1, 1).date() and
                range_obj.ending_date == datetime(2019, 1, 22).date())

    def test_add3(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-22',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-22',
                'ending_date': '2019-1-28',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 5
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assign1 += assign2

        range_obj = assign1.range_obj
        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
                assign1.ending_date == datetime(2019, 1, 22).date() and
                range_obj.starting_date == datetime(2019, 1, 1).date() and
                range_obj.ending_date == datetime(2019, 1, 22).date())

    def test_add4(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-15',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-5',
                'ending_date': '2019-1-28',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assign1 += assign2

        range_obj = assign1.range_obj
        assert (assign1.starting_date == datetime(2019, 1, 5).date() and
                assign1.ending_date == datetime(2019, 1, 28).date() and
                range_obj.starting_date == datetime(2019, 1, 5).date() and
                range_obj.ending_date == datetime(2019, 1, 28).date())

    def test_add5(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-15',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-5',
                'ending_date': '2019-1-28',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 3
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assign1 += assign2

        range_obj = assign1.range_obj
        assert (assign1.starting_date == datetime(2019, 1, 5).date() and
                assign1.ending_date == datetime(2019, 1, 28).date() and
                range_obj.starting_date == datetime(2019, 1, 5).date() and
                range_obj.ending_date == datetime(2019, 1, 28).date())

    def test_get_difference1(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-15',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign = create_an_assignation(data, workshift_db)
        assign.starting_date = datetime(2019, 1, 13).date()

        resp = assign.get_differences()

        resp_left = Range(
            datetime(2019, 1, 10).date(),
            datetime(2019, 1, 12).date())

        assert [resp_left] == resp['was_deleted'] and resp['was_created'] == []

    def test_get_difference2(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-15',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign = create_an_assignation(data, workshift_db)
        assign.ending_date = datetime(2019, 1, 13).date()

        resp = assign.get_differences()

        resp_right = Range(
            datetime(2019, 1, 14).date(),
            datetime(2019, 1, 15).date())

        assert [resp_right] == resp['was_deleted'] and resp['was_created'] == []

    def test_get_difference3(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-15',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign = create_an_assignation(data, workshift_db)
        assign.starting_date = datetime(2019, 1, 10).date()
        assign.ending_date = datetime(2019, 1, 15).date()

        resp = assign.get_differences()

        assert [] == resp['was_deleted'] and resp['was_created'] == []

    def test_get_difference4(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-20',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign = create_an_assignation(data, workshift_db)
        assign.starting_date = datetime(2019, 1, 13).date()
        assign.ending_date = datetime(2019, 1, 18).date()

        resp = assign.get_differences()

        resp_left = Range(
            datetime(2019, 1, 10).date(),
            datetime(2019, 1, 12).date())

        resp_right = Range(
            datetime(2019, 1, 19).date(),
            datetime(2019, 1, 20).date())

        assert ([resp_left, resp_right] == resp['was_deleted'] and
                resp['was_created'] == [])

    def test_get_difference5(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-15',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign = create_an_assignation(data, workshift_db)
        assign.starting_date = datetime(2019, 1, 13).date()
        assign.ending_date = datetime(2019, 1, 18).date()

        resp = assign.get_differences()

        resp_left = Range(
            datetime(2019, 1, 10).date(),
            datetime(2019, 1, 12).date())

        resp_right = Range(
            datetime(2019, 1, 16).date(),
            datetime(2019, 1, 18).date())

        assert ([resp_right] == resp['was_created'] and
                resp['was_deleted'] == [resp_left])

    def test_get_difference6(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-15',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign = create_an_assignation(data, workshift_db)
        assign.starting_date = datetime(2019, 1, 7).date()
        assign.ending_date = datetime(2019, 1, 12).date()

        resp = assign.get_differences()

        resp_left = Range(
            datetime(2019, 1, 7).date(),
            datetime(2019, 1, 9).date())

        resp_right = Range(
            datetime(2019, 1, 13).date(),
            datetime(2019, 1, 15).date())

        assert ([resp_left] == resp['was_created'] and
                resp['was_deleted'] == [resp_right])

    def test_get_difference7(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-10',
                'ending_date': '2019-1-15',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign = create_an_assignation(data, workshift_db)
        assign.starting_date = datetime(2019, 1, 7).date()
        assign.ending_date = datetime(2019, 1, 12).date()

        resp = assign.get_differences()

        resp_left = Range(
            datetime(2019, 1, 7).date(),
            datetime(2019, 1, 9).date())

        resp_right = Range(
            datetime(2019, 1, 13).date(),
            datetime(2019, 1, 15).date())

        assert ([resp_left] == resp['was_created'] and
                resp['was_deleted'] == [resp_right])

    def test_get_difference8(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 8
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-2-16',
                'ending_date': '2019-2-16',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 8
            }
        }
        assign = create_an_assignation(data, workshift_db)
        assign.starting_date = datetime(2019, 2, 16).date()
        assign.ending_date = datetime(2019, 2, 20).date()

        resp = assign.get_differences()

        resp_right = Range(
            datetime(2019, 2, 17).date(),
            datetime(2019, 2, 20).date())

        assert ([resp_right] == resp['was_created'] and
                resp['was_deleted'] == [])
