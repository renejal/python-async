import dataclasses
from typing import List

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class AvFee(FromDictMixin):
    fee_code: str = None
    name: str = None

@dataclasses.dataclass
class AvFees(FromDictMixin):
    data: List[AvFee] = dataclasses.field(default_factory=list)
