from datetime import datetime, timedelta


class ManualAssignationFacade():

    def __init__(self, assignation):
        self.assignation = assignation

    def get_days(self):
        return self.assignation.workshift_proxy.get_days()
