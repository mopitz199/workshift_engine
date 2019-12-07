from typing import Dict, List, NewType, Any, Tuple

from proxies.assignation_proxy import AssignationProxy


ProxyAssignationByHashType = NewType(
    'ProxyAssignationByHashType',
    Dict[str, List[AssignationProxy]]
)
