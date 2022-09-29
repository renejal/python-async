import dataclasses
import datetime
from enum import Enum
from typing import List


from utils.dataclass_classmethods import FromDictMixin

from .service_charge import ServiceCharge

@dataclasses.dataclass()
class PassengerFare(FromDictMixin):
    passenger_type: str
    service_charges: List[ServiceCharge] = dataclasses.field(default_factory=list)
    multiplier: int = 0
    discount_code: str = None
    fare_discount_code: str = None