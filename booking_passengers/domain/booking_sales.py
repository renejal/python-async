import dataclasses
import datetime
from enum import Enum

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class PointOfSale(FromDictMixin):
    agent_code: str = None
    domain_code: str = None
    location_code: str = None
    organization_code: str = None

@dataclasses.dataclass
class BookingPointOfSale(FromDictMixin):
    iso_country_code: str = None
    source_system_code: str = None
    agent_code: str = None
    domain_code: str = None
    location_code: str = None
    organization_code: str = None

@dataclasses.dataclass
class BookingSales(FromDictMixin):
    created: PointOfSale = None
    source: BookingPointOfSale = None
    modified: PointOfSale = None