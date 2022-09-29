import dataclasses
from typing import Dict, List
import datetime

from utils.dataclass_classmethods import FromDictMixin

from .name import Name


@dataclasses.dataclass
class BookingReservation(FromDictMixin):
    booking_key: str = None
    flight_date : datetime.date = None
    flight_number: str = None
    booking_status: str = None
    origin: str = None
    destination: str = None
    record_locator: str = None
    name: Name = None
    
    def is_commited(self):
        return self.record_locator and self.booking_key

