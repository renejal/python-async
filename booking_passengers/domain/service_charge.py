import dataclasses
import enum
from typing import List

from utils.dataclass_classmethods import FromDictMixin

class ServiceChargeType(enum.Enum):
    FARE_PRICE = 0
    DISCOUNT = enum.auto()
    INCLUDED_TRAVEL_FEE = enum.auto()
    INCLUDED_TAX = enum.auto()
    TRAVEL_FEE = enum.auto()
    TAX = enum.auto()
    SERVICE_CHARGE = enum.auto()
    PROMOTION_DISCOUNT = enum.auto()
    CONNECTION_ADJUSTMENT_AMOUNT = enum.auto()
    ADDONS_PRICE = enum.auto()
    FARE_POINTS = enum.auto()
    DISCOUNT_POINTS = enum.auto()
    INCLUDED_ADDONS_FEE = enum.auto()
    ADDONS_FEE = enum.auto()
    ADDONS_MARKUP = enum.auto()
    FARE_SURCHARGE = enum.auto()
    ADDONS_CANCEL_FEE = enum.auto()
    CALCULATED = enum.auto()
    NOTE = enum.auto()
    POINTS = enum.auto()
    DYNAMIC_FARE_ADJUSTMENT = enum.auto()


class CollectType(enum.Enum):
    SELLER_CHARGEABLE = 0
    EXTERNAL_CHARGEABLE = enum.auto()
    SELLERNON_CHARGEABLE = enum.auto()
    EXTERNAL_NON_CHARGEABLE = enum.auto()
    EXTERNAL_CHARGEABLE_IMMEDIATE = enum.auto()


@dataclasses.dataclass
class ServiceCharge(FromDictMixin):
    amount: float = 0.0
    code: str = None
    detail: str = None
    detail_en: str = None
    detail_es: str = None
    type: ServiceChargeType = ServiceChargeType.FARE_PRICE
    collect_type: CollectType = CollectType.SELLER_CHARGEABLE
    currency_code: str = None
    foreign_currency_code: str = None
    foreign_amount: float = 0.0
    ticket_code: str = None
