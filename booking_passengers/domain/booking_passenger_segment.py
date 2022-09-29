import dataclasses
import enum
import datetime
from typing import Dict, List

from utils.dataclass_classmethods import FromDictMixin

from .weight_type import WeightType
from .point_of_sale import PointOfSale
from .passenger_ssr import PassengerSSR
from .passenger_seat import PassengerSeat
from .ticket import Ticket
from .passenger_segment_bag import PassengerSegmentBag
from .passenger_score import PassengerScore
from .passenger_boarding_pass_detail import PassengerBoardingPassDetail
from .seat_preferences import SeatPreferences

class LiftStatusType(enum.Enum):
    DEFAULT = 0
    CHECKED_IN = enum.auto()
    BOARDED = enum.auto()
    NO_SHOW = enum.auto()

class OverBookIndicator(enum.Enum):
    NORMAL_SELL = 0
    OVERSOLD = enum.auto()
    CLASS_OR_CABIN_OVERSOLD = enum.auto()

@dataclasses.dataclass
class PassengerSegment(FromDictMixin):
    seats: List[PassengerSeat] = dataclasses.field(default_factory=list)
    passenger_key: str = None
    activity_date: str = None
    baggage_allowance_used: bool = None
    baggage_allowance_weight: int = 0
    baggage_allowance_weight_type: WeightType = WeightType.DEFAULT
    boarding_sequence: str = None
    created_date: datetime.datetime = None
    lift_status: LiftStatusType = LiftStatusType.DEFAULT
    modified_date: datetime.datetime = None
    over_book_indicator: OverBookIndicator = OverBookIndicator.NORMAL_SELL
    priority_date: datetime.datetime = None
    time_changed: bool = False
    # verified_travel_docs: str = None # deprecated
    source_point_of_sale: PointOfSale = None
    point_of_sale: PointOfSale = None
    ssrs: List[PassengerSSR] = dataclasses.field(default_factory=list)
    bundle_code: str = None
    tickets: List[Ticket] = dataclasses.field(default_factory=list)
    bags: List[PassengerSegmentBag] = dataclasses.field(default_factory=list)
    scores: List[PassengerScore] = dataclasses.field(default_factory=list)
    boarding_pass_detail: PassengerBoardingPassDetail = None
    has_infant: bool = False
    seat_preferences: SeatPreferences = None
    verified_travel_documents: List[str] = None