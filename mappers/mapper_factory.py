from mappers.assignation_mapper import AssignationMapper


class FactoryMapper(object):

    @staticmethod
    def create_assignation_mapper(obj):
        assignation_mapper = AssignationMapper(obj)
        return assignation_mapper
