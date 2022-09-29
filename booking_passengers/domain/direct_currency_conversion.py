import dataclasses
import enum
from typing import List
import datetime

from utils.dataclass_classmethods import FromDictMixin

class DirectCurrencyConversionStatus(enum.Enum):
    DCC_NOT_OFFERED = 0
    DCC_OFFER_REJECTED = enum.auto()
    DCC_OFFER_ACCEPTED = enum.auto()
    DCC_INITIAL_VALUE = enum.auto()
    MCC_IN_USE = enum.auto()

@dataclasses.dataclass
class DirectCurrencyConversion(FromDictMixin):
    rate_id: str = None
    currency_code: str = None
    rate_ralue: float = None
    amount: float = None
    put_in_state: str = None
    status: DirectCurrencyConversionStatus = DirectCurrencyConversionStatus.DCC_NOT_OFFERED
    applicable: bool = False