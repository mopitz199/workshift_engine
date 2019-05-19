from mappers.workshift_mapper import WorkshiftMapper
from mappers.assignation_mapper import AssignationMapper
from mappers.person_mapper import PersonMapper


class FactoryMapper(object):

    @staticmethod
    def create_workshift_mapper(obj):
        print(obj)
        print("----------")
        return WorkshiftMapper(obj)

    @staticmethod
    def create_person_mapper(obj):
        print(obj)
        print("----------")
        return PersonMapper(obj)

    @staticmethod
    def create_assignation_mapper(obj):
        assignation_mapper = AssignationMapper(obj)
        return assignation_mapper
