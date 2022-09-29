import dataclasses
from enum import Enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class TransportationIdentifier(FromDictMixin):
    identifier: str
    carrier_code: str
    op_suffix: str = None