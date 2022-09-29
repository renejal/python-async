import dataclasses


from utils.dataclass_classmethods import FromDictMixin

from .charge_breakdown import ChargeBreakdown

@dataclasses.dataclass
class PassengerPriceBreakdownBase(FromDictMixin):
    services: ChargeBreakdown = None
    special_services: ChargeBreakdown = None
    seats: ChargeBreakdown = None
    upgrades: ChargeBreakdown = None
    spoilage: ChargeBreakdown = None
    name_changes: ChargeBreakdown = None
    convenience: ChargeBreakdown = None
    infant: ChargeBreakdown = None