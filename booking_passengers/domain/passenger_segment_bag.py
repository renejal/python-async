import dataclasses
import enum
import datetime
from typing import Dict, List


from utils.dataclass_classmethods import FromDictMixin

class BagStatus(enum.Enum):
    DEFAULT = 0
    CHECKED = enum.auto()
    REMOVED = enum.auto()
    ADDED = enum.auto()
    ADDED_PRINTED = enum.auto()

@dataclasses.dataclass
class PassengerSegmentBag(FromDictMixin):
    passenger_key: str
    departure_station: str
    arrival_station: str
    baggage_key: str = None
    status: BagStatus = BagStatus.DEFAULT
    os_tag: str = None