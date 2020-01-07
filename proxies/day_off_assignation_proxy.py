import copy

from datetime import timedelta

from database.db_extension import DBExtension
from proxies.base_proxy import Proxy
from utils.range import Range


class DayOffAssignationProxy(Proxy, DBExtension):

    def __init__(self, obj, *args, **kwargs):
        super(DayOffAssignationProxy, self).__init__(obj)
