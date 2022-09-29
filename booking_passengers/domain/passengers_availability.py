import dataclasses

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class PassengerAvailability(FromDictMixin):
    ssr_key: str
    passenger_key: str
    price: float = 0.0
    include: int = 0