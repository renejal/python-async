from typing import List
import dataclasses
from dotrez.v1.booking_management.utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class Passenger(FromDictMixin):
    last: str = "",
    type_document: str = "",
    document_number: str = "",
    gender: str = "",
    country: str = "",
    expiration_date: str = "",
    email: str = ""
    nacionality: str = "",
    phone: str = "",
    seat: str = "",
    child: str = "",
    infant: str = ""

@dataclasses.dataclass
class PassengerRequest(FromDictMixin):
    passengers: List[Passenger] = dataclasses.field(default_factory=list)

    
