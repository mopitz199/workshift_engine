from datetime import datetime

from operators.differences_operator import DifferencesOperator
from database.assignation_db import AssignationDB
from test_utils.utils import create_an_assignation


class TestDifferencesOperatorGetAllDbDifferenceRanges(object):
    """Class to test if the assignation mapper add method works well"""
    
    """
    def test_get_all_db_difference_ranges1(self):

        data = {
            'assignation': {
                'id': 1,
                'starting_date': datetime(2019, 2, 1).date(),
                'ending_date': datetime(2019, 2, 7).date(),
                'workshift_id': 6,
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
                'starting_date': datetime(2019, 2, 11).date(),
                'ending_date': datetime(2019, 2, 16).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign2 = create_an_assignation(data)

        assignations = [assign1, assign2]
        assignation_db = AssignationDB(assignations, None)

        data = {
            'assignation': {
                'starting_date': datetime(2019, 2, 8).date(),
                'ending_date': datetime(2019, 2, 12).date(),
                'workshift_id': 6,
                'person_id': 1,
                'start_day': None
            },
            'workshift': {
                'total_workshift_days': 8,
            }}
        assign3 = create_an_assignation(data)
        assignation_db.assignate(assign3)

        differences_operator = DifferencesOperator(assignation_db)
        ranges = differences_operator.get_all_db_difference_ranges()

        import pdb; pdb.set_trace()

        assert len(ranges) == 1
    """