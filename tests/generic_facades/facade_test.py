import types
from datetime import datetime

from assignation.operators.assignation_operator import AssignationOperator
from proxies.assignation_proxy import AssignationProxy

from test_utils.utils import create_an_assignation


class TestSimulateStartingDay(object):
    """To test if the function to simulate an start_date from a
    given assign and date works."""

    def test_simulate_starting_day1(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 31).date(),
                'starting_day': 1
            },
            'workshift': {
                'total_workshift_days': 7}}

        assign = create_an_assignation(data)

        date_obj = datetime(2019, 1, 12).date()

        simulated_starting_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 5 == simulated_starting_day

    def test_simulate_starting_day2(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 31).date(),
                'starting_day': 3
            },
            'workshift': {
                'total_workshift_days': 6}}

        assign = create_an_assignation(data)

        date_obj = datetime(2019, 1, 14).date()

        simulated_starting_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 4 == simulated_starting_day

    def test_simulate_starting_day3(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 31).date(),
                'starting_day': 2
            },
            'workshift': {
                'total_workshift_days': 8}}

        assign = create_an_assignation(data)

        date_obj = datetime(2019, 1, 23).date()

        simulated_starting_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 8 == simulated_starting_day

    def test_simulate_starting_day4(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 31).date(),
                'starting_day': 2
            },
            'workshift': {
                'total_workshift_days': 6}}

        assign = create_an_assignation(data)

        date_obj = datetime(2019, 1, 6).date()

        simulated_starting_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 1 == simulated_starting_day

    def test_simulate_starting_day5(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 1).date(),
                'starting_day': 4
            },
            'workshift': {
                'total_workshift_days': 6}}

        assign = create_an_assignation(data)

        date_obj = datetime(2019, 1, 1).date()

        simulated_starting_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert 4 == simulated_starting_day

    def test_simulate_starting_day6(self):
        data = {
            'assignation': {
                'starting_date': datetime(2019, 1, 1).date(),
                'ending_date': datetime(2019, 1, 1).date(),
                'starting_day': None
            },
            'workshift': {
                'total_workshift_days': 6}}

        assign = create_an_assignation(data)

        date_obj = datetime(2019, 1, 1).date()

        simulated_starting_day = AssignationOperator.simulate_starting_day(
            assign, date_obj)

        assert simulated_starting_day is None
