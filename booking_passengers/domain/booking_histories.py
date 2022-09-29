import dataclasses
from typing import List

from utils.dataclass_classmethods import FromDictMixin

from .booking_history import BookingHistory

@dataclasses.dataclass
class BookingHistories(FromDictMixin):
    histories: List[BookingHistory] = dataclasses.field(default_factory=dict)

