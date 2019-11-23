import pytest
from datetime import datetime
from test_utils.utils import create_an_assignation


@pytest.fixture
def proxy():
    data = {
        'assignation': {
            'person': 5,
            'starting_date': datetime(2019, 1, 1).date(),
            'starting_day': 1,
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
    """To test if the get feature works properly as a proxy"""

    def test_wrong_attr1(self, proxy):
            try:
                proxy.hola
                assert False
            except:
                assert True

    def test_mapped_attr1(self, proxy):
            try:
                proxy.starting_date
                assert True
            except:
                assert False

    def test_mapped_attr2(self, proxy):
            try:
                proxy.workshift.total_workshift_days
                assert True
            except:
                assert False

    def test_not_mapped_attr1(self, proxy):
            try:
                proxy.obj
                assert True
            except:
                assert False

    def test_not_mapped_attr2(self, proxy):
            try:
                proxy.obj
                assert True
            except:
                assert False


class TestSetAttr(object):
    """To test if the set feature works properly as a proxy"""

    def test_set_attr1(self, proxy):
        proxy.starting_day = 4
        assert proxy.obj.starting_day == 4

    def test_set_attr2(self, proxy):
        proxy.hola = 4
        assert proxy.hola == 4

    def test_set_attr3(self, proxy):
        proxy.starting_date = datetime(2019, 4, 5).date()
        assert proxy.starting_date == proxy.range_obj.starting_date
