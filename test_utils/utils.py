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


def create_an_assignation(data):

    assignation_data = data.get('assignation')
    assignation = DumbAssignation(**assignation_data)

    workshift_data = data.get('workshift', {})
    days_data = workshift_data.pop('days', [])
    days = []
    for day_data in days_data:
        day = DumbDay(**day_data)
        days.append(day)

    workshift = DumbWorkShift(**workshift_data)
    workshift.days = days
    assignation.workshift = workshift

    person_data = data.get('person', {})
    assignation.person = DumbPerson(**person_data)

    return ProxyFactory.create_assignation_proxy(assignation)
