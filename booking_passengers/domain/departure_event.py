import dataclasses
import datetime
import enum
from typing import List, Dict

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class DepartureEvent(FromDictMixin):
    scheduled: datetime.datetime = None
    estimated: datetime.datetime = None