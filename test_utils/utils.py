from datetime import datetime

from proxies.assignation_proxy import AssignationProxy
from proxies.proxy_factory import ProxyFactory


class DumbAssignation(object):

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)


class DumbWorkShift(object):

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)

    def get_days(self):
        return getattr(self, 'days')


class DumbPerson(object):

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)


class DumbDay(object):

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)


class DumbDayOffAssignation(object):

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)


def create_an_assignation(
    data,
    workshift_db=None,
    day_off_assignation_db=None
):
    assignation_data = data.get('assignation')

    starting_date_str = assignation_data.get('starting_date')
    starting_date = datetime.strptime(starting_date_str, '%Y-%m-%d').date()
    assignation_data['starting_date'] = starting_date

    ending_date_str = assignation_data.get('ending_date')
    ending_date = datetime.strptime(ending_date_str, '%Y-%m-%d').date()
    assignation_data['ending_date'] = ending_date

    assignation = DumbAssignation(**assignation_data)

    if workshift_db:
        workshift_proxy = workshift_db.get_by_id(assignation.workshift_id)
        assignation.workshift_proxy = workshift_proxy

    if day_off_assignation_db:
        day_off_assignations = day_off_assignation_db.get_by_person_id(
            assignation.person_id
        )
        assignation.day_off_assignations = day_off_assignations

    person_data = data.get('person', {})
    assignation.person = DumbPerson(**person_data)

    return ProxyFactory.create_assignation_proxy(assignation)


def create_proxy_workshifts(workshifts_data):
    dumb_workshifts = []
    for workshift_data in workshifts_data:
        days_data = workshift_data.pop('days', [])
        days = []
        for day_data in days_data:
            day = DumbDay(**day_data)
            days.append(day)

        dumb_workshift = DumbWorkShift(**workshift_data)
        dumb_workshift.days = days
        dumb_workshifts.append(dumb_workshift)

    return ProxyFactory.create_multiple_workshift_proxies(dumb_workshifts)


def create_proxy_day_off_assignation(day_off_assignations_data):
    dumb_day_off_assignations = []
    for day_off_assignation_data in day_off_assignations_data:
        dumb_day_off_assignation = DumbDayOffAssignation(
            **day_off_assignation_data
        )
        dumb_day_off_assignations.append(dumb_day_off_assignation)

    return ProxyFactory.create_multiple_day_off_assignation_proxies(
        dumb_day_off_assignations
    )
