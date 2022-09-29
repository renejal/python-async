import dataclasses
from enum import Enum

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class PassengerProgram(FromDictMixin):
    code: str = None
    level_code: str = None
    number: str = None