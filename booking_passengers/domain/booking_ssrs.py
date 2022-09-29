import dataclasses
from utils.dataclass_classmethods import FromDictMixin
from domain.receipt.booking_ssr import Ssr
from typing import List

@dataclasses.dataclass
class Ssrs(FromDictMixin):
	data: List[Ssr] = dataclasses.field(default_factory=list)