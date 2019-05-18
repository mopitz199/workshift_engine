from datetime import datetime

from workshift_engine.database.assignation_db import AssignationDB
from workshift_engine.test_utils.utils import create_an_assignation


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
        assignation_db.update(assign1)

        assert (assignation_db.db == {'6_1': [assign1]} and
                assignation_db.to_be_updated == [] and
                assignation_db.to_be_created == [assign1])
