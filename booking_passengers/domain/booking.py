import re
import json
import dataclasses
from typing import Dict, List

from conf import settings

from utils.dataclass_classmethods import FromDictMixin
from fixtures.payment_methods import TAXES,CARGOS
from .locators import Locators
from .type_of_sale import TypeOfSale
from .booking_info import BookingInfo
from .booking_sales import BookingSales
from .service_charge import ServiceCharge
from .received_by_info import ReceivedByInfo
from .booking_breakdown import BookingPriceBreakdown
from .contact import Contact
from .passenger import Passenger
from .journey import Journey
from .booking_comment import BookingComment
from .booking_history import BookingHistory
from .booking_hold import BookingHold
from .payment import Payment


def payment_match_field(payment, field_regexp):
    for field, value in payment.details.fields.items():
        if re.match(field_regexp, value):
            return True
    return False


@dataclasses.dataclass
class Booking(FromDictMixin):
    self_service_move_available: bool = False
    booking_key: str = ""
    record_locator: str = ""
    currency_code: str = ""
    system_code: str = ""
    group_name: str = ""
    hold: BookingHold = None
    locators: Locators = None
    info: BookingInfo = None
    sales: BookingSales = None
    type_of_sale: TypeOfSale = None
    breakdown: BookingPriceBreakdown = None
    received_by: ReceivedByInfo = None
    contacts: Dict[str, Contact] = dataclasses.field(default_factory=dict)
    passengers: Dict[str, Passenger] = dataclasses.field(default_factory=dict)
    infant_count: int = None
    journeys: List[Journey] = dataclasses.field(default_factory=list)
    comments: List[BookingComment] = dataclasses.field(default_factory=list)
    # queues: list
    history: List[BookingHistory] = dataclasses.field(default_factory=list)
    payments: List[Payment] = dataclasses.field(default_factory=list)
    # add_ons: dict
    charges: List[ServiceCharge] = dataclasses.field(default_factory=list)

    def get_last_reference(self):
        references = []
        for comment in reversed(self.comments):
            if comment.text.startswith('Receipt:6') or comment.text.startswith('Receipt:3'):
                text = comment.text.split('\n')
                receipt = json.loads(text[0].replace('Receipt:','').replace(' ',''))
                references.append(receipt)
        return references

    def get_references(self):
        references = []
        for comment in reversed(self.comments):
            if comment.text.startswith('Receipt:6') or comment.text.startswith('Receipt:3'):
                text = comment.text.split('\n')
                reference = {}
                for item in text:
                    if item.startswith('Receipt:'):
                        reference['receipt'] = item.replace('Receipt:','').replace(' ','')
                    if item.startswith('Passenger:'):
                        reference['passenger'] = item.split('|')[0].replace('Passenger:','').replace(' ','')
                references.append(reference)
        return references

    def is_commited(self):
        return self.record_locator and self.booking_key

    def search_ssr_key(self, journey_key, ssr_code, passenger_key):
        for journey in self.journeys:
            for segment in journey.segments:
                for passenger in segment.passenger_segment.values():
                    for ssr in passenger.ssrs:
                        if journey.journey_key == journey_key and ssr.ssr_code == ssr_code and passenger.passenger_key == passenger_key:
                            return ssr.count
                        # if ssr.ssr_key == ssr_key:
                        #     return ssr.count
        return 0

    def __format_fees(self, fees):
        fee_dict = {}
        for fee in fees.data:
            fee_dict[fee.fee_code] = fee
        return fee_dict

    def add_fees_passenger_detail(self, fee_response):
        fees_response = self.__format_fees(fee_response)
        for passenger in self.passengers.values():
            fees_remove = []
            for fee in passenger.fees:
                for service_charge in fee.service_charges[:]:
                    if service_charge.detail == "Fee OR":
                        fees_remove.append(fee)
                        break
                    if service_charge.code is None:
                        service_charge.detail_es = 'Tarifa publicada'
                        service_charge.detail_en = 'Publish fare'
                        continue
                    if service_charge.code in ['FDDIRQ', 'FIDIRQ']:
                        service_charge.detail_es = 'Cargo por combustible'
                        service_charge.detail_en = 'Fuel charge'
                        continue
                    if service_charge.code in fees_response:
                        fee_response = fees_response[service_charge.code]
                        service_charge.detail_es = fee_response.name
                        service_charge.detail_en = fee_response.description
            for fee_remove in fees_remove[:]:
                passenger.fees.remove(fee_remove)

    def add_fees_detail(self, fee_response):
        fees = self.__format_fees(fee_response)
        for journey in self.journeys:
            for segment in journey.segments:
                for fare in segment.fares:
                    passenger_fares = fare.passenger_fares
                    for passenger_fare in passenger_fares[:]:
                        for service_charge in passenger_fare.service_charges:
                            if service_charge.detail == "Fee OR":
                                passenger_fares.remove(passenger_fare)
                                break
                            if service_charge.code is None:
                                service_charge.detail_es = 'Tarifa publicada'
                                service_charge.detail_en = 'Publish fare'
                                continue
                            if service_charge.code in ['FDDIRQ', 'FIDIRQ']:
                                service_charge.detail_es = 'Cargo por combustible'
                                service_charge.detail_en = 'Fuel charge'
                                continue
                            if service_charge.code in fees:
                                fee = fees[service_charge.code]
                                service_charge.detail_es = fee.name
                                service_charge.detail_en = fee.description

    def add_multiplier(self):
        for journey in self.journeys:
            for segment in journey.segments:
                for fare in segment.fares:
                    for passenger_fare in fare.passenger_fares:
                        multiplier = 0
                        for passenger in self.passengers.values():
                            if passenger.passenger_type_code == passenger_fare.passenger_type:
                                multiplier += 1
                        passenger_fare.multiplier = multiplier

    def get_passenger_name(self, passenger_key):
        try:
            passenger = self.passengers.get(passenger_key)
            return passenger.name
        except:
            return None

    def get_receipt(self):
        # print(self.comments)
        # for comment in self.comments:
        #     if "Receipt:" in comment.text:
        #         return comment.text.split("\n")[0].replace("Receipt:", "")
        return self.locators.numeric_record_locator

    def get_total_if(self, callback):
        total_fare = sum(
            service_charge.amount
            for journey in self.journeys
            for segment in journey.segments
            for fare in segment.fares
            for passenger_fare in fare.passenger_fares[:1]
            for service_charge in passenger_fare.service_charges
            if callback(service_charge)
        )
        return total_fare

    def get_total_yq(self):
        total_fare = self.get_total_if(lambda charge: charge.ticket_code == "YQ")
        return total_fare

    def get_total_airport_charges(self):
        total_fare = self.get_total_if(
            lambda charge: charge.ticket_code in list(CARGOS.keys())
        )
        return total_fare

    def get_total_taxes(self):
        total_fare = self.get_total_if(
            lambda charge: charge.ticket_code in list(TAXES.keys())
        )
        return total_fare

    def get_total_fare(self):
        total_fare = self.get_total_if(lambda charge: charge.code is None)
        return total_fare

    def get_total_fcco(self):
        total_fare = self.get_total_if(lambda charge: charge.code == "FCCO")
        return total_fare

    def get_total_fcys(self):
        total_fare = self.get_total_if(lambda charge: charge.code == "FCYS")
        return total_fare

    def get_total_fddirq(self):
        total_fare = self.get_total_if(lambda charge: charge.code == "FDDIRQ")
        return total_fare

    def get_total_fcadm(self):
        total_fare = self.get_total_if(lambda charge: charge.code == "FCADM")
        return total_fare

    def get_total_fares(self):
        total_fare = sum([
            self.get_total_fare(),
            self.get_total_yq(),
            self.get_total_airport_charges(),
            self.get_total_taxes(),
            -self.breakdown.journey_totals.total_discount,
        ])
        return total_fare

    def get_total_fare_fcco_fcys(self):
        total_fare = sum([
            self.get_total_fare(),
            self.get_total_fcco(),
            self.get_total_fcys()
        ])
        return total_fare

    def get_total_services(self):
        total_base = 0
        total_tax = 0
        for passenger in self.passengers.values():
            for fee in passenger.fees:
                base, tax = fee.fares()
                total_base = total_base + base
                total_tax = total_tax + tax
        return (total_base, total_tax, total_base + total_tax)

    def get_total_services_fare(self):
        total_fare = sum(self.get_total_services()) + self.get_total_fare()
        return total_fare

    def get_total_services_fcys(self):
        total_fare = sum(self.get_total_services()) + self.get_total_fcys()
        return total_fare

    def get_total_services_fare_fcys(self):
        total_fare = self.get_total_services_fare() + self.get_total_services_fcys()
        return total_fare

    def get_checkin_url(self):
        return f"{settings.URL_MMB}/co/es/manage-my-booking/menu?recordLocator={self.record_locator}&lastName={list(self.passengers.values())[0].name.last}"

    @staticmethod
    def set_designatior_name(designator, station_mapping):
        for station in station_mapping:
            if station.station_iata_code == designator.origin:
                designator.origin_name = station.station_name
                continue
            if station.station_iata_code == designator.destination:
                designator.destination_name = station.station_name

    def set_station_mapping(self, station_mapping):
        for journey in self.journeys:
            for segment in journey.segments:
                self.set_designatior_name(segment.designator, station_mapping)
            self.set_designatior_name(journey.designator, station_mapping)

    def has_payment(self, match_callback):
        return bool(next(filter(
            lambda payment: match_callback(payment),
            self.payments
        ), None))

    def is_international(self):
        return any([
            segment.international
            for journey in self.journeys
            for segment in journey.segments
        ])

    def get_carrier_code(self):
        return next((segment.identifier.carrier_code for journey in self.journeys for segment in journey.segments), 'VV')

    def get_passenger_fee_charges(self) -> List[ServiceCharge]:
        return [
            service_charge
            for passenger in self.passengers.values()
            for fee in passenger.fees
            for service_charge in fee.service_charges
        ]
