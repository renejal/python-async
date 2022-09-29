import dataclasses
import datetime
import enum
from typing import List, Dict

from utils.dataclass_classmethods import FromDictMixin

class LegClassStatus(enum.Enum):
    ACTIVE = 0
    IN_ACTIVE = enum.auto()
    AVS_OPEN = enum.auto()
    AVS_ON_REQUEST = enum.auto()
    AVS_CLOSED = enum.auto()

@dataclasses.dataclass
class LegClass(FromDictMixin):
    class_of_service: str
    class_nest: int = 0
    class_allotted: int = 0
    class_type: str = None
    class_authorized_units: int = 0
    class_rank: int = 0
    class_sold: int = 0
    cnx_sold: int = 0
    latest_advanced_reservation: int = 0
    status: LegClassStatus= LegClassStatus.ACTIVE
    thru_sold: int = 0
