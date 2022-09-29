import dataclasses
import datetime
import enum
from typing import List, Dict

from utils.dataclass_classmethods import FromDictMixin

from .leg_class import LegClass


class NestType(enum.Enum):
    DEFAULT = 0
    NET = enum.auto()
    SERIAL = enum.auto()
    ONE_BOOKING = enum.auto()


@dataclasses.dataclass
class LegNest(FromDictMixin):
    adjusted_capacity: int = 0
    class_nest: int = 0
    lid: int = 0
    travel_class_code: str = None
    nest_type: NestType = NestType.DEFAULT
    leg_classes: List[LegClass] = dataclasses.field(default_factory=list)