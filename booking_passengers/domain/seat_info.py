import dataclasses
import enum
import datetime
from typing import Dict, List


from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class SeatInfo(FromDictMixin):
    deck: int = 0
    seat_set: int = 0
    property_list: Dict[str, str] = dataclasses.field(default_factory=dict)