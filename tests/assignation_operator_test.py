import pytest
import types
from datetime import datetime

from operators.assignation_operator import *
from mappers.assignation_mapper import *

class DumbAssignation:

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)
        self.range_mapper = RangeMapper(self.starting_date, self.ending_date)

data = {
    'starting_date': datetime(2019, 1, 1).date(),
    'ending_date': datetime(2019, 1, 5).date()}
conf = {key:key for key in data.keys()}
assign1 = AssignationMapper(DumbAssignation(**data), conf)

class TestAreNeighbors(object):
    """This class are to test the method are_neighbors"""

    def test_are_neighbors1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 5).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert AssignationOperator.are_neighbors(assign1, assign2) == True

    def test_are_neighbors2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 6).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert AssignationOperator.are_neighbors(assign1, assign2) == True

    def test_arent_neighbors1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 4).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 6).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert AssignationOperator.are_neighbors(assign1, assign2) == False


class TestAreMultipleNeighbors(object):
    """To test if the function can get all the neighbors from
    the given list of assigns"""

    def test_are_multiple_neighbors1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 8).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 4).date(),
            'ending_date': datetime(2019, 1, 7).date()}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2]

        assert AssignationOperator.are_multiple_neighbors(assign, assign_list) == assign_list

    def test_are_multiple_neighbors2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 8).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 4).date(),
            'ending_date': datetime(2019, 1, 6).date()}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2]

        assert AssignationOperator.are_multiple_neighbors(assign, assign_list) == [assign1]

    def test_are_multiple_neighbors2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 9).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 7).date()}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2]

        assert AssignationOperator.are_multiple_neighbors(assign, assign_list) == []


class TestGetAssignationGenerator(object):
    """To test if method that take a list
    and it transform it in a generator works"""

    def test_get_assignation_generator1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 5).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2]

        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)

        all_assign = True
        for idx, assign in enumerate(assign_generator):
            if assign != assign_list[idx]:
                all_assign = False
                break 

        assert all_assign and isinstance(assign_generator, types.GeneratorType)


class TestGetMaxEndingDate(object):
    """To Test if the function return the assign with the
    maximum ending date from all the assignments"""

    def test_get_max_ending_date1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 5).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1,  assign2]
        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)
        assert AssignationOperator.get_max_ending_date(assign_generator) == assign2

    def test_get_max_ending_date2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 5).date(),
            'ending_date': datetime(2019, 1, 6).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1,  assign2]
        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)
        assert AssignationOperator.get_max_ending_date(assign_generator) == assign1

    
class TestGetMinStartingDate(object):
    """To Test if the function return the assign with the
    minimum starting date from all the assignments"""

    def test_get_min_starting_date1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 5).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1,  assign2]
        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)
        assert AssignationOperator.get_min_starting_date(assign_generator) == assign1

    def test_get_min_starting_date2(self):
        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 8).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 3).date(),
            'ending_date': datetime(2019, 1, 10).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1,  assign2]
        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)
        assert AssignationOperator.get_min_starting_date(assign_generator) == assign2


class TestSimulateStartingDay(object):
    """To test if the function to simulate an start_date from a
    given assign and date works."""

    def test_simulate_starting_day1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 31).date(),
            'start_day': 1,
            'total_workshift_days': 7}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        date_obj = datetime(2019, 1, 12).date()
        
        simulated_start_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 5 == simulated_start_day

    def test_simulate_starting_day2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 31).date(),
            'start_day': 3,
            'total_workshift_days': 6}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        date_obj = datetime(2019, 1, 14).date()
        
        simulated_start_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 4 == simulated_start_day

    def test_simulate_starting_day3(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 31).date(),
            'start_day': 2,
            'total_workshift_days': 8}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        date_obj = datetime(2019, 1, 23).date()
        
        simulated_start_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 8 == simulated_start_day

    def test_simulate_starting_day4(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 31).date(),
            'start_day': 2,
            'total_workshift_days': 6}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        date_obj = datetime(2019, 1, 6).date()
        
        simulated_start_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 1 == simulated_start_day

    def test_simulate_starting_day5(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 1).date(),
            'start_day': 4,
            'total_workshift_days': 6}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        date_obj = datetime(2019, 1, 1).date()
        
        simulated_start_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 4 == simulated_start_day

    def test_simulate_starting_day6(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 1).date(),
            'start_day': None,
            'total_workshift_days': 6}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        date_obj = datetime(2019, 1, 1).date()
        
        simulated_start_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert None == simulated_start_day


class TestAreCompatible(object):
    """To test if the function can determine if two assigns are
    comptaible to join"""

    def test_are_compatible1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 3).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 4).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 4}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert AssignationOperator.are_compatible(assign1, assign2)

    def test_are_compatible2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 3).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 3}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert AssignationOperator.are_compatible(assign1, assign2)

    def test_are_compatible3(self):
        data = {
            'starting_date': datetime(2019, 1, 3).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 3}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert AssignationOperator.are_compatible(assign1, assign2)

    def test_are_compatible4(self):
        data = {
            'starting_date': datetime(2018, 12, 28).date(),
            'ending_date': datetime(2019, 1, 10).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 3}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert AssignationOperator.are_compatible(assign1, assign2)

    def test_are_compatible5(self):
        data = {
            'starting_date': datetime(2018, 12, 28).date(),
            'ending_date': datetime(2019, 1, 10).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': None}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': None}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert AssignationOperator.are_compatible(assign1, assign2)

    def test_are_compatible6(self):
        data = {
            'starting_date': datetime(2018, 12, 28).date(),
            'ending_date': datetime(2019, 1, 10).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': None}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert not AssignationOperator.are_compatible(assign1, assign2)


    def test_arent_compatible1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 3).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 4).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 6,
            'start_day': 3}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert not AssignationOperator.are_compatible(assign1, assign2)

    def test_arent_compatible2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 3).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 3,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 4).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 3,
            'start_day': 2}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assert not AssignationOperator.are_compatible(assign1, assign2)



class TestAreMultipleCompatible(object):
    """To test if the function can determine if two assigns are
    comptaible to join"""

    def test_are_compatible1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 6}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 11).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 4}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 6).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 3}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        list_assigns = [assign1, assign2]

        resp = AssignationOperator.are_multiple_compatible(assign, list_assigns)

        assert list_assigns == resp

    def test_are_compatible2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 6}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 11).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 4}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 4).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        list_assigns = [assign1, assign2]

        resp = AssignationOperator.are_multiple_compatible(assign, list_assigns)

        assert list_assigns == resp

    def test_are_compatible3(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 6}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 11).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 5}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 4).date(),
            'ending_date': datetime(2019, 1, 6).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        list_assigns = [assign1, assign2]

        resp = AssignationOperator.are_multiple_compatible(assign, list_assigns)

        assert resp == [assign1]

    def test_are_compatible4(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 6}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 11).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 4}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2018, 12, 31).date(),
            'ending_date': datetime(2019, 1, 8).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 5}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        list_assigns = [assign1, assign2]

        resp = AssignationOperator.are_multiple_compatible(assign, list_assigns)
        assert resp == list_assigns

    
class TestGetBiggestAssign(object):
    """To test if the function determine the assignment with the more
    quantity of days"""

    def test_get_biggest_assign1(self):
        data = {
            'starting_date': datetime(2018, 12, 31).date(),
            'ending_date': datetime(2019, 1, 8).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 2, 1).date(),
            'ending_date': datetime(2019, 3, 8).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2018, 12, 31).date(),
            'ending_date': datetime(2019, 1, 7).date()}
        conf = {key:key for key in data.keys()}
        assign3 = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2, assign3]

        assert AssignationOperator.get_biggest_assign(assign_list) == assign2

    
    def test_get_biggest_assign2(self):
        data = {
            'starting_date': datetime(2018, 12, 31).date(),
            'ending_date': datetime(2019, 1, 8).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 3, 1).date(),
            'ending_date': datetime(2019, 3, 20).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2]

        assert AssignationOperator.get_biggest_assign(assign_list) == assign2

    def test_get_biggest_assign3(self):
        data = {
            'starting_date': datetime(2018, 12, 31).date(),
            'ending_date': datetime(2019, 1, 8).date()}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2018, 12, 31).date(),
            'ending_date': datetime(2019, 1, 8).date()}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2]

        assert AssignationOperator.get_biggest_assign(assign_list) == assign1

        
class TestGetCandidates(object):
    """To test if the function can get the best and the other candidates from
    a given list of assignments mappers."""

    def test_get_candidates1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 6}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 11).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 2}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 13).date(),
            'ending_date': datetime(2019, 1, 16).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 2}
        conf = {key:key for key in data.keys()}
        assign3 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 4).date(),
            'ending_date': datetime(2019, 1, 14).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2, assign3] 

        best, others = AssignationOperator.get_candidates(assign, assign_list)

        assert best == assign1 and others == [assign3]

    def test_get_candidates2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 6}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 11).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 2}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 13).date(),
            'ending_date': datetime(2019, 1, 16).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 2}
        conf = {key:key for key in data.keys()}
        assign3 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 14).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 4}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2, assign3] 

        best, others = AssignationOperator.get_candidates(assign, assign_list)

        assert best == assign3 and others == []  

    def test_get_candidates3(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 5).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 6}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 7).date(),
            'ending_date': datetime(2019, 1, 11).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 4}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 13).date(),
            'ending_date': datetime(2019, 1, 16).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 2}
        conf = {key:key for key in data.keys()}
        assign3 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 12).date(),
            'ending_date': datetime(2019, 1, 12).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        assign_list = [assign1, assign2, assign3] 

        best, others = AssignationOperator.get_candidates(assign, assign_list)

        assert best == assign2 and others == [assign3]


class TestGetRemovingType(object):
    """To test if the function can get the type of how to
    handle an assign remove."""

    def test_get_removing_type1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        starting_date = datetime(2019, 1, 3).date()
        ending_date = datetime(2019, 1, 21).date()

        removing_type = AssignationOperator.get_removing_type(
            assign, starting_date, ending_date
        )

        assert removing_type == 'middle'

    def test_get_removing_type2(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        starting_date = datetime(2018, 12, 15).date()
        ending_date = datetime(2019, 1, 21).date()

        removing_type = AssignationOperator.get_removing_type(
            assign, starting_date, ending_date
        )

        assert removing_type == 'one_side'

    def test_get_removing_type3(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        starting_date = datetime(2019, 1, 1).date()
        ending_date = datetime(2019, 1, 22).date()

        removing_type = AssignationOperator.get_removing_type(
            assign, starting_date, ending_date
        )

        assert removing_type == 'complete'

    def test_get_removing_type3(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        starting_date = datetime(2019, 1, 22).date()
        ending_date = datetime(2019, 1, 23).date()

        removing_type = AssignationOperator.get_removing_type(
            assign, starting_date, ending_date
        )

        assert removing_type == 'one_side'


class TestCopyAssign(object):
    """To test if the function can get the best and the other candidates from
    a given list of assignments mappers."""

    def test_copy_assign1(self):
        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign1 = AssignationMapper(DumbAssignation(**data), conf)

        data = {
            'starting_date': datetime(2019, 1, 1).date(),
            'ending_date': datetime(2019, 1, 22).date(),
            'workshift': 4,
            'person': 1,
            'total_workshift_days': 8,
            'start_day': 1}
        conf = {key:key for key in data.keys()}
        assign2 = AssignationMapper(DumbAssignation(**data), conf)

        assign.eaten_assignments = [assign1, assign2]

        copy_assign = AssignationOperator.copy_assign(assign)

        assert id(copy_assign) != id(assign)
