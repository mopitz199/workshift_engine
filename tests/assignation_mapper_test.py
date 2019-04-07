import pytest
import types
from datetime import datetime

from mappers.assignation_mapper import AssignationMapper

class DumbAssignation:

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)

class TestAssignationMapperAdd(object):

    def test_add1(self):
        pass
