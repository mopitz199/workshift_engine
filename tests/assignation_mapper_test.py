import pytest
import types
from datetime import datetime

from mappers.assignation_mapper import AssignationMapper
from test_utils.utils import create_an_assignation

from operators.assignation_operator import AssignationOperator

class TestAssignationMapperAdd(object):
    """Class to test if the assignation mapper add method works well"""

    def test_add1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': None}
        assign1 = create_an_assignation(data)

        data = {
            'starting_date': datetime(2019, 1, 23).date(),
            'ending_date': datetime(2019, 1, 28).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': None}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
            assign1.ending_date == datetime(2019, 1, 28).date() and
            assign1.range_mapper.starting_date == datetime(2019, 1, 1).date() and
            assign1.range_mapper.ending_date == datetime(2019, 1, 28).date())

    def test_add2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': None}
        assign1 = create_an_assignation(data)

        data = {
            'starting_date': datetime(2019, 1, 24).date(),
            'ending_date': datetime(2019, 1, 28).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': None}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
            assign1.ending_date == datetime(2019, 1, 22).date() and
            assign1.range_mapper.starting_date == datetime(2019, 1, 1).date() and
            assign1.range_mapper.ending_date == datetime(2019, 1, 22).date())

    def test_add3(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        assign1 = create_an_assignation(data)

        data = {
            'starting_date': datetime(2019, 1, 22).date(),
            'ending_date': datetime(2019, 1, 28).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': 5}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
            assign1.ending_date == datetime(2019, 1, 22).date() and
            assign1.range_mapper.starting_date == datetime(2019, 1, 1).date() and
            assign1.range_mapper.ending_date == datetime(2019, 1, 22).date())

    def test_add4(self):
        data = {
            'starting_date': datetime(2019, 1, 10).date(),
            'ending_date': datetime(2019, 1, 15).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': None}
        assign1 = create_an_assignation(data)

        data = {
            'starting_date': datetime(2019, 1, 5).date(),
            'ending_date': datetime(2019, 1, 28).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': None}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        assert (assign1.starting_date == datetime(2019, 1, 5).date() and
            assign1.ending_date == datetime(2019, 1, 28).date() and
            assign1.range_mapper.starting_date == datetime(2019, 1, 5).date() and
            assign1.range_mapper.ending_date == datetime(2019, 1, 28).date())

    def test_add5(self):
        data = {
            'starting_date': datetime(2019, 1, 10).date(),
            'ending_date': datetime(2019, 1, 15).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': 8}
        assign1 = create_an_assignation(data)

        data = {
            'starting_date': datetime(2019, 1, 5).date(),
            'ending_date': datetime(2019, 1, 28).date(),
            'workshift_id': 4,
            'person_id': 1,
            'total_workshift_days': 8,
            'start_day': 3}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        assert (assign1.starting_date == datetime(2019, 1, 5).date() and
            assign1.ending_date == datetime(2019, 1, 28).date() and
            assign1.range_mapper.starting_date == datetime(2019, 1, 5).date() and
            assign1.range_mapper.ending_date == datetime(2019, 1, 28).date())