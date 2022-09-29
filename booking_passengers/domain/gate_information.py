import dataclasses
import datetime
import enum
from typing import List, Dict

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class GateInformation(FromDictMixin):
    estimated_gate: str = None
    actual_gate: str = None