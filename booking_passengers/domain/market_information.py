import dataclasses
import datetime
import enum
import datetime
from typing import Dict, List

from utils.dataclass_classmethods import FromDictMixin

from .transportation_identifier import TransportationIdentifier

@dataclasses.dataclass
class MarketInformation(FromDictMixin):
    identifier: TransportationIdentifier
    destination: str
    origin: str
    departure_date: datetime.datetime