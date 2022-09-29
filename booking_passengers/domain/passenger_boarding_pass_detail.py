import dataclasses
import enum
import datetime
from typing import Dict, List

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class PassengerBoardingPassDetail(FromDictMixin):
    gate_information: str = None
    priority_information: str = None
    cabin_class: str = None
    compartment_level: str = None
    boarding_zone: str = None
    seat_assignment: str = None
    sequence_number: str = None
    