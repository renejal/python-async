import dataclasses
from typing import List

from utils.dataclass_classmethods import FromDictMixin
from .service_charge import ServiceCharge


@dataclasses.dataclass
class ChargeBreakdown(FromDictMixin):
    total: float = 0
    taxes: float = 0
    adjustments: float = 0
    charges: List[ServiceCharge] = dataclasses.field(default_factory=list)