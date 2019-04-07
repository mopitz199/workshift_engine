import pytest
from datetime import datetime
from mappers.assignation_mapper import *

class DummyClass:

    def __init__(self):
        self.person = "Maximiliano Opitz"
        self.fromDate = datetime(2019, 1, 1).date()
        self.toDate = datetime(2019, 1, 31).date()
        self.start_day = 1
        self.workShift = "Semanal Talana"
        self.total_workshift_days = 13

attr_mapping = {
    'person': 'person',
    'starting_date': 'fromDate',
    'start_day': 'start_day',
    'ending_date': 'toDate',
    'workshift': 'workShift',
    'total_workshift_days': 'total_workshift_days',
    'fake_attr': 'badAttr'
}

@pytest.fixture
def mapper():
    dummy_obj = DummyClass()
    return AssignationMapper(dummy_obj, attr_mapping)


class TestGetAttr(object):
    """To test if the get feature works properly as a mapper"""

    def test_wrong_attr(self, mapper):
            try:
                mapper.hola
                assert False
            except:
                assert True

    def test_mapped_attr(self, mapper):
            try:
                mapper.starting_date
                assert True
            except:
                assert False

    def test_not_mapped_attr(self, mapper):
            try:
                mapper.obj
                assert True
            except:
                assert False

    def test_not_mapped_attr(self, mapper):
            try:
                mapper.obj
                assert True
            except:
                assert False


class TestSetAttr(object):
    """To test if the set feature works properly as a mapper"""

    def test_set_attr1(self, mapper):
        mapper.start_day = 4
        assert mapper.obj.start_day == 4

    def test_set_attr2(self, mapper):
        mapper.hola = 4
        assert mapper.hola == 4