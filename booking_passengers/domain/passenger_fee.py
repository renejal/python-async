import dataclasses
import enum
from typing import List
import datetime

from utils.dataclass_classmethods import FromDictMixin

from .service_charge import ServiceCharge
from itertools import groupby


class FeeType(enum.Enum):
    ALL = 0
    TAX = enum.auto()
    TRAVEL_FEE = enum.auto()
    SERVICE_FEE = enum.auto()
    PAYMENT_FEE = enum.auto()
    PENALTY_FEE = enum.auto()
    SSR_FEE = enum.auto()
    NON_FLIGHT_SERVICE_FEE = enum.auto()
    UPGRADE_FEE = enum.auto()
    SEAT_FEE = enum.auto()
    BASE_FARE = enum.auto()
    SPOILAGE_FEE = enum.auto()
    NAME_CHANGE_FEE = enum.auto()
    CONVENIENCE_FEE = enum.auto()
    BAGGAGE_FEE = enum.auto()
    FARE_SURCHARGE = enum.auto()
    PROMOTION_DISCOUNT = enum.auto()
    SERVICE_BUNDLE = enum.auto()
    EXTRA_BAG_FEE = enum.auto()
    ATPCO_BAG_FEE = enum.auto()


@dataclasses.dataclass
class PassengerFee(FromDictMixin):
    code: str
    type: FeeType = FeeType.ALL
    ssr_code: str = None
    ssr_number: int = 0
    payment_number: int = 0
    is_confirmed: int = 0
    detail: str = None
    passenger_fee_key: str = None
    override: bool = False
    flight_reference: str = None
    note: str = None
    created_date: datetime.datetime = None
    is_protected: bool = False
    service_charges: List[ServiceCharge] = dataclasses.field(default_factory=list)

    def fares(self):
        if not self.service_charges:
            return (0, 0)
        base = 0
        tax = 0
        prev_charge = self.service_charges[0]
        for charge in self.service_charges:
            if charge.detail == "Fee OR":
                if charge.code == prev_charge.code:
                    base = base - prev_charge.amount + charge.amount
            elif charge.ticket_code in ['YS', 'PE', 'MX']:
                tax = tax + charge.amount
            else:
                base = base + charge.amount
            prev_charge = charge
        return (base, tax)
    
    def tax_type(self):
        tax = "Impuesto"
        for charge in self.service_charges:
            if charge.ticket_code == "YS":
                tax = "IVA CO"
            if charge.ticket_code == "PE":
                tax = "IGV PE"
            if charge.ticket_code == "MX":
                tax = "IVA MX"
        return tax
