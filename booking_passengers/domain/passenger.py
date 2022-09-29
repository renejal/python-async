import dataclasses
import enum
from typing import List

from fixtures.document_types import DOCUMENT_TYPES
from utils.dataclass_classmethods import FromDictMixin

from .passenger_fee import PassengerFee
from .name import Name
from .passenger_bag import PassengerBag
from .passenger_program import PassengerProgram
from .passenger_infant import PassengerInfant
from .service_charge import ServiceCharge
from .passenger_information import PassengerInformation
from .passenger_travel_document import PassengerTravelDocument
from .passenger_address import PassengerAddress
from .passenger_travel_document import PassengerTravelDocument
from .passenger_information import PassengerInformation
from .passenger_address import PassengerAddress


class WeightCategory(enum.Enum):
    MALE = 1
    FEMALE = enum.auto()
    CHILD = enum.auto()


@dataclasses.dataclass
class Passenger(FromDictMixin):
    passenger_type_code: str
    passenger_key: str = None
    passenger_alternate_key: str = None
    customer_number: str = None
    fees: List[PassengerFee] = dataclasses.field(default_factory=list)
    name: Name = None
    discount_code: str = None
    bags: List[PassengerBag] = dataclasses.field(default_factory=list)
    program: PassengerProgram = None
    infant: PassengerInfant = None
    info: PassengerInformation = None
    travel_documents: List[PassengerTravelDocument] = dataclasses.field(default_factory=list)
    addresses: List[PassengerAddress] = dataclasses.field(default_factory=list)
    weight_category: WeightCategory = WeightCategory.FEMALE

    def get_full_name(self):
        names = [p.capitalize() for p in self.name.first.split(" ")]
        name = " ".join(names)
        lasts = [p.capitalize() for p in self.name.last.split(" ")]
        last = " ".join(lasts)
        return f"{name} {last}"

    def get_document_type(self):
        # print(self.travel_documents)
        return next((
            DOCUMENT_TYPES.get(
                travel_document.document_type_code,
                travel_document.document_type_code
            )
            for travel_document in self.travel_documents
        ), '')

    def get_document(self):
        return next((travel_document.number for travel_document in self.travel_documents), '')

    def get_fee_charges(self) -> List[ServiceCharge]:
        return [
            service_charge
            for fee in self.fees
            for service_charge in fee.service_charges
        ]

    def get_total_services(self):
        total_base = 0
        total_tax = 0
        for fee in self.fees:
            base, tax = fee.fares()
            total_base = total_base + base
            total_tax = total_tax + tax
        return (total_base, total_tax, total_base + total_tax)

    def get_total_amount(self, booking):
        return sum([
            booking.get_total_fares(),
            booking.get_total_fcadm(),
            self.get_total_services()[2]
        ])


@dataclasses.dataclass
class PassengerSsr(FromDictMixin):
    ssr_key: str = None
    passenger_key: str = None
    price: float = None
    include: int = 0
