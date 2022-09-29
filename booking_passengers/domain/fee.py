import dataclasses

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class Fee(FromDictMixin):
    can_be_manually_added: bool = False
    has_default_fee_price: bool = False
    is_fee_charged_per_segment: bool = False
    allowed: bool = False
    charge_limit: int = 0
    charge_limit_mode: int = 0
    charge_limit_travel_component: int = 0
    commissionable: bool = False
    country_code: str = None
    description: str = None
    display_code: str = None
    fee_application: int = 0
    fee_code: str = None
    fee_option_mode: int = 0
    fee_type: int = 0
    in_active: bool = False
    itemizable: bool = False
    min_stopover: int = 0
    min_stopover_international: int = 0
    name: str = None
    tax_application: int = 0
    ticketable: bool = False
    travel_component: int = 0
