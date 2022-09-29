import dataclasses
import enum
from typing import Dict
import datetime

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class PaymentAmounts(FromDictMixin):
    amount: float = None
    currency_code: str = None
    collected: float = None
    collected_currency_code: str = None
    quoted: float = None
    quoted_currency_code: str = None
