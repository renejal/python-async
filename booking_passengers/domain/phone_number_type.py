import dataclasses
import enum
from typing import List

class PhoneNumberType(enum.Enum):
    OTHER = 0
    HOME = enum.auto()
    WORK = enum.auto()
    MOBILE = enum.auto()
    FAX = enum.auto()