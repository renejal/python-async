import dataclasses
import enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin
from .phone_number import PhoneNumber
from .booking_contact_address import Address
from .name import Name

class DistributionOption(enum.Enum):
    NONE = 0
    MAIL = enum.auto()
    EMAIL = enum.auto()
    FAX = enum.auto()
    MAIL_FAX = enum.auto()
    AIRPORT = enum.auto()
    HOLD = enum.auto()
    PRINT = enum.auto()

class NotificationPreference(enum.Enum):
    NONE=0
    PROMOTIONAL=enum.auto()

@dataclasses.dataclass
class Contact(FromDictMixin):
    contact_type_code: str
    phone_numbers: List[PhoneNumber] = dataclasses.field(default_factory=list)
    culture_code: str = None
    address: Address = None
    email_address: str = None
    customer_number: str = None
    source_organization: str = None
    distribution_option: DistributionOption = DistributionOption.NONE
    notification_preference: NotificationPreference = NotificationPreference.NONE
    company_name: str = None
    name : Name = None