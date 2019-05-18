from mappers.workshift_mapper import WorkshiftMapper
from mappers.person_mapper import PersonMapper
from mappers.assignation_mapper import AssignationMapper

from mappers.mapper_factory import FactoryMapper


class DumbAssignation(object):

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)


class DumbWorkshift(object):

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)


class DumbPerson(object):

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)


def build_conf(data):
    resp = {}
    for model_name in data:
        resp[model_name] = {key: key for key in data[model_name].keys()}
    resp['assignation']['workshift_obj'] = 'workshift'
    resp['assignation']['person_obj'] = 'person'
    return resp


def create_an_assignation(data):
    conf = build_conf(data)

    assignation_data = data.get('assignation')
    assignation = DumbAssignation(**assignation_data)

    workshift_data = data.get('workshift', {})
    assignation.workshift = DumbWorkshift(**workshift_data)

    person_data = data.get('person', {})
    assignation.person = DumbPerson(**person_data)

    factory_mapper = FactoryMapper()
    return factory_mapper.create_assignation_mapper(assignation, conf)
