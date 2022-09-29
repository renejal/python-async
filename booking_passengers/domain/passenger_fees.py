import dataclasses
from typing import List

from utils.dataclass_classmethods import FromDictMixin

from .passenger_fee import PassengerFee

@dataclasses.dataclass
class PassengerFees(FromDictMixin):
    data: List[PassengerFee] = dataclasses.field(default_factory=list)