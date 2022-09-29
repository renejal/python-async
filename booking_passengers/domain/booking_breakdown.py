import dataclasses
from typing import Dict

from utils.dataclass_classmethods import FromDictMixin

from .passenger_price_breakdown_base import PassengerPriceBreakdownBase
from .passenger_price_breakdown import PassengerPriceBreakdown
from .journey_price_breakdown_base import JourneyPriceBreakdownBase
from .journey_price_breakdown import JourneyPriceBreakdown
from .add_on_price_breakdown import AddOnPriceBreakdown

@dataclasses.dataclass
class BookingPriceBreakdown(FromDictMixin):
    balance_due: float = 0
    points_balance_due: float = 0
    authorized_balance_due: float = 0
    total_amount: float = 0
    total_points: float = 0
    total_to_collect: float = 0
    total_points_to_collect: float = 0
    total_charged: float = 0
    passenger_totals: PassengerPriceBreakdownBase = None
    passengers: Dict[str, PassengerPriceBreakdown] = dataclasses.field(default_factory=dict)
    journey_totals: JourneyPriceBreakdownBase = None
    journeys: Dict[str, JourneyPriceBreakdown] = dataclasses.field(default_factory=dict)
    add_on_totals: AddOnPriceBreakdown = None
