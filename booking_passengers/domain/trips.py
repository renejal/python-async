import dataclasses
import datetime
from enum import Enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin
from domain.receipt.journey_available import Journey

@dataclasses.dataclass
class TripInformationJourney(FromDictMixin):
    origin: str = None
    destination: str = None
    journeys_available: List[Journey] = dataclasses.field(default_factory=list)

@dataclasses.dataclass
class Trips(FromDictMixin):
    trips: List[TripInformationJourney] = dataclasses.field(default_factory=list)