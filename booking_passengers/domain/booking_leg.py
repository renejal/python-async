import dataclasses
import datetime
from enum import Enum
from typing import List, Dict

from utils.dataclass_classmethods import FromDictMixin

from .transportation_designator import TransportationDesignator
from .operations_information import OperationsInformation
from .leg_information import LegInformation
from .leg_nest import LegNest
from .leg_ssr import LegSSR


@dataclasses.dataclass
class Leg(FromDictMixin):
    leg_key: str = None
    operations_info: OperationsInformation = None
    designator: TransportationDesignator = None
    leg_info: LegInformation = None
    nests: List[LegNest] = dataclasses.field(default_factory=list)
    ssrs: List[LegSSR] = dataclasses.field(default_factory=list)
    seatmap_reference: str = None
    flight_reference: str = None
