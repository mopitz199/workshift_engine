import pytest
import types
from datetime import datetime

from mappers.assignation_mapper import AssignationMapper
from test_utils.utils import create_an_assignation

class TestAssignationMapperAdd(object):

    def test_add1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift_id': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': None}
        assign1 = create_an_assignation(data)

        data = {
            'starting_date': datetime(2019, 1, 23).date(),
            'ending_date': datetime(2019, 1, 28).date(),
            'workshift_id': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': None}
        assign2 = create_an_assignation(data)

        assign1 += assign2

        assert (assign1.starting_date == datetime(2019, 1, 1).date() and
            assign1.ending_date == datetime(2019, 1, 28).date() and
            assign1.range_mapper.starting_date == datetime(2019, 1, 1).date() and
            assign1.range_mapper.ending_date == datetime(2019, 1, 28).date())