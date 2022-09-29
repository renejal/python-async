import dataclasses
import enum
from typing import Dict, List
import datetime

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class CreditAvailable(FromDictMixin):
    account_reference: str = None
    currency_code: str = None
    amount: float = 0
    foreign_amount: float = 0
    foreign_currency_code: str = None