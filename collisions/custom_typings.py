from typing import Dict, List, NewType, Any, Tuple

CToWCollisionType = NewType('CToWCollisionType', Dict[str, Dict])
CToWResolverType = NewType('CToWResolverType', Tuple[bool, CToWCollisionType])

CToMCollisionType = NewType('CToMCollisionType', Dict[str, List])
CToMResolverType = NewType('CToMResolverType', Tuple[bool, CToMCollisionType])
