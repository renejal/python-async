import dataclasses
import datetime
from enum import Enum
from typing import List, Dict

from utils.dataclass_classmethods import FromDictMixin


from .booking_passenger_fare import PassengerFare

class FareApplicationType(Enum):
    ROUTE = 0
    SECTOR = 1
    GOVERNING = 2

class InBoundOutBound(Enum):
    NONE = 0
    IN_BOUND = 1
    OUT_BOUND = 2
    BOTH = 3
    ROUND_FROM = 4
    ROUND_TO = 5

class FareStatus(Enum):
    DEFAULT = 0
    SAME_DAY_STANDBY = 1
    FARE_OVERRIDE_CONFIRMING = 2
    FARE_OVERRIDE_CONFIRMED = 3
    PUBLISHED_FARE_OVERRIDE_CONFIRMING = 4
    PUBLISHED_FARE_OVERRIDE_CONFIRMED = 5


@dataclasses.dataclass
class Fare(FromDictMixin):
    is_governing: bool= False
    downgrade_available: bool = False
    carrier_code: str = None
    fare_key: str = None
    class_of_service: str = None
    class_type: str = None
    fare_application_type: str = None
    fare_class_of_service: str = None
    fare_basis_code: str = None
    fare_sequence: int = 0
    inbound_out_bound: InBoundOutBound = InBoundOutBound.NONE
    fare_status: FareStatus = FareStatus.DEFAULT
    is_allotment_market_fare: bool = False
    original_class_of_service: str = None
    rule_number: str = None
    product_class: str = None
    rule_tariff: str = None
    travel_class_code: str = None
    cross_reference_class_of_service: str = None
    passenger_fares: List[PassengerFare] = dataclasses.field(default_factory=list)
    fare_link: int = 0