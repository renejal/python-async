import dataclasses
import datetime
import enum

from utils.dataclass_classmethods import FromDictMixin
from .channel_type import ChannelType

class BookingStatus(enum.Enum):
    DEFAULT = 0
    HOLD = enum.auto()
    CONFIRMED = enum.auto()
    CLOSED = enum.auto()
    HOLD_CANCELED = enum.auto()
    PENDING_ARCHIVE = enum.auto()
    ARCHIVED = enum.auto()

class PaidStatus(enum.Enum):
    UNDER_PAID = 0
    PAID_IN_FULL = enum.auto()
    OVER_PAID = enum.auto()

class PriceStatus(enum.Enum):
    INVALID = 0
    OVERRIDE = enum.auto()
    VALID = enum.auto()

class ProfileStatus(enum.Enum):
    DEFAULT = 0
    KNOWN_INDIVIDUAL = enum.auto()
    RESOLUTION_GROUP = enum.auto()
    SELECTEE_GROUP = enum.auto()
    NOT_USED = enum.auto()
    FAILURE_GROUP = enum.auto()
    RANDOM_SELECTEE = enum.auto()
    EXEMPT = enum.auto()

@dataclasses.dataclass
class BookingInfo(FromDictMixin):
    status: BookingStatus = None
    paid_status: PaidStatus = None
    price_status: PriceStatus = None
    profile_status: ProfileStatus = None
    booking_Type: str = None
    channel_type: ChannelType = None
    booked_date: datetime.datetime = None
    created_date: datetime.datetime = None
    expiration_date: datetime.datetime = None
    modified_date: datetime.datetime = None
    modified_agent_id: int = 0
    created_agent_id: int = 0
    owning_carrier_code: str = None
    change_allowed: bool = False