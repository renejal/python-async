import dataclasses
import datetime
import enum

from utils.dataclass_classmethods import FromDictMixin

from .name import Name

class Gender(enum.Enum):
    XX = 0
    MALE = enum.auto()
    FEMALE = enum.auto()

@dataclasses.dataclass
class PassengerTravelDocument(FromDictMixin):
    document_type_code: str
    passenger_travel_document_key: str = None
    birth_country: str = None
    issued_by_code: str = None
    name: Name = None
    expiration_date: str = None
    number: str = None
    issued_date: str = None
    gender: Gender = None
    date_of_birth: str = None