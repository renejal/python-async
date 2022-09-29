import dataclasses
import datetime
from typing import List

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class Message(FromDictMixin):
    created_date: datetime.datetime
    type: str = ""
    message: str = ""


@dataclasses.dataclass
class Messages(FromDictMixin):
    data: List[Message] = dataclasses.field(default_factory=list)
