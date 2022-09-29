import dataclasses
import enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class Address(FromDictMixin):
    line_one: str = None
    line_two: str = None
    line_three: str = None
    country_code: str = None
    province_state: str = None
    city: str = None
    postal_code: str = None
        