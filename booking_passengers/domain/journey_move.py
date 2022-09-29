import dataclasses
from enum import Enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class JourneyMove(FromDictMixin):
    max_move_back_days: int = 0
    max_move_out_days: int = 0