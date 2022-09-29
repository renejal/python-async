import dataclasses
import enum
from typing import List
import datetime


from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class PaymentVoucherDetails(FromDictMixin):
    id: int = 0
    transaction_id: int = 0
    override_restrictions: bool = False
    override_amount: bool = False
    record_locator: str = None