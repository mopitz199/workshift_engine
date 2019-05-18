from workshift_engine.mappers.workshift_mapper import WorkshiftMapper
from workshift_engine.mappers.assignation_mapper import AssignationMapper
from workshift_engine.mappers.person_mapper import PersonMapper


class FactoryMapper(object):

    def create_workshift_mapper(self, obj, conf):
        print obj
        print conf
        print "----------"
        return WorkshiftMapper(obj, conf.get('workshift', {}))

    def create_person_mapper(self, obj, conf):
        print obj
        print conf
        print "----------"
        return PersonMapper(obj, conf.get('person', {}))

    def create_assignation_mapper(self, obj, conf):
        assignation_mapper = AssignationMapper(obj, conf.get('assignation'))
        assignation_mapper.workshift_mapper = self.create_workshift_mapper(
            assignation_mapper.workshift_obj,
            conf.get('workshift', {})
        )
        assignation_mapper.person_mapper = self.create_person_mapper(
            assignation_mapper.person_obj,
            conf.get('person', {})
        )
        return assignation_mapper
