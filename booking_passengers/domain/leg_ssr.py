import dataclasses
import datetime
from enum import Enum
from typing import List, Dict


from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class LegSSR(FromDictMixin):
    available: int = 0
    ssr_nest_code: str = None
    lid: int = 0
    sold: int = 0
    unit_sold: int = 0
