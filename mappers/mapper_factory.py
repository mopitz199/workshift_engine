from mappers.assignation_mapper import AssignationMapper


class FactoryMapper(object):

    @staticmethod
    def create_assignation_mapper(obj):
        assignation_mapper = AssignationMapper(obj)
        return assignation_mapper

    @staticmethod
    def create_multiple_assignation_mappers(obj_list):
        resp = []
        for obj in obj_list:
            mapper = FactoryMapper.create_assignation_mapper(obj)
            resp.append(mapper)
        return resp
