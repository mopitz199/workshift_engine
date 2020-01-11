import pytest  # type: ignore
from datetime import datetime

from database.workshift_db import WorkShiftDB
from proxies.workshift_proxy import WorkShiftProxy
from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts,
)


@pytest.fixture
def proxy():

    workshifts_data = [
        {
            'id': 10,
            'total_workshift_days': 7
        }
    ]
    workshifts = create_proxy_workshifts(workshifts_data)
    workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

    data = {
        'assignation': {
            'person': 5,
            'starting_date': '2019-1-1',
            'starting_day': 1,
            'ending_date': '2019-1-10',
            'workshift_id': 10,
            'fake_attr': 'badAttr'
        }
    }

    return create_an_assignation(data, workshift_db)


class TestGetAttr(object):
    """To test if the get feature works properly as a proxy"""

    def test_wrong_attr1(self, proxy):
        try:
            proxy.hola
            assert False
        except Exception:
            assert True

    def test_mapped_attr1(self, proxy):
        try:
            proxy.starting_date
            assert True
        except Exception:
            assert False

    def test_mapped_attr2(self, proxy):
        try:
            proxy.workshift_proxy.total_workshift_days
            assert True
        except Exception:
            assert False

    def test_not_mapped_attr1(self, proxy):
        try:
            proxy.obj
            assert True
        except Exception:
            assert False

    def test_not_mapped_attr2(self, proxy):
        try:
            proxy.obj
            assert True
        except Exception:
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
