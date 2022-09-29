import dataclasses

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class JourneyPriceBreakdown(FromDictMixin):
    journey_key: str = None
    total_amount: float = 0
    total_points: float = 0
    total_tax: float = 0
    total_discount: float = 0