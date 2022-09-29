import dataclasses
from typing import List

from utils.dataclass_classmethods import FromDictMixin

from .fee import Fee

@dataclasses.dataclass
class Fees(FromDictMixin):
    data: List[Fee] = dataclasses.field(default_factory=list)
    

