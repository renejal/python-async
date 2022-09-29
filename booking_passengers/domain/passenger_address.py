import dataclasses
import datetime
import enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin

from .passenger_travel_document import Gender

class AddressStatus(enum.Enum):
    RESIDENCE = 0
    IN_COUNTRY = enum.auto()
    EMERGENCY = enum.auto()
    CONTACT = enum.auto()

@dataclasses.dataclass
class PassengerAddress(FromDictMixin):
    status: AddressStatus = AddressStatus.RESIDENCE
    company_name: str = None
    line_one: str = None
    passenger_address_key: str = None
    phone: str = None
    line_two: str = None
    station_code: str = None
    line_three: str = None
    email_address: str = None
    country_code: str = None
    culture_code: str = None
    province_state: str = None
    refused_contact: bool = False
    city: str = None
    postal_code: str = None