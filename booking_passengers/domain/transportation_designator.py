import dataclasses
import datetime
from enum import Enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin



@dataclasses.dataclass
class TransportationDesignator(FromDictMixin):
    destination: str = None
    origin: str = None
    destination_name: str = None
    origin_name: str = None
    arrival: datetime.datetime = None
    departure: datetime.datetime = None
