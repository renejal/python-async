import dataclasses
import datetime
import enum
from typing import List, Dict

from utils.dataclass_classmethods import FromDictMixin

from .gate_information import GateInformation
from .departure_event import DepartureEvent


class ArrivalStatus(enum.Enum):
    DEFAULT = 0
    CANCELLED = enum.auto()
    ARRIVED = enum.auto()
    SEE_AGENT = enum.auto()
    DELAYED = enum.auto()


class DepartureStatus(enum.Enum):
    DEFAULT = 0
    CANCELLED = enum.auto()
    BOARDING = enum.auto()
    SEE_AGENT = enum.auto()
    DELAYED = enum.auto()
    DEPARTED = enum.auto()


@dataclasses.dataclass
class OperationsInformation(FromDictMixin):
    arrival_gate: GateInformation = None
    estimated_arrival_time: str = None
    departure_gate: GateInformation = None
    actual_off_block_time: str = None
    actual_on_block_time: str = None
    actual_touch_down_time: str = None
    airborne_time: str = None
    arrival_note: str = None
    arrival_status: ArrivalStatus = ArrivalStatus.DEFAULT
    baggage_claim: str = None
    departure_note: str = None
    departure_status: DepartureStatus = DepartureStatus.DEFAULT
    departure_times: DepartureEvent = None
    standard_arrival_time: str = None
    tail_number: str = None