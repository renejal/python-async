import dataclasses
import datetime
from enum import Enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin

from .passenger_travel_document import Gender


@dataclasses.dataclass()
class PassengerInformation(FromDictMixin):
    nationality: str = None
    resident_country: str = None
    gender: Gender = Gender.XX
    date_of_birth: datetime.datetime = None
    family_number: int = None
