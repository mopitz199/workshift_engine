import types
from datetime import datetime

from assignation.operators.assignation_operator import AssignationOperator
from database.workshift_db import WorkShiftDB
from proxies.workshift_proxy import WorkShiftProxy

from test_utils.utils import (
    create_an_assignation,
    create_proxy_workshifts
)


class TestAreNeighbors(object):
    """This class are to test the method are_neighbors"""

    def test_are_neighbors1(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-5'}}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-5',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        assert AssignationOperator.are_neighbors(assign1, assign2)

    def test_are_neighbors2(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-5'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-6',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        assert AssignationOperator.are_neighbors(assign1, assign2)

    def test_arent_neighbors1(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-4'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-6',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        assert not AssignationOperator.are_neighbors(assign1, assign2)


class TestAreMultipleNeighbors(object):
    """To test if the function can get all the neighbors from
    the given list of assigns"""

    def test_are_multiple_neighbors1(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-5'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-8',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-7'}}

        assign = create_an_assignation(data)

        assign_list = [assign1, assign2]

        resp = AssignationOperator.are_multiple_neighbors(assign, assign_list)
        assert resp == assign_list

    def test_are_multiple_neighbors2(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-5'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-8',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-6'}}

        assign = create_an_assignation(data)

        assign_list = [assign1, assign2]

        resp = AssignationOperator.are_multiple_neighbors(assign, assign_list)
        assert resp == [assign1]

    def test_are_multiple_neighbors3(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-5'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-9',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-7'}}

        assign = create_an_assignation(data)

        assign_list = [assign1, assign2]

        resp = AssignationOperator.are_multiple_neighbors(assign, assign_list)
        assert resp == []


class TestGetAssignationGenerator(object):
    """To test if method that take a list
    and it transform it in a generator works"""

    def test_get_assignation_generator1(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-5'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-5',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

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
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-5'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-5',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        assign_list = [assign1,  assign2]
        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)

        resp = AssignationOperator.get_max_ending_date(assign_generator)
        assert resp == assign2

    def test_get_max_ending_date2(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-10'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-5',
                'ending_date': '2019-1-6'}}

        assign2 = create_an_assignation(data)

        assign_list = [assign1,  assign2]
        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)

        resp = AssignationOperator.get_max_ending_date(assign_generator)
        assert resp == assign1


class TestGetMinStartingDate(object):
    """To Test if the function return the assign with the
    minimum starting date from all the assignments"""

    def test_get_min_starting_date1(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-5'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-5',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        assign_list = [assign1,  assign2]
        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)

        resp = AssignationOperator.get_min_starting_date(assign_generator)
        assert resp == assign1

    def test_get_min_starting_date2(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-8'}}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-3',
                'ending_date': '2019-1-10'}}

        assign2 = create_an_assignation(data)

        assign_list = [assign1,  assign2]
        assign_generator = AssignationOperator.get_assignation_generator(
            assign_list)

        resp = AssignationOperator.get_min_starting_date(assign_generator)
        assert resp == assign2


class TestAreCompatible(object):
    """To test if the function can determine if two assigns are
    comptaible to join"""

    def test_can_be_joined1(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 6
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-3',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }

        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 4
            }
        }

        assign2 = create_an_assignation(data, workshift_db)

        assert AssignationOperator.can_be_joined(assign1, assign2)

    def test_can_be_joined2(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 6
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-3',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 3
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assert AssignationOperator.can_be_joined(assign1, assign2)

    def test_can_be_joined3(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 6
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-3',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 3
            }
        }

        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }

        assign2 = create_an_assignation(data, workshift_db)

        assert AssignationOperator.can_be_joined(assign1, assign2)

    def test_can_be_joined4(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 6
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2018-12-28',
                'ending_date': '2019-1-10',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 3
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assert AssignationOperator.can_be_joined(assign1, assign2)

    def test_can_be_joined5(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 6
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2018-12-28',
                'ending_date': '2019-1-10',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assert AssignationOperator.can_be_joined(assign1, assign2)

    def test_can_be_joined6(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 6
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2018-12-28',
                'ending_date': '2019-1-10',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': None
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assert not AssignationOperator.can_be_joined(assign1, assign2)

    def test_arent_compatible1(self):

        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 6
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-3',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }

        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 3
            }
        }

        assign2 = create_an_assignation(data, workshift_db)

        assert not AssignationOperator.can_be_joined(assign1, assign2)

    def test_arent_compatible2(self):
        workshifts_data = [
            {
                'id': 4,
                'total_workshift_days': 3
            }
        ]
        workshifts = create_proxy_workshifts(workshifts_data)
        workshift_db = WorkShiftDB(workshifts, WorkShiftProxy)

        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-3',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 2
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        assert not AssignationOperator.can_be_joined(assign1, assign2)


class TestAreMultipleCompatible(object):
    """To test if the function can determine if two assigns are
    comptaible to join"""

    def test_can_be_joined1(self):

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
                'ending_date': '2019-1-5',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-11',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 4
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-6',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 3
            }
        }
        assign = create_an_assignation(data, workshift_db)

        list_assigns = [assign1, assign2]

        resp = AssignationOperator.are_multiple_compatible(
            assign,
            list_assigns)

        assert list_assigns == resp

    def test_can_be_joined2(self):

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
                'ending_date': '2019-1-5',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-11',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 4
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign = create_an_assignation(data, workshift_db)

        list_assigns = [assign1, assign2]

        resp = AssignationOperator.are_multiple_compatible(
            assign,
            list_assigns)

        assert list_assigns == resp

    def test_can_be_joined3(self):

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
                'ending_date': '2019-1-5',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-11',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 5
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-6',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign = create_an_assignation(data, workshift_db)

        list_assigns = [assign1, assign2]

        resp = AssignationOperator.are_multiple_compatible(
            assign,
            list_assigns)

        assert resp == [assign1]

    def test_can_be_joined4(self):

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
                'ending_date': '2019-1-5',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-11',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 4
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2018-12-31',
                'ending_date': '2019-1-8',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 5
            }
        }
        assign = create_an_assignation(data, workshift_db)

        list_assigns = [assign1, assign2]

        resp = AssignationOperator.are_multiple_compatible(
            assign,
            list_assigns)

        assert resp == list_assigns


class TestGetBiggestAssign(object):
    """To test if the function determine the assignment with the more
    quantity of days"""

    def test_get_biggest_assign1(self):

        data = {
            'assignation': {
                'starting_date': '2018-12-31',
                'ending_date': '2019-1-8'
            }}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-2-1',
                'ending_date': '2019-3-8'
            }}

        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2018-12-31',
                'ending_date': '2019-1-7'
            }}

        assign3 = create_an_assignation(data)

        assign_list = [assign1, assign2, assign3]

        assert AssignationOperator.get_biggest_assign(assign_list) == assign2

    def test_get_biggest_assign2(self):
        data = {
            'assignation': {
                'starting_date': '2018-12-31',
                'ending_date': '2019-1-8'
            }}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-3-1',
                'ending_date': '2019-3-20'
            }}

        assign2 = create_an_assignation(data)

        assign_list = [assign1, assign2]

        assert AssignationOperator.get_biggest_assign(assign_list) == assign2

    def test_get_biggest_assign3(self):
        data = {
            'assignation': {
                'starting_date': '2018-12-31',
                'ending_date': '2019-1-8'
            }}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2018-12-31',
                'ending_date': '2019-1-8'
            }}

        assign2 = create_an_assignation(data)

        assign_list = [assign1, assign2]

        assert AssignationOperator.get_biggest_assign(assign_list) == assign1


class TestGetCandidates(object):
    """To test if the function can get the best and the other candidates from
    a given list of assignments proxies."""

    def test_get_candidates1(self):

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
                'ending_date': '2019-1-5',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-11',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 2
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-13',
                'ending_date': '2019-1-16',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 2
            }
        }
        assign3 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-14',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign = create_an_assignation(data, workshift_db)

        assign_list = [assign1, assign2, assign3]

        best, others = AssignationOperator.get_candidates(assign, assign_list)

        assert best == assign1 and others == [assign3]

    def test_get_candidates2(self):

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
                'ending_date': '2019-1-5',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-11',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 2
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-13',
                'ending_date': '2019-1-16',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 2
            }
        }
        assign3 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-14',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 4
            }
        }
        assign = create_an_assignation(data, workshift_db)

        assign_list = [assign1, assign2, assign3]

        best, others = AssignationOperator.get_candidates(assign, assign_list)

        assert best == assign3 and others == []

    def test_get_candidates3(self):

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
                'ending_date': '2019-1-5',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign1 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-7',
                'ending_date': '2019-1-11',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 4
            }
        }
        assign2 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-13',
                'ending_date': '2019-1-16',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 2
            }
        }
        assign3 = create_an_assignation(data, workshift_db)

        data = {
            'assignation': {
                'starting_date': '2019-1-12',
                'ending_date': '2019-1-12',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 1
            }
        }
        assign = create_an_assignation(data, workshift_db)

        assign_list = [assign1, assign2, assign3]

        best, others = AssignationOperator.get_candidates(assign, assign_list)

        assert best == assign2 and others == [assign3]


class TestRemove(object):
    """To test if the function to remove a range from a given assignation
    works properly"""

    def test_remove1(self):

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
                'ending_date': '2019-1-5',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign = create_an_assignation(data, workshift_db)

        resp = AssignationOperator.remove(
            assign,
            datetime(2019, 1, 1).date(),
            datetime(2019, 1, 1).date())

        resp_assign = resp['update']

        assert (resp['create'] is None and
                resp['delete'] is None and
                resp['update'] == assign and
                resp_assign.starting_day == 7 and
                resp_assign.starting_date == datetime(2019, 1, 2).date() and
                resp_assign.ending_date == datetime(2019-1-5).date())

    def test_remove2(self):

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
                'ending_date': '2019-1-10',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign = create_an_assignation(data, workshift_db)

        resp = AssignationOperator.remove(
            assign,
            datetime(2019, 1, 4).date(),
            datetime(2019, 1, 6).date())

        resp_assign = resp['update']
        new_assign = resp['create']

        assert (resp_assign.starting_date == datetime(2019, 1, 7).date() and
                resp_assign.ending_date == datetime(2019, 1, 1).date() and
                resp_assign.starting_day == 4 and
                new_assign.starting_date == datetime(2019, 1, 1).date() and
                new_assign.ending_date == datetime(2019, 1, 3).date() and
                new_assign.starting_day == 6 and
                resp['update'] == assign and
                resp['delete'] is None)

    def test_remove3(self):

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
                'ending_date': '2019-1-10',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign = create_an_assignation(data, workshift_db)

        resp = AssignationOperator.remove(
            assign,
            datetime(2019, 1, 4).date(),
            datetime(2019, 1, 14).date())

        resp_assign = resp['update']

        assert (resp_assign.starting_date == datetime(2019, 1, 1).date() and
                resp_assign.ending_date == datetime(2019, 1, 3).date() and
                resp_assign.starting_day == 6 and
                resp['update'] == assign and
                resp['create'] is None and
                resp['delete'] is None)

    def test_remove4(self):

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
                'ending_date': '2019-1-10',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign = create_an_assignation(data, workshift_db)

        resp = AssignationOperator.remove(
            assign,
            datetime(2019, 1, 1).date(),
            datetime(2019, 1, 14).date())

        assert (resp['delete'] == assign and
                resp['update'] is None and
                resp['create'] is None)

    def test_remove5(self):

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
                'ending_date': '2019-1-10',
                'workshift_id': 4,
                'person_id': 1,
                'starting_day': 6
            }
        }
        assign = create_an_assignation(data, workshift_db)

        resp = AssignationOperator.remove(
            assign,
            datetime(2019, 1, 12).date(),
            datetime(2019, 1, 14).date())

        assert (resp['delete'] is None and
                resp['update'] is None and
                resp['create'] is None)


class TestSortAscStartingDate(object):

    def test_sort_asc_starting_date1(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-10'
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-13',
                'ending_date': '2019-1-18'
            }}
        assign2 = create_an_assignation(data)

        assigns = [assign2, assign1]

        resp = AssignationOperator.sort_asc_starting_date(assigns)

        assert resp == [assign1, assign2]

    def test_sort_asc_starting_date2(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-10'
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-18'
            }}
        assign2 = create_an_assignation(data)

        assigns = [assign2, assign1]

        resp = AssignationOperator.sort_asc_starting_date(assigns)

        assert resp == [assign1, assign2]

    def test_sort_asc_starting_date3(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-10'
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-18'
            }}
        assign2 = create_an_assignation(data)

        assigns = [assign1, assign2]

        resp = AssignationOperator.sort_asc_starting_date(assigns)

        assert resp == assigns


class TestSortDescStartingDate(object):

    def test_sort_desc_starting_date1(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-10'
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-13',
                'ending_date': '2019-1-18'
            }}
        assign2 = create_an_assignation(data)

        assigns = [assign1, assign2]

        resp = AssignationOperator.sort_desc_starting_date(assigns)

        assert resp == [assign2, assign1]

    def test_sort_desc_starting_date2(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-10'
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-18'
            }}
        assign2 = create_an_assignation(data)

        assigns = [assign1, assign2]

        resp = AssignationOperator.sort_desc_starting_date(assigns)

        assert resp == [assign2, assign1]

    def test_sort_desc_starting_date3(self):
        data = {
            'assignation': {
                'starting_date': '2019-1-1',
                'ending_date': '2019-1-10'
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': '2019-1-4',
                'ending_date': '2019-1-18'
            }}
        assign2 = create_an_assignation(data)

        assigns = [assign2, assign1]

        resp = AssignationOperator.sort_desc_starting_date(assigns)

        assert resp == assigns
