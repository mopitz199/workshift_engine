import pytest
from datetime import datetime
from workshift_engine.test_utils.utils import create_an_assignation


@pytest.fixture
def mapper():
    data = {
        'assignation': {
            'person': 5,
            'starting_date': datetime(2019, 1, 1).date(),
            'start_day': 1,
            'ending_date': datetime(2019, 1, 10).date(),
            'workshift_id': 10,
            'fake_attr': 'badAttr'
        },
        'workshift': {
            'total_workshift_days': 7
        }
    }

    return create_an_assignation(data)


class TestGetAttr(object):
    """To test if the get feature works properly as a mapper"""

    def test_wrong_attr1(self, mapper):
            try:
                mapper.hola
                assert False
            except:
                assert True

    def test_mapped_attr1(self, mapper):
            try:
                mapper.starting_date
                assert True
            except:
                assert False

    def test_mapped_attr2(self, mapper):
            try:
                mapper.workshift.total_workshift_days
                assert True
            except:
                assert False

    def test_not_mapped_attr1(self, mapper):
            try:
                mapper.obj
                assert True
            except:
                assert False

    def test_not_mapped_attr2(self, mapper):
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

    def test_set_attr3(self, mapper):
        mapper.starting_date = datetime(2019, 4, 5).date()
        assert mapper.starting_date == mapper.range_mapper.starting_date
