import dataclasses

from utils.dataclass_classmethods import FromDictMixin

from .weight_type import WeightType

@dataclasses.dataclass
class PassengerBag(FromDictMixin):
    identifier: str = None
    baggage_key: str = None
    non_standard: bool = False
    type: str = None
    os_tag: str = None
    os_tag_date: str = None
    tagged_to_station: str = None
    station_code: str = None
    weight: int = 0
    tagged_to_carrier_code: str = None
    weight_type: WeightType = None