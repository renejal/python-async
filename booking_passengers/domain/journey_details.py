import dataclasses

from utils.dataclass_classmethods import FromDictMixin
from .journey_identifier import JourneyIdentifier


@dataclasses.dataclass
class JourneyDetails(FromDictMixin):
    identifier: JourneyIdentifier
    destination: str
    origin: str
    departure_date: str
