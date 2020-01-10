from typing import Any, List

from database.generic_database import DB
from proxies.day_off_assignation_proxy import DayOffAssignationProxy


class DayOffAssignationDB(DB):

    def hash_function(
        self,
        element: DayOffAssignationProxy
    ) -> str:
        return "{}".format(element.person_id)

    def get_by_person_id(
        self,
        person_id: int
    ) -> List[DayOffAssignationProxy]:
        hash_str = "{}".format(person_id)
        day_off_assignations = self.db.get(hash_str, [])
        return day_off_assignations
