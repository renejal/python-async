import dataclasses
import enum
import datetime
from typing import Dict, List

from utils.dataclass_classmethods import FromDictMixin

from .seat_info import SeatInfo
from domain.fee import Fee


@dataclasses.dataclass
class PassengerSeat(FromDictMixin):
    compartment_designator: str = None
    penalty: int = 0
    unit_designator: str = None
    seat_information: SeatInfo = None
    arrival_station: str = None
    departure_station: str = None
    passenger_key: str = None
    unit_key: str = None
    fees: List[Fee] = dataclasses.field(default_factory=list)
