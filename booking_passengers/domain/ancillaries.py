import dataclasses
from typing import Dict, List

from .passenger_fee import PassengerFee
from .journey import Journey

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class Ancillary(FromDictMixin):
    changed_journeys: List[Journey] = dataclasses.field(default_factory=dict)
    fees: List[PassengerFee] = dataclasses.field(default_factory=dict)
