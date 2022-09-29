import dataclasses
import enum
from typing import Dict
import datetime

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class PaymentDetails(FromDictMixin):
    account_number_id: int = 0
    parent_payment_id: int = None
    account_name: str = None
    account_number: str = None
    expiration_date: str = None
    text: str = None
    installments: int = 0
    bin_range: int = 0
    fields: Dict[str, str] = dataclasses.field(default_factory=dict)
