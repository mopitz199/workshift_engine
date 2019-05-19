from mappers.workshift_mapper import WorkshiftMapper
from mappers.assignation_mapper import AssignationMapper
from mappers.person_mapper import PersonMapper


class FactoryMapper(object):

    @staticmethod
    def create_workshift_mapper(obj, conf):
        print(obj)
        print(conf)
        print("----------")
        return WorkshiftMapper(obj, conf.get('workshift', {}))

    @staticmethod
    def create_person_mapper(obj, conf):
        print(obj)
        print(conf)
        print("----------")
        return PersonMapper(obj, conf.get('person', {}))

    @staticmethod
    def create_assignation_mapper(obj, conf):
        assignation_mapper = AssignationMapper(obj, conf.get('assignation'))
        workshift_mapper = FactoryMapper.create_workshift_mapper(
            assignation_mapper.workshift_obj,
            conf.get('workshift', {})
        )
        assignation_mapper.workshift_mapper = workshift_mapper

        person_mapper = FactoryMapper.create_person_mapper(
            assignation_mapper.person_obj,
            conf.get('person', {})
        )
        assignation_mapper.person_mapper = person_mapper
        return assignation_mapper
