import types
from datetime import datetime

from proxies.assignation_proxy import AssignationProxy
from utils.range import Range
from operators.assignation_operator import AssignationOperator
from test_utils.utils import create_an_assignation


class TestAssignationProxyAdd(object):
    """Class to test if the assignation mapper add method works well"""

    def test_add1(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 23).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        range_mapper = assign1.range_mapper
        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
                assign1.ending_date == datetime(2019, 1, 28).date() and
                range_mapper.starting_date == datetime(2019, 1, 1).date() and
                range_mapper.ending_date == datetime(2019, 1, 28).date())

    def test_add2(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 24).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        range_mapper = assign1.range_mapper
        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
                assign1.ending_date == datetime(2019, 1, 22).date() and
                range_mapper.starting_date == datetime(2019, 1, 1).date() and
                range_mapper.ending_date == datetime(2019, 1, 22).date())

    def test_add3(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 1
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 22).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 5
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        range_mapper = assign1.range_mapper
        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
                assign1.ending_date == datetime(2019, 1, 22).date() and
                range_mapper.starting_date == datetime(2019, 1, 1).date() and
                range_mapper.ending_date == datetime(2019, 1, 22).date())

    def test_add4(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 15).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 5).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        range_mapper = assign1.range_mapper
        assert (assign1.starting_date == datetime(2019, 1, 5).date() and
                assign1.ending_date == datetime(2019, 1, 28).date() and
                range_mapper.starting_date == datetime(2019, 1, 5).date() and
                range_mapper.ending_date == datetime(2019, 1, 28).date())

    def test_add5(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 15).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 5).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 3
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        range_mapper = assign1.range_mapper
        assert (assign1.starting_date == datetime(2019, 1, 5).date() and
                assign1.ending_date == datetime(2019, 1, 28).date() and
                range_mapper.starting_date == datetime(2019, 1, 5).date() and
                range_mapper.ending_date == datetime(2019, 1, 28).date())

    def test_get_difference1(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 15).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign = create_an_assignation(data)
        assign.starting_date = datetime(2019, 1, 13).date()

        resp = assign.get_differences()

        resp_left = Range(
            datetime(2019, 1, 10).date(),
            datetime(2019, 1, 12).date())

        assert [resp_left] == resp['was_deleted'] and resp['was_created'] == []

    def test_get_difference2(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 15).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign = create_an_assignation(data)
        assign.ending_date = datetime(2019, 1, 13).date()

        resp = assign.get_differences()

        resp_right = Range(
            datetime(2019, 1, 14).date(),
            datetime(2019, 1, 15).date())

        assert [resp_right] == resp['was_deleted'] and resp['was_created'] == []

    def test_get_difference3(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 15).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign = create_an_assignation(data)
        assign.starting_date = datetime(2019, 1, 10).date()
        assign.ending_date = datetime(2019, 1, 15).date()

        resp = assign.get_differences()

        assert [] == resp['was_deleted'] and resp['was_created'] == []

    def test_get_difference4(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 20).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign = create_an_assignation(data)
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
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 15).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign = create_an_assignation(data)
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
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 15).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign = create_an_assignation(data)
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
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 15).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign = create_an_assignation(data)
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
        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 16).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8
            }}
        assign = create_an_assignation(data)
        assign.starting_date = datetime(2019, 2, 16).date()
        assign.ending_date = datetime(2019, 2, 20).date()

        resp = assign.get_differences()

        resp_right = Range(
            datetime(2019, 2, 17).date(),
            datetime(2019, 2, 20).date())

        assert ([resp_right] == resp['was_created'] and
                resp['was_deleted'] == [])
