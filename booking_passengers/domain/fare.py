import dataclasses
from typing import Dict, List

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class Fare(FromDictMixin):
    fare_availability_key: str = None
    fare_code: str = None
    available_count: int = 0
    is_sum_of_sector: bool = False
    class_of_service: str = None

@dataclasses.dataclass
class FareType(FromDictMixin):
    type: str = None
    observation: str = None
    amount: int = None

    

