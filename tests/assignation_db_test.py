from datetime import datetime

from database.assignation_db import AssignationDB
from test_utils.utils import create_an_assignation


class TestAssignationBuildDatabase(object):
    """Class to test if the init function works well"""

    def test_init1(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'total_workshift_days': 8,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 1, 23).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)

        assert assignation_db.db == {'4_1': assignations}

    def test_init2(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}

        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 1, 23).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 5,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}

        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)

        assert assignation_db.db == {'4_1': [assign1], '5_1': [assign2]}


class TestAssignationAddDatabase(object):
    """
    Class to test if the function to add an assignation
    to the database works well
    """

    def test_add1(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1}}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 1, 24).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 4,
                'person_id': 1}}
        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 4,
                'person_id': 1}}
        assign3 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.add(assign3)

        total_assignations = [assign1, assign2, assign3]

        assert (assignation_db.db == {'4_1': total_assignations} and
                assignation_db.to_be_created == [assign3])

    def test_add2(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 4,
                'person_id': 1}}
        assign = create_an_assignation(data)

        assignations = []

        assignation_db = AssignationDB(assignations, None)
        assignation_db.add(assign)

        total_assignations = [assign]

        assert (assignation_db.db == {'4_1': total_assignations} and
                assignation_db.to_be_created == [])

    def test_add3(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1}}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 7,
                'person_id': 1}}

        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 8,
                'person_id': 1}}
        assign3 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.add(assign3)

        assert (assignation_db.db == {
            '6_1': [assign1],
            '7_1': [assign2],
            '8_1': [assign3]} and
            assignation_db.to_be_created == [assign3])


class TestAssignationRemoveDatabase(object):
    """
    Class to test if the function to remove
    an assignation to the database works well
    """

    def test_remove1(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1}}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 7,
                'person_id': 1}}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.remove(assign1)

        assert (assignation_db.db == {'7_1': [assign2]} and
                assignation_db.to_be_deleted == [assign1])

    def test_remove2(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1}}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1}}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.remove(assign1)

        assert (assignation_db.db == {'6_1': [assign2]} and
                assignation_db.to_be_deleted == [assign1])

    def test_remove3(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1}}
        assign1 = create_an_assignation(data)

        assignations = [assign1]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.remove(assign1)

        assert (assignation_db.db == {} and
                assignation_db.to_be_deleted == [assign1])

    def test_remove4(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1
            }}
        assign1 = create_an_assignation(data)

        assignations = []

        assignation_db = AssignationDB(assignations, None)
        assignation_db.add(assign1)
        assignation_db.remove(assign1)

        assert (assignation_db.db == {} and
                assignation_db.to_be_deleted == [] and
                assignation_db.to_be_updated == [] and
                assignation_db.to_be_created == [])


class TestAssignationUpdateDatabase(object):
    """
    Class to test if the function to update an
    assignation to the database works well
    """

    def test_update1(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1}}
        assign1 = create_an_assignation(data)

        assignations = [assign1]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.update(assign1)

        assert (assignation_db.db == {'6_1': [assign1]} and
                assignation_db.to_be_updated == [assign1])

    def test_update2(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1
            }}
        assign1 = create_an_assignation(data)

        assignations = []

        assignation_db = AssignationDB(assignations, None)
        assignation_db.add(assign1)

        assert (assignation_db.db == {'6_1': [assign1]} and
                assignation_db.to_be_updated == [] and
                assignation_db.to_be_created == [assign1])


class TestAssignationOperatorDatabase(object):
    """Class to test a combiation off add, remove and update
    in special circunstances with assignate and unassign methods"""

    def test_opetrator_database1(self):
        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 18).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.unassign(assign1)
        assignation_db.assignate(assign2)

        assert (assignation_db.db == {'6_1': [assign1]} and
                assignation_db.to_be_updated == [assign1] and
                assignation_db.to_be_created == [] and
                assignation_db.to_be_deleted == [])

    def test_opetrator_database2(self):
        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 18).date(),
                'ending_date': datetime(2019, 2, 20).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 19).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign3 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.unassign(assign1)
        assignation_db.unassign(assign2)
        assignation_db.assignate(assign3)

        assert (assignation_db.db == {'6_1': [assign2]} and
                assignation_db.to_be_updated == [assign2] and
                assignation_db.to_be_created == [] and
                assignation_db.to_be_deleted == [assign1])

    def test_opetrator_database3(self):
        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 18).date(),
                'ending_date': datetime(2019, 2, 20).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 24).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 19).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign3 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.unassign(assign1)
        assignation_db.unassign(assign2)
        assignation_db.assignate(assign3)

        assert (assignation_db.db == {'6_1': [assign2]} and
                assignation_db.to_be_updated == [assign2] and
                assignation_db.to_be_created == [] and
                assignation_db.to_be_deleted == [assign1])

    def test_opetrator_database4(self):
        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 10).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 20).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 15).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign3 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 13).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign4 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.unassign(assign1)
        assignation_db.unassign(assign2)
        assignation_db.assignate(assign3)
        assignation_db.assignate(assign4)

        rm2 = assign2.range_mapper
        rm1 = assign1.range_mapper

        assert (assignation_db.db == {'6_1': [assign2, assign1]} and
                assignation_db.to_be_updated == [assign2, assign1] and
                assignation_db.to_be_created == [] and
                assignation_db.to_be_deleted == [] and
                rm2.starting_date == datetime(2019, 2, 15).date() and
                rm2.ending_date == datetime(2019, 2, 25).date() and
                rm1.starting_date == datetime(2019, 2, 13).date() and
                rm1.ending_date == datetime(2019, 2, 13).date())

    def test_opetrator_database5(self):
        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 10).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 20).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 15).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign3 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 13).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign4 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 14).date(),
                'ending_date': datetime(2019, 2, 14).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            }}
        assign5 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.unassign(assign1)
        assignation_db.unassign(assign2)
        assignation_db.assignate(assign3)
        assignation_db.assignate(assign4)
        assignation_db.assignate(assign5)

        rm2 = assign2.range_mapper

        assert (assignation_db.db == {'6_1': [assign2]} and
                assignation_db.to_be_updated == [assign2] and
                assignation_db.to_be_created == [] and
                assignation_db.to_be_deleted == [assign1] and
                rm2.starting_date == datetime(2019, 2, 13).date() and
                rm2.ending_date == datetime(2019, 2, 25).date())

    def test_opetrator_database6(self):
        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 10).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 20).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 3
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 15).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 6
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign3 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 13).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 4
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign4 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 14).date(),
                'ending_date': datetime(2019, 2, 14).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 5
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign5 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.unassign(assign1)
        assignation_db.unassign(assign2)
        assignation_db.assignate(assign3)
        assignation_db.assignate(assign4)
        assignation_db.assignate(assign5)

        rm2 = assign2.range_mapper

        assert (assignation_db.db == {'6_1': [assign2]} and
                assignation_db.to_be_updated == [assign2] and
                assignation_db.to_be_created == [] and
                assignation_db.to_be_deleted == [assign1] and
                rm2.starting_date == datetime(2019, 2, 13).date() and
                rm2.ending_date == datetime(2019, 2, 25).date())

    def test_opetrator_database7(self):
        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 10).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 3,
                'starting_date': datetime(2019, 2, 20).date(),
                'ending_date': datetime(2019, 2, 28).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 3
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 15).date(),
                'ending_date': datetime(2019, 2, 25).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 6
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign3 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 13).date(),
                'ending_date': datetime(2019, 2, 13).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 4
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign4 = create_an_assignation(data)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 14).date(),
                'ending_date': datetime(2019, 2, 14).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign5 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        assignation_db.unassign(assign1)
        assignation_db.unassign(assign2)
        assignation_db.assignate(assign3)
        assignation_db.assignate(assign4)
        assignation_db.assignate(assign5)

        rm2 = assign2.range_mapper
        rm1 = assign1.range_mapper
        rm5 = assign5.range_mapper

        assert (assignation_db.db == {'6_1': [assign2, assign1, assign5]} and
                assignation_db.to_be_updated == [assign2, assign1] and
                assignation_db.to_be_created == [assign5] and
                assignation_db.to_be_deleted == [] and
                rm2.starting_date == datetime(2019, 2, 15).date() and
                rm2.ending_date == datetime(2019, 2, 25).date() and
                rm1.starting_date == datetime(2019, 2, 13).date() and
                rm1.ending_date == datetime(2019, 2, 13).date() and
                rm5.starting_date == datetime(2019, 2, 14).date() and
                rm5.ending_date == datetime(2019, 2, 14).date())


class TestAssignateDatabse(object):

    def build_db_1(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'total_workshift_days': 8,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 1, 26).date(),
                'ending_date': datetime(2019, 1, 30).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        return assignation_db

    def build_db_2(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'total_workshift_days': 8,
                'start_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 1, 26).date(),
                'ending_date': datetime(2019, 1, 30).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 7
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        return assignation_db

    def test_assignate1(self):
        db_obj = self.build_db_1()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 21).date(),
                'ending_date': datetime(2019, 1, 29).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        rm = db_obj.db['4_1'][0].range_mapper
        assert (len(db_obj.db['4_1']) == 1 and
                rm.starting_date == datetime(2019, 1, 1).date() and
                rm.ending_date == datetime(2019, 1, 30).date() and
                len(db_obj.to_be_deleted) == 1 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 0)

    def test_assignate2(self):
        db_obj = self.build_db_1()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 24).date(),
                'ending_date': datetime(2019, 1, 24).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        assert (len(db_obj.db['4_1']) == 3 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 0 and
                len(db_obj.to_be_created) == 1)

    def test_assignate3(self):
        db_obj = self.build_db_1()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 24).date(),
                'ending_date': datetime(2019, 1, 25).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 0)

    def test_assignate4(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 23).date(),
                'ending_date': datetime(2019, 1, 30).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 7
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 0)

    def test_assignate5(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 23).date(),
                'ending_date': datetime(2019, 1, 30).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 6
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        assert (len(db_obj.db['4_1']) == 3 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 0 and
                len(db_obj.to_be_created) == 1)

    def test_assignate6(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 25).date(),
                'ending_date': datetime(2019, 1, 25).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 6
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 0)

    def test_assignate7(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 23).date(),
                'ending_date': datetime(2019, 1, 23).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 3
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 24).date(),
                'ending_date': datetime(2019, 1, 24).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 4
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        assert (len(db_obj.db['4_1']) == 3 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 0 and
                len(db_obj.to_be_created) == 1)

    def test_assignate8(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 23).date(),
                'ending_date': datetime(2019, 1, 23).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 4
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 24).date(),
                'ending_date': datetime(2019, 1, 25).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 5
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.assignate(assign)

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 0)


class TestUnassignDatabse(object):

    def build_db_1(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'total_workshift_days': 8,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 1, 26).date(),
                'ending_date': datetime(2019, 1, 30).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        return assignation_db

    def build_db_2(self):
        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 22).date(),
                'workshift_id': 4,
                'person_id': 1,
                'total_workshift_days': 8,
                'start_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign1 = create_an_assignation(data)

        data = {
            'assignation': {
                'id': 2,
                'starting_date': datetime(2019, 1, 26).date(),
                'ending_date': datetime(2019, 1, 30).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 7
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]

        assignation_db = AssignationDB(assignations, None)
        return assignation_db

    def test_unassign1(self):
        db_obj = self.build_db_1()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 26).date(),
                'ending_date': datetime(2019, 1, 26).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        rm = db_obj.to_be_updated[0].range_mapper
        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 0 and
                rm.starting_date == datetime(2019, 1, 27).date() and
                rm.ending_date == datetime(2019, 1, 30).date())

    def test_unassign2(self):
        db_obj = self.build_db_1()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 20).date(),
                'ending_date': datetime(2019, 1, 28).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        rm1 = db_obj.to_be_updated[0].range_mapper
        rm2 = db_obj.to_be_updated[1].range_mapper
        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 2 and
                len(db_obj.to_be_created) == 0 and
                rm1.starting_date == datetime(2019, 1, 1).date() and
                rm1.ending_date == datetime(2019, 1, 19).date() and
                rm2.starting_date == datetime(2019, 1, 29).date() and
                rm2.ending_date == datetime(2019, 1, 30).date())

    def test_unassign3(self):
        db_obj = self.build_db_1()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 26).date(),
                'ending_date': datetime(2019, 1, 30).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        rm = db_obj.to_be_deleted[0].range_mapper

        assert (len(db_obj.db['4_1']) == 1 and
                len(db_obj.to_be_deleted) == 1 and
                len(db_obj.to_be_updated) == 0 and
                len(db_obj.to_be_created) == 0 and
                rm.starting_date == datetime(2019, 1, 26).date() and
                rm.ending_date == datetime(2019, 1, 30).date())

    def test_unassign4(self):
        db_obj = self.build_db_1()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 24).date(),
                'ending_date': datetime(2019, 1, 24).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 0 and
                len(db_obj.to_be_created) == 0)

    def test_unassign5(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 26).date(),
                'ending_date': datetime(2019, 1, 29).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 1
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 0 and
                len(db_obj.to_be_created) == 0)

    def test_unassign6(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 23).date(),
                'ending_date': datetime(2019, 1, 29).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 4
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        rm = db_obj.to_be_updated[0].range_mapper

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 0 and
                rm.starting_date == datetime(2019, 1, 30).date() and
                rm.ending_date == datetime(2019, 1, 30).date())

    def test_unassign7(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 29).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 2
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        rm = db_obj.to_be_updated[0].range_mapper

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 0 and
                rm.starting_date == datetime(2019, 1, 1).date() and
                rm.ending_date == datetime(2019, 1, 9).date())

    def test_unassign8(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 10).date(),
                'ending_date': datetime(2019, 1, 29).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 5
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        assert (len(db_obj.db['4_1']) == 2 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 0 and
                len(db_obj.to_be_created) == 0)

    def test_unassign9(self):
        db_obj = self.build_db_2()

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 27).date(),
                'ending_date': datetime(2019, 1, 27).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 8
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        data = {
            'assignation': {
                'id': None,
                'starting_date': datetime(2019, 1, 29).date(),
                'ending_date': datetime(2019, 1, 29).date(),
                'workshift_id': 4,
                'person_id': 1,
                'start_day': 2
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign = create_an_assignation(data)
        db_obj.unassign(assign)

        assert (len(db_obj.db['4_1']) == 4 and
                len(db_obj.to_be_deleted) == 0 and
                len(db_obj.to_be_updated) == 1 and
                len(db_obj.to_be_created) == 2)
