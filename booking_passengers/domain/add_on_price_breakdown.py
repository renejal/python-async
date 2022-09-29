import dataclasses

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class AddOnPriceBreakdown(FromDictMixin):
    car: float = None
    hotel: float = None
    activities: float = None