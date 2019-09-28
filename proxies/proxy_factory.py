from proxies.assignation_proxy import AssignationProxy
from proxies.workshift_proxy import WorkShiftProxy


class ProxyFactory(object):

    @staticmethod
    def create_assignation_proxy(obj):
        assignation_proxy = AssignationProxy(obj)
        return assignation_proxy

    @staticmethod
    def create_multiple_assignation_proxies(obj_list):
        resp = []
        for obj in obj_list:
            proxy = ProxyFactory.create_assignation_proxy(obj)
            resp.append(proxy)
        return resp
