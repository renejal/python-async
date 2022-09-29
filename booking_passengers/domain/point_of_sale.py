import dataclasses
from enum import Enum
from typing import List
import datetime


from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class PointOfSale(FromDictMixin):
    agent_code: str = None
    domain_code: str = None
    location_code: str = None
    organization_code: str = None