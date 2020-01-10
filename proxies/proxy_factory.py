from proxies.assignation_proxy import AssignationProxy
from proxies.workshift_proxy import WorkShiftProxy
from proxies.day_off_assignation_proxy import DayOffAssignationProxy


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

    @staticmethod
    def create_workshift_proxy(obj):
        workshift_proxy = WorkShiftProxy(obj)
        return workshift_proxy

    @staticmethod
    def create_multiple_workshift_proxies(obj_list):
        resp = []
        for obj in obj_list:
            proxy = ProxyFactory.create_workshift_proxy(obj)
            resp.append(proxy)
        return resp

    @staticmethod
    def create_day_off_assignation_proxy(obj):
        day_off_assignation = DayOffAssignationProxy(obj)
        return day_off_assignation

    @staticmethod
    def create_multiple_day_off_assignation_proxies(obj_list):
        resp = []
        for obj in obj_list:
            proxy = ProxyFactory.create_day_off_assignation_proxy(obj)
            resp.append(proxy)
        return resp
