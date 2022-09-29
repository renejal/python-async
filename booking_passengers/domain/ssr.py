import dataclasses

from utils.dataclass_classmethods import FromDictMixin
from typing import Dict

from domain.receipt.passengers_availability import PassengerAvailability

@dataclasses.dataclass
class ExtraIcon(FromDictMixin):
    dimensions: list
    url: str


@dataclasses.dataclass
class Ssr(FromDictMixin):
    ssr_code: str = None
    passengers_availability: Dict[str, PassengerAvailability] = dataclasses.field(default_factory=dict)
    name: str = None
    limit_per_passenger: int = None
    available: int = None
    inventory_controlled: bool = None
    seat_dependent: bool= None
    fee_code: str = None
    nest: str = None
    seat_restriction: str = None
    group: str = None
    order: int = None
    ssr_type: str = None
    extra_icon: ExtraIcon = None

    @classmethod
    def from_dict(cls, obj, page_settings):
        new_object = super().from_dict(obj)
        for ssr in page_settings.ssrs:
            for info in ssr.ssr_info:
                if info.text == new_object.ssr_code:
                    new_object.name = ssr.name
                    new_object.group = ssr.group
                    new_object.order = info.order
                    new_object.ssr_type = ssr.ssr_type
                    new_object.extra_icon = ssr.extra_icon
        # print(page_settings)
        return new_object
