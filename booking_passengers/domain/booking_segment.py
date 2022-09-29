import dataclasses
import datetime
from enum import Enum
from typing import List, Dict


from utils.dataclass_classmethods import FromDictMixin


from .transportation_designator import TransportationDesignator
from .booking_fare import Fare
from .transportation_identifier import TransportationIdentifier
from .booking_passenger_segment import PassengerSegment
from .booking_leg import Leg
from .channel_type import ChannelType


class ChangeReasonCode(Enum):
    NO_CHANGE = 0
    IROP = 1
    SCHEDULE_CHANGE = 2
    MOVE = 3
    VOLUNTARY_FLY_AHEAD = 4
    INVOLUNTARY_FLY_AHEAD = 5
    SELF_SERVICE_REBOOKING = 6


class SegmentType(Enum):
    NORMAL = 0
    CODE_SHARE_OPERATING = 1
    CODE_SHARE_MARKETING = 2
    INTERLINE_OUTBOUND = 3
    INTERLINE_INBOUND = 4
    PASSIVE = 5


@dataclasses.dataclass
class Segment(FromDictMixin):
    is_standby: bool = False
    is_confirming: bool = False
    is_confirming_external: bool = False
    is_blocked: bool = False
    is_hosted: bool = False
    is_change_of_gauge: bool = False
    designator: TransportationDesignator = None
    is_seatmap_viewable: bool = False
    fares: List[Fare] = dataclasses.field(default_factory=list)
    segment_key: str = None
    identifier: TransportationIdentifier = None
    passenger_segment: Dict[str, PassengerSegment] = dataclasses.field(
        default_factory=dict)
    channel_type: ChannelType = None
    cabin_of_service: str = None
    external_identifier: TransportationIdentifier = None
    priority_code: str = None
    change_reason_code: ChangeReasonCode = None
    segment_type: SegmentType = None
    sales_date: datetime.datetime = None
    international: bool = False
    flight_reference: str = None
    legs: List[Leg] = dataclasses.field(default_factory=list)

    def get_carrier_code_name(self):
        if self.identifier.carrier_code == "VH":
            return "FAST COLOMBIA S.A.S"
        elif self.identifier.carrier_code == "VV":
            return "Viva Air Peru"
        return ""

    def get_iata_segment(self):
        return f"{self.designator.origin}-{self.designator.destination}"
