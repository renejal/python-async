import dataclasses
import datetime
from typing import List
from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class TypeOfSale(FromDictMixin):
    resident_country: str = None
    promotion_code: str = None
    fare_types: List[str] = dataclasses.field(default_factory=list)