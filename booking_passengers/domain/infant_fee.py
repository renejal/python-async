import dataclasses
from enum import Enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin

from .service_charge import ServiceCharge

@dataclasses.dataclass
class InfantFee(FromDictMixin):
    is_confirmed: bool = False
    code: str = None
    detail: str = None
    passenger_fee_key: str = None
    override: bool = False
    flight_reference: str = None
    note: str = None
    created_date: str = None
    is_protected: bool = False
    service_charges: List[ServiceCharge] = dataclasses.field(default_factory=list)