import dataclasses
import enum
from typing import List

from .propierty import Propierty

from utils.dataclass_classmethods import FromDictMixin


class AvailabilityType(enum.Enum):
    UNKNOWN = 0
    RESERVED = enum.auto()
    BLOCKED = enum.auto()
    HELD_FOR_ANOTHER_SESSION = enum.auto()
    HELD_FOR_THIS_SESSION = enum.auto()
    OPEN = enum.auto()
    MISSING = enum.auto()
    CHECKED_IN = enum.auto()
    FLEET_BLOCKED = enum.auto()
    RESTRICTED = enum.auto()
    BROKEN = enum.auto()
    RESERVED_FOR_PNR = enum.auto()
    SOFT_BLOCKED = enum.auto()
    UNAVAILABLE = enum.auto()


class UnitType(enum.Enum):
    UNKNOWN = 0
    NORMAL_SEAT = enum.auto()
    LARGE_SEAT = enum.auto()
    COUCHETTE = enum.auto()
    COMPARTMENT = enum.auto()
    TABLE = enum.auto()
    WALL = enum.auto()
    WINDOW = enum.auto()
    DOOR = enum.auto()
    STAIRS = enum.auto()
    WING = enum.auto()
    OTHER = enum.auto()
    BULKHEAD = enum.auto()
    BED_ONE_OF_THREE = enum.auto()
    BED_TWO_OF_THREE = enum.auto()
    BED_THREE_OF_THREE = enum.auto()
    BED_ONE_OF_TWO = enum.auto()
    BED_TWO_OF_TWO = enum.auto()
    BED = enum.auto()
    EXIT = enum.auto()
    LABEL_RULER = enum.auto()
    GENERIC_UNIT_RESIZABLE_AREA = enum.auto()
    LAVATORY = enum.auto()
    LAVATORY_WITH_HANDI_CAPPED_FACILITIES = enum.auto()
    LUGGAGE = enum.auto()
    MOVABLE_COMPARTMENT_DIVIDER = enum.auto()
    BAR = enum.auto()
    CLOSET = enum.auto()
    GALLERY = enum.auto()
    MOVIE_SCREEN = enum.auto()
    STORAGE = enum.auto()

@dataclasses.dataclass
class ServiceCharges(FromDictMixin):
    amount: float
    code: str
    currency_code: str

    @classmethod
    def from_dict(cls, obj):
        return cls(
            amount = obj['amount'],
            code = obj['code'],
            currency_code=obj['currencyCode']
        )

@dataclasses.dataclass
class Fee(FromDictMixin):
    passenger_key: str
    serviceCharges: List[ServiceCharges]

    @classmethod
    def from_dict(cls, obj):
        return cls(
            passenger_key=obj['passengerKey'],
            serviceCharges=obj['serviceCharges']
        )

@dataclasses.dataclass
class Unit(FromDictMixin):
    unit_key: str = None
    assignable: bool = False
    availability: AvailabilityType = AvailabilityType.UNKNOWN
    designator: str = None
    row: int = None
    column: str = None
    type: UnitType = UnitType.UNKNOWN
    travel_class_code: str = None
    width: int = None
    height: int = None
    x: float = None
    y: float = None
    group: int = None
    zone: int = None
    allow_ssrs: List[str] = dataclasses.field(default_factory=list)
    properties: List[Propierty] = dataclasses.field(default_factory=list)
    fees: List[Fee] = dataclasses.field(default_factory=list)

    @classmethod
    def from_dict(cls, obj):
        obj = super().from_dict(obj)
        obj.x = obj.x / 100
        obj.y = obj.y / 100
        return obj