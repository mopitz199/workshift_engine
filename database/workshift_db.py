from typing import Any, Optional

from database.generic_database import DB
from proxies.workshift_proxy import WorkShiftProxy


class WorkShiftDB(DB):

    def hash_function(
        self,
        element: WorkShiftProxy
    ) -> str:
        return "{}".format(element.id)

    def get_by_id(
        self,
        id: int
    ) -> Optional[WorkShiftProxy]:
        hash_str = "{}".format(id)
        workshifts = self.db.get(hash_str, [])
        if workshifts:
            if len(workshifts) == 1:
                return workshifts[0]
            else:
                raise Exception('Hash key must return one workshift as maximum')
        else:
            return None
