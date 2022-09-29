import dataclasses
import datetime
from enum import Enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin

from .infant_fee import InfantFee
from .passenger_travel_document import PassengerTravelDocument, Gender
from .name import Name



@dataclasses.dataclass
class PassengerInfant(FromDictMixin):
    fees: List[InfantFee] = dataclasses.field(default_factory=list)
    nationality: str = None
    date_of_birth: str = None
    travel_documents: List[PassengerTravelDocument] = dataclasses.field(default_factory=list)
    resident_country: str = None
    gender: Gender = Gender.MALE
    name: Name = None

    def get_full_name(self):
        names = [p.capitalize() for p in self.name.first.split(" ")]
        name = "".join(names)
        lasts = [p.capitalize() for p in self.name.last.split(" ")]
        last = "".join(lasts)
        return f"{name} {last}"