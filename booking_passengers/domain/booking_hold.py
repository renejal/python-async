import dataclasses
import enum
import datetime
from typing import List

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class BookingHold(FromDictMixin):
    expiration: datetime.datetime