import dataclasses
import enum
import datetime
from typing import Dict, List


from utils.dataclass_classmethods import FromDictMixin

class SimpleSeatPreference(enum.Enum):
    NONE = 0
    WINDOW = enum.auto()
    AISLE = enum.auto()
    OTHER = enum.auto()

class TravelClass(enum.Enum):
    NONE = 0
    BUSINESS = enum.auto()
    ECONOMY = enum.auto()
    FIRST_CLASS = enum.auto()

@dataclasses.dataclass
class SeatPreference(FromDictMixin):
    seat_map_code: str
    value: str

@dataclasses.dataclass
class SeatPreferences(FromDictMixin):
    seat: SimpleSeatPreference = SimpleSeatPreference.NONE
    travel_class: TravelClass = TravelClass.NONE
    advanced_preferences: List[SeatPreference] = dataclasses.field(default_factory=list)