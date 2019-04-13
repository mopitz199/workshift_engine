from mappers.workshift_mapper import WorkshiftMapper
from mappers.assignation_mapper import AssignationMapper

class DumbAssignation:

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)

class DumbWorkshift:

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            val = kwargs.get(kwarg, None)
            setattr(self, kwarg, val)

def create_an_assignation(data):
    workshift_data = {
        'total_workshift_days': data.pop('total_workshift_days', None)}
    workshift_mapper = create_a_workshift_mapper(workshift_data)
    
    conf = {key:key for key in data.keys()}
    assignation_mapper = AssignationMapper(DumbAssignation(**data), conf)
    assignation_mapper.workshift_obj = workshift_mapper
    return assignation_mapper

def create_a_workshift_mapper(workshift_data):
    workshift = DumbWorkshift(**workshift_data)
    conf = {key:key for key in workshift_data.keys()}
    return WorkshiftMapper(workshift, conf)