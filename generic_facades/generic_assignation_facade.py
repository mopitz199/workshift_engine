import copy
from datetime import datetime, timedelta


class GenericAssignationFacade():

    def __init__(self, assignation):
        self.assignation = assignation

    def copy(self):
        """
        To create a deep copy of a given assign

        :param assign: An assign proxy object
        :type assign: AssignationProxy

        :rtype: AssignationProxy
        """
        assign = self.assignation
        copied = copy.copy(assign)
        copied.obj = copy.deepcopy(assign.obj)
        copied.range_obj = copy.deepcopy(assign.range_obj)
        copied.workshift = assign.workshift
        copied.person = assign.person
        copied.obj.id = None
        return copied
