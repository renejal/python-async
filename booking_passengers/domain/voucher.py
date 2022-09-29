import dataclasses
from typing import List
from datetime import datetime
from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class Voucher(FromDictMixin):
    calculated_amount: int = 0
    foreign_currency_code: str = None
    voucher_key: str = None
    expiration: datetime = None
    currency_code: str = None
    customer_number: str = None
    foreign_amount: float = 0
    reference: str = None
    amount: float = 0
    foreign_calculated_amount: float = 0
    type: int = 0
    configuration_code: str = None
    foreign_calculateded_currencyCode: str = None
    password: str = None
    status: int = 0
    foreign_reversable_amount: float = 0
    record_locator: str = None
    available: float = 0
    name_restriction: int = 0
    transactions: List[dict] = dataclasses.field(default_factory=list)
    first_name: str = None
    redeemable_amount: float = 0
    last_name: str = None
    reversable_amount: float = 0
    person_key: str = None
    foreign_available_currency_code: str = None
    voucher_issuance_key: str = None
