import dataclasses
import datetime
import enum
from typing import List, Dict


from utils.dataclass_classmethods import FromDictMixin

class CodeShareIndicator(enum.Enum):
    NON_CODE_SHARE = 0
    CODE_SHARE_COMMERCIAL_DUPLICATE = enum.auto()
    SHARED_DESIGNATOR_OR_WET_LEASE = enum.auto()
    CODE_SHARE_HOST_OPERATING_CARRIER = enum.auto()
    CODE_SHARE_COMMERCIAL_DUPLICATE_WITH_OVERRIDE_TEXT = enum.auto()
    SHARED_DESIGNATOR_OR_WET_LEASE_WITH_OVERRIDE_TEXT = enum.auto()


class LegStatus(enum.Enum):
    NORMAL = 0
    CLOSED = enum.auto()
    CANCELED = enum.auto()
    SUSPENDED = enum.auto()
    CLOSED_PENDING = enum.auto()
    BLOCK_ALL_ACTIVITIES = enum.auto()
    MISHAP = enum.auto()


@dataclasses.dataclass
class LegInformation(FromDictMixin):
    departure_time_utc: datetime.datetime = None
    arrival_time_utc: datetime.datetime = None
    adjusted_capacity: int = 0
    arrival_terminal: str = None
    arrival_time_variant: int = 0
    back_move_days: int = 0
    capacity: int = 0
    change_of_direction: bool = False
    code_share_indicator: CodeShareIndicator = CodeShareIndicator.NON_CODE_SHARE
    departure_terminal: str = None
    departure_time_variant: int = 0
    equipment_type: str = None
    equipment_type_suffix: str = None
    e_ticket: bool = False
    irop: bool = False
    lid: int = 0
    marketing_code: str = None
    marketing_override: bool = False
    operated_by_text: str = None
    operating_carrier: str = None
    operating_flight_number: str = None
    operating_op_suffix: str = None
    out_move_days: int = 0
    arrival_time: str = None
    departure_time: str = None
    prbc_code: str = None
    schedule_service_type: str = None
    sold: int = 0
    status: LegStatus = LegStatus.NORMAL
    subject_to_govt_approval: bool = False