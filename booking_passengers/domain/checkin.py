import dataclasses
import datetime
from enum import Enum
import pytz

class PhoneNumberType(Enum):
    OTHER = 0
    HOME = 1
    WORK = 2
    MOBILE = 3
    FAX = 4


@dataclasses.dataclass
class Fee:
    key: str
    code: str

    @classmethod
    def from_booking(cls, obj):
        return cls(
            obj["passengerFeeKey"],
            obj["code"]
        )


@dataclasses.dataclass
class PhoneNumber:
    number_type: PhoneNumberType
    number: str

    def serialize(self):
        return {
            "type": self.number_type.value,
            "number": self.number
        }

    @classmethod
    def from_booking(cls, obj):
        return cls(
            PhoneNumberType(obj["type"]),
            obj["number"]
        )


@dataclasses.dataclass
class Contact:
    contact_type_code: str
    email_address: str
    first_name: str
    last_name: str
    phone_numbers: list
    title: str = None
    suffix: str = None
    middle_name: str = None

    @classmethod
    def from_booking(cls, obj):
        return cls(
            obj["contactTypeCode"],
            obj["emailAddress"],
            obj["name"]["first"],
            obj["name"]["last"],
            [
                PhoneNumber.from_booking(i)
                for i in obj["phoneNumbers"]
            ]
        )


@dataclasses.dataclass
class Passenger:
    key: str
    alternate_key: str
    first_name: str
    last_name: str
    type_code: str
    gender: str
    customer_number: str = None
    title: str = None
    suffix: str = None
    middle_name: str = None
    has_infant: bool = False
    travel_documents: list = dataclasses.field(default_factory=list)
    fees: list = dataclasses.field(default_factory=list)

    @classmethod
    def from_booking(cls, obj):
        return Passenger(
            obj['passengerKey'],
            obj['passengerAlternateKey'],
            obj['name']["first"],
            obj['name']["last"],
            obj["passengerTypeCode"],
            "Male" if obj["info"]["gender"] == 1 else "Female",
            obj['customerNumber'],
            obj['name']["title"],
            obj['name']["suffix"],
            obj['name']["middle"],
            obj['infant'] is not None,
            obj["travelDocuments"],
            [Fee.from_booking(fee) for fee in obj["fees"]]
        )

    def get_name_dict(self):
        return {
            "first": self.first_name,
            "middle": self.middle_name,
            "last": self.last_name,
            "title": self.title,
            "suffix": self.suffix
        }

    def get_chat_friendly_name(self):
        name = [
            self.title,
            self.first_name,
            self.middle_name,
            self.last_name,
            self.suffix
        ]
        return " ".join(i for i in name if i)

    def get_first_travel_document_number(self, document_type_code='A'):
        return next(
            (i
             for i in self.travel_documents),
            {}
        ).get('number', "")


@dataclasses.dataclass
class Seat:
    unit_designator: str
    unit_key: str
    boarding_zone: str = None

    @classmethod
    def from_booking(cls, obj):
        print(obj)
        return cls(
            obj["unitDesignator"],
            obj['unitKey'],
            f"Grupo {obj['seatInformation']['propertyList']['BRDZONE']}"
        )


@dataclasses.dataclass
class SSR:
    key: str
    code: str
    fee_code: str

    @classmethod
    def from_booking(cls, obj):
        return cls(
            key=obj['ssrKey'],
            code=obj['ssrCode'],
            fee_code=obj['feeCode'],
        )


@dataclasses.dataclass
class Leg:
    departure_time_utc: str = ""

    @classmethod
    def from_booking(cls, obj):
        print(obj)
        return cls(
            departure_time_utc=obj['legInfo']['departureTimeUtc']
        )

@dataclasses.dataclass
class Segment:
    key: str
    carrier_code: str
    flight_number: str
    origin: str
    destination: str
    departure: datetime.datetime
    arrival: datetime.datetime
    is_within_24h: bool = False
    seats: dict = dataclasses.field(default_factory=dict)
    bundle_code: str = ""
    is_in_the_past: bool = False
    passenger_ssrs: dict = dataclasses.field(default_factory=dict)
    passenger_overbooking_status: dict = dataclasses.field(
        default_factory=dict)
    international: bool = False
    class_of_service: str = ""
    legs: list = dataclasses.field(default_factory=list)

    @classmethod
    def from_booking(cls, obj):
        segment = cls(
            obj['segmentKey'],
            obj['identifier']['carrierCode'],
            obj['identifier']['identifier'],
            obj['designator']["origin"],
            obj['designator']["destination"],
            (
                datetime.datetime
                .strptime(obj['designator']["departure"], "%Y-%m-%dT%H:%M:%S")
                .replace(tzinfo=pytz.timezone("America/Bogota"))
            ),
            (
                datetime.datetime
                .strptime(obj['designator']["arrival"], "%Y-%m-%dT%H:%M:%S")
                .replace(tzinfo=pytz.timezone("America/Bogota"))
            )
        )

        segment.legs = [Leg.from_booking(i) for i in obj["legs"]]

        segment.international = obj['international']
        now_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
        now = now_utc.astimezone(pytz.timezone("America/Bogota"))

        time_until_segment = (segment.departure -
                              now).total_seconds() / (60 * 60)
        segment.is_within_24h = (time_until_segment < 24)
        segment.is_in_the_past = (time_until_segment < 0)
        segment.seats = {
            k: [Seat.from_booking(seat) for seat in v["seats"]]
            for k, v in obj["passengerSegment"].items()
        }
        segment.passenger_ssrs = {
            k: [SSR.from_booking(ssr) for ssr in v["ssrs"]]
            for k, v in obj["passengerSegment"].items()
        }
        segment.passenger_overbooking_status = {
            k: bool(v['overBookIndicator'])
            for k, v in obj["passengerSegment"].items()
        }

        segment.class_of_service = obj['fares'][0]["classOfService"]

        return segment

    def get_passenger_seat(self, passenger: Passenger):
        seat: Seat = next(iter(self.seats.get(passenger.key, [])), None)
        if seat:
            return seat
        return ""

    def get_chat_friendly_name(self):
        return (f"{self.carrier_code} {self.flight_number}"
                f" {self.origin} -> {self.destination}"
                f" saliendo {self.departure}")

    def get_flight_number(self):
        return f"{self.carrier_code}{self.flight_number}"

@dataclasses.dataclass
class Journey:
    key: str
    flight_type: int
    stops: int
    origin: str
    destination: str
    departure: datetime.datetime
    arrival: datetime.datetime
    is_within_24h: bool = False
    segments: list = dataclasses.field(default_factory=list)

    @classmethod
    def from_booking(cls, obj):
        journey = cls(
            obj['journeyKey'],
            obj['flightType'],
            obj['stops'],
            obj['designator']["origin"],
            obj['designator']["destination"],
            (
                datetime.datetime
                .strptime(obj['designator']["departure"], "%Y-%m-%dT%H:%M:%S")
                .replace(tzinfo=pytz.timezone("America/Bogota"))
            ),
            (
                datetime.datetime
                .strptime(obj['designator']["arrival"], "%Y-%m-%dT%H:%M:%S")
                .replace(tzinfo=pytz.timezone("America/Bogota"))
            )
        )
        segments = [Segment.from_booking(i) for i in obj["segments"]]

        for segment in obj["segments"]:
            now_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
            for leg in segment['legs']:
                departure_utc = leg['legInfo']['departureTimeUtc']
                departure_utc = datetime.datetime.strptime(departure_utc, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc)
                time_until_leg = (departure_utc -
                                now_utc).total_seconds() / (60 * 60)
                if time_until_leg < 24:
                    journey.is_within_24h = True
                    journey.segments = segments
                    return journey
                else:
                    journey.is_within_24h = False
        journey.segments = segments
        return journey

    def get_chat_friendly_name(self):
        return f"{self.origin} -> {self.destination} saliendo {self.departure}"


    def checkin_open(self, checkin_open=24):
        segment: Segment
        for segment in self.segments:
            now_utc = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
            for leg in segment.legs:
                departure_utc = leg.departure_time_utc
                departure_utc = datetime.datetime.strptime(departure_utc, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc)
                time_until_leg = (departure_utc -
                                now_utc).total_seconds() / (60 * 60)
                if time_until_leg < checkin_open:
                    return True
        return False



    def get_passenger_seat(self, passenger: Passenger):
        seats = ""
        for segment in self.segments:
            seat: Seat = next(iter(segment.seats.get(passenger.key, [])), None)
            seats +=  seat.unit_designator + "-"
        return seats

    def get_flight_number(self):
        flight = ""
        for segment in self.segments:
            flight += segment.flight_number + "-"
        return flight


class Booking:
    def __init__(self, passengers: dict, journeys: dict, contacts: dict):
        self.passengers = passengers
        self.journeys = journeys
        self.segments = {i.key: i for journey in list(
            journeys.values()) for i in journey.segments}
        self.contacts = contacts
        self.passenger_mapping = {
            v.get_chat_friendly_name(): k
            for k, v in self.passengers.items()
        }

        self.journey_mapping = {
            v.get_chat_friendly_name(): k
            for k, v in self.journeys.items()
        }

        self.segment_mapping = {
            v.get_chat_friendly_name(): k
            for k, v in self.segments.items()
        }
        self.has_infants = any(
            pax.has_infant
            for pax in passengers.values()
        )

    def get_chat_friendly_journey_list(self):
        return [i.get_chat_friendly_name() for _, i in self.journeys.items()]

    def get_chat_friendly_segment_list(self):
        return [i.get_chat_friendly_name() for _, i in self.segments.items()]

    def get_passenger(self, key):
        if key in self.passenger_mapping.keys():
            return self.passengers[self.passenger_mapping[key]]
        return self.passengers[key]


    def get_journey(self, key):
        if key in self.journey_mapping.keys():
            return self.journeys[self.journey_mapping[key]]
        return self.journeys.get(key)

    def get_segment(self, key):
        if key in self.segment_mapping.keys():
            return self.segments[self.segment_mapping[key]]
        return self.segments.get(key)

    def is_minor_traveling_alone(self):
        return all(
            "CHD" in i.type_code
            for i in self.passengers.values()
        )

    def has_ssrs_in_list(self, ssr_list: list):
        return any(
            ssr.code in ssr_list
            for segment in self.segments.values()
            for passenger_ssrs in segment.passenger_ssrs.values()
            for ssr in passenger_ssrs
        )

    def has_wheelchair(self):
        wheelchair_codes = (
            'ZWCC', 'ZWCD', 'ZWCO',
            'ZWCP', 'ZWCR', 'ZWCS',
            'ZWCW',
        )
        return self.has_ssrs_in_list(wheelchair_codes)


    def has_especial_extras(self):
        wheelchair_codes = (
            'ZPMR', 'ZLAG', 'ZEXS',
            'ZEMB', 'ZDEA', 'ZBLN',
            'ZASE'
        )
        return self.has_ssrs_in_list(wheelchair_codes)

    def has_pets(self):
        pet_codes = (
            'FPET'
        )
        return self.has_ssrs_in_list(pet_codes)

    def can_give_boarding_pass(self):
        validations = [
            {
                'fcn': self.is_minor_traveling_alone,
                'reason': 'minor_traveling_alone'
            },
            {
                'fcn': self.has_wheelchair,
                'reason': 'has_wheelchair'
            },
            {
                'fcn': self.has_pets,
                'reason': 'has_pets'
            },
            {
                'fcn': self.has_especial_extras,
                'reason': 'has_especial_extras'
            },
        ]
        return not any(map(lambda x: x['fcn'](), validations))

    @classmethod
    def from_navitaire_response(cls, response):
        passengers = {
            k: Passenger.from_booking(v)
            for k, v in response["data"]["passengers"].items()
        }

        journeys = {
            i["journeyKey"]: Journey.from_booking(i)
            for i in response["data"]["journeys"]
        }
        contacts = {
            k: Contact.from_booking(i)
            for k, i in response["data"]["contacts"].items()
        }

        instance = cls(passengers, journeys, contacts)
        instance.record_locator = response["data"]["recordLocator"]
        return instance