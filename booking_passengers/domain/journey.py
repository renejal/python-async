import dataclasses
from enum import Enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin
import datetime
import pytz

from .transportation_designator import TransportationDesignator
from .journey_move import JourneyMove
from .booking_segment import Segment


class FlightType(Enum):
    NONE = 0
    NON_STOP = 1
    THROUGH = 2
    DIRECT = 3
    CONNECT = 4
    ALL = 5


@dataclasses.dataclass
class Journey(FromDictMixin):
    flight_type: FlightType = None
    stops: int = 0
    designator: TransportationDesignator = None
    move: JourneyMove = None
    segments: List[Segment] = dataclasses.field(default_factory=list)
    journey_key: str = None
    not_for_general_user: bool = False

    def is_within_24h(self):
        for segment in self.segments:
            now_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
            for leg in segment.legs:
                departure_utc = leg.leg_info.departure_time_utc
                # departure = datetime.datetime.strptime(segment.designator.departure, "%Y-%m-%dT%H:%M:%S")
                time_until_segment = (departure_utc - now_utc).total_seconds() / (60 * 60)
                if time_until_segment < 24:
                    return time_until_segment < 24
        return False

    def get_iata_journey(self):
        return "|".join(map(
            lambda segment: segment.get_iata_segment(),
            self.segments
        ))
