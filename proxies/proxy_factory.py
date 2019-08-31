from proxies.assignation_proxy import AssignationProxy


class ProxyFactory(object):

    @staticmethod
    def create_assignation_mapper(obj):
        assignation_mapper = AssignationProxy(obj)
        return assignation_mapper

    @staticmethod
    def create_multiple_assignation_mappers(obj_list):
        resp = []
        for obj in obj_list:
            mapper = ProxyFactory.create_assignation_mapper(obj)
            resp.append(mapper)
        return resp
