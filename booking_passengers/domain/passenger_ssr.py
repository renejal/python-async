import dataclasses
import enum
import datetime
from typing import Dict, List

from utils.dataclass_classmethods import FromDictMixin

from .market_information import MarketInformation

class SSRDuration(enum.Enum):
    SEGMENT = 0
    JOURNEY = enum.auto()
    LEG = enum.auto()

@dataclasses.dataclass
class PassengerSSR(FromDictMixin):
    is_confirmed: bool = False
    is_confirming_unheld: bool = False
    note: str = None
    ssr_duration: SSRDuration = SSRDuration.SEGMENT
    ssr_key: str = None
    count: int = 0
    ssr_code: str = None
    fee_code: str = None
    in_bundle: bool = False
    passenger_key: str = None
    ssr_detail: str = None
    ssr_number: int = 0
    market: MarketInformation = None