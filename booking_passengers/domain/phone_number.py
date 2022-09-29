import dataclasses
import enum


from utils.dataclass_classmethods import FromDictMixin
from .phone_number_type import PhoneNumberType


@dataclasses.dataclass
class PhoneNumber(FromDictMixin):
    number: str
    type: PhoneNumberType = None