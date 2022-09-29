import dataclasses
import datetime
from typing import List
from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class InfantRequest:
    passenger_key: str = ""
    document_type_code: str = ""
    first: str = ""
    middle: str = ""
    last: str = ""
    nationality: str = ""
    document_number: str = ""
    gender: str = "" 
    issued_by_code: str = ""
    date_of_birth: datetime.date = ""

    @classmethod
    def from_dict(cls, data):
        return cls(
            first = data['first'],
            middle = data.get('middle'),
            last = data['last'],
            gender = data.get('gender', 'Male'),
            date_of_birth = data.get('dateOfBirth'),
            document_number=data.get('documentNumber'),
            document_type_code=data.get('documentTypeCode'),
            passenger_key=data.get('passengerKey'),
            issued_by_code=data.get('issuedByCode'),
            nationality=data.get('nationality')
        )

@dataclasses.dataclass
class PassengerRequest:
    id: str = ""
    name: str = ""
    last: str = ""
    type_document: str = "" 
    person_type: str = ""
    document_number: str =  ""
    dateOfBirth: str = ""
    gender: str = ""
    country: datetime.date = "" 
    expiration_date: str = "" 
    email: str = "" 
    nacionality: str = "" 
    phone: str = ""
    seat: str = "" 
    ssrs: str = "" 
    child: str = "" 
    infant: InfantRequest = None
    suffix: str = ""

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data.get('id'),
            name = data.get('name'),
            last = data.get('last'),
            type_document = data.get('type_document'),
            person_type = data.get('person_type'),
            document_number = data.get('document_number'),
            dateOfBirth = data.get("dateOfBirth"),
            gender = data.get('gender'),
            country = data.get('country'),
            expiration_date = data.get('expiration_date'),
            email = data.get('email'),
            nacionality = data.get('nacionality'),
            phone = data.get('phone'),
            seat = data.get('seat'),
            ssrs = data.get('ssrs'),
            child = data.get('child'),
            infant = InfantRequest.from_dict(data.get('infant',"")) if data.get('infant')!=None else None)

@dataclasses.dataclass
class PassengersRequest(FromDictMixin):
    passengers: List[PassengerRequest]
    emails: List[str]

@dataclasses.dataclass
class InfantsRequest(FromDictMixin):
    passengers: List[InfantRequest]
