import json
from urllib import response

from requests import Session
from request_objects.passenger import PassengerRequest, InfantsRequest
from dotrez.v1.booking_management.utils.login_navitaire import SetNavitaireHost
from conf.settings import SessionManager
from rest_framework import status
from rest_framework.response import Response
from repositories.error_response import get_error_from_response
# from dotrez.v1.booking_management.http_response import HttpResponse
from utils.http_response import HttpResponse
from rest_framework.serializers import ValidationError


class PassengerRepository(SetNavitaireHost):
    def get(self, passenger_request: PassengerRequest):
        passenger_endpoint = f"/api/nsk/v1/booking/passengers/{passenger_request.passenger_key}"
        session = SessionManager().get()
        passenger_response = session.get(
            f"{self.host}{passenger_endpoint}",
            headers={
                "content-type": "application/json",
                "Authorization": f"Bearer {self.get_api_token()}"
            })
        return passenger_response


    def post(self, passenger_request: PassengerRequest):
        passenger_endpoint = f"/api/nsk/v3/booking/passengers/{passenger_request.passenger_key}"
        session = SessionManager().get()
        passenger_navitaire_request = {
            "customerNumber": passenger_request.username,
            "name": {
                "first": passenger_request.first,
                "middle": passenger_request.middle,
                "last": passenger_request.last
            },
            "info":{
                "gender": passenger_request.gender,
                "dateOfBirth": passenger_request.date_of_birth
            }
        }
        passenger_response = session.put(
            f"{self.host}{passenger_endpoint}",
            headers={
                "content-type": "application/json",
                "Authorization": f"Bearer {self.get_api_token()}"
            },
            json=passenger_navitaire_request)
        return passenger_response

    def add_travelDocument(self, passenger: PassengerRequest, passenger_booking_key):
        passenger_endpoint = f"/api/nsk/v2/booking/passengers/{passenger_booking_key}/documents"
        document_type_dict= {"CC":"A","P":"P","TI":"A","M":"M"}
        gender_dict = {"M":"MALE","F":"FEMALE","XX":"XX"}
        session = SessionManager().get()
        passenger_navitaire_request = {
            "documentTypeCode": document_type_dict.get(passenger.type_document),
            "name": {
                "first": passenger.name,
                "middle": "",
                "last": passenger.last,
                "title": "",
                "suffix": ""
            },
            "nationality": "",
            "expirationDate": passenger.expiration_date if passenger.expiration_date != None else "3000-05-18",
            "number": passenger.document_number,
            "gender": gender_dict.get(passenger.gender),
            "dateOfBirth": passenger.dateOfBirth
        }
        passenger_response = session.post(
        f"{self.host}{passenger_endpoint}",
        headers={
            "content-type": "application/json",
            "Authorization": f"Bearer {self.get_api_token()}"
        },
        json=passenger_navitaire_request)
        if passenger_response.status_code != 201:
            return HttpResponse.Success({"name":passenger.name,"last":passenger.last,"document":passenger.document_number, 
                                             "detail":"error", "status":False})
        return HttpResponse.Success({"name":passenger.name, "last":passenger.last, "document":passenger.document_number,"detail":"add document","status":True})

    async def update_passenger(session, self, passenger:PassengerRequest, passenger_booking_key) -> Response:
        gender_dict = {"F":"Male","M":"Female","X":"XX"}
        waive = 'True'
        passenger_endpoint = f"/api/nsk/v3/booking/passengers/{passenger_booking_key}?waiveNameChangeFees={waive}"
        passenger_navitaire_request = {
            "customerNumber": "",
            "name": {
                "first": passenger.name,
                "middle": "",
                "last": passenger.last,
                "suffix":passenger.suffix
            },
            "info":{
                "gender": gender_dict.get(passenger.gender),
                "dateOfBirth": passenger.dateOfBirth
            }
        }
        passenger_response = session.put(
        f"{self.host}{passenger_endpoint}",
        headers={
            "content-type": "application/json",
            "Authorization": f"Bearer {self.get_api_token()}"
        },
        json=passenger_navitaire_request)
        if passenger_response.status_code != 200:
            return HttpResponse.CustomError(passenger_response.status_code,{"name":passenger.name, "last":passenger.last, 
                                                                            "document":passenger.document_number,"detail":"add name","status":False})
        return HttpResponse.Success({"name":passenger.name, "last":passenger.last, 
                                     "document":passenger.document_number,"detail":"add name","status":True})

    def update_passenger_type(self, passenger:PassengerRequest, passenger_key)-> Response:
        passenger_endpoint = f"/api/nsk/v1/booking/passengers/{passenger_key}/passengerTypeCode"
        session = SessionManager().get()
        passenger_navitaire_request = {
            "passengerTypeCode": "CHD",
            "dateOfBirth": passenger.dateOfBirth,
        }
        passenger_response = session.patch(
            f"{self.host}{passenger_endpoint}",
            headers={
                "content-type": "application/json",
                "Authorization": f"Bearer {self.get_api_token()}"
            },
            json=passenger_navitaire_request)
        print("child ", passenger_navitaire_request)
        if passenger_response != 200:
            return HttpResponse.CustomError(passenger_response.status_code,{"name":passenger.name, "last":passenger.last, 
                                                                            "document":passenger.document_number,"detail":"change passenger type CHD","status":False})
        return HttpResponse.Success({"name":passenger.name, "last":passenger.last, 
                                     "document":passenger.document_number,"detail":"change passenger type CHD","status":True}) 

    def update_passenger_birth_date(self, passenger, birth_date):
        passenger_endpoint = f"/api/nsk/v3/booking/passengers/{passenger.passenger_key}"
        session = SessionManager().get()
        passenger_navitaire_request = {
            "info": {
                "dateOfBirth": birth_date
            }
        }
        passenger_response = session.patch(
            f"{self.host}{passenger_endpoint}",
            headers={
                "content-type": "application/json",
                "Authorization": f"Bearer {self.get_api_token()}"
            },
            json=passenger_navitaire_request)
        if passenger_response.status_code != 200:
            raise get_error_from_response(passenger_response)
        return passenger_response
class PassengerBookingRepository(SetNavitaireHost):
    def put(self, passenger_request: PassengerRequest):
        passenger_endpoint = f"/api/nsk/v3/booking/passengers/{passenger_request.passenger_key}"
        passenger_navitaire_request = {
            "name": {
                "first": passenger_request.first,
                "middle": passenger_request.middle,
                "last": passenger_request.last
            },
            "info":{
                "gender": passenger_request.gender,
                "dateOfBirth": passenger_request.date_of_birth
            }
        }

        session = SessionManager().get()
        passenger_response = session.put(
            f"{self.host}{passenger_endpoint}",
            headers={
                "content-type": "application/json",
                "Authorization": f"Bearer {self.get_api_token()}"
            },
            json=passenger_navitaire_request)
        if passenger_response.status_code != 200:
            raise get_error_from_response(passenger_response)
        return passenger_response
class PassengerInfantRepository(SetNavitaireHost):
    def post(self, passenger_request: PassengerRequest):
        passenger_infant_endpoint = f"/api/nsk/v3/booking/passengers/{passenger_request.passenger_key}/infant"
        session = SessionManager().get()
        infant = passenger_request.infant
        passenger_infant_navitaire_request = {
            "name": {
                "first": infant.first,
                "middle": infant.middle,
                "last": infant.last
            },
            "gender": infant.gender,
            "dateOfBirth": infant.date_of_birth
        }
        passenger_infant_response = session.put(
            f"{self.host}{passenger_infant_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.get_api_token()}"
                },
                data=json.dumps(passenger_infant_navitaire_request))
        return passenger_infant_response
            
    def add_infante(self, passenger: PassengerRequest, passenger_key):
        passenger_infant_endpoint = f"/api/nsk/v3/booking/passengers/{passenger_key}/infant"
        session = SessionManager().get()
        infant = passenger.infant
        print("___________infant", infant)
        passenger_infant_navitaire_request = {
            "dateOfBirth": infant.date_of_birth,
            "gender": infant.gender,
            "name": {
                "first": infant.first,
                "last": infant.last
            },
        }
        passenger_infant_response = session.post(
            f"{self.host}{passenger_infant_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.get_api_token()}"
                },
                data=json.dumps(passenger_infant_navitaire_request))
        if passenger_infant_response.status_code != 201:
            return HttpResponse.CustomError(passenger_infant_response.status_code,{"name":passenger.name, "last":passenger.last, 
                                                                                   "document":passenger.document_number,"detail":"error","status":False})
        return HttpResponse.Success({"name":passenger.name, "last":passenger.last, "document":passenger.document_number,"detail":"add infant","status":True})

    def update_infant(self, infants: InfantsRequest):
        for infant_request in infants.passengers:
            passenger_infant_endpoint = f"/api/nsk/v3/booking/passengers/{infant_request.passenger_key}/infant"
            session = SessionManager().get()
            infant = infant_request
            passenger_infant_navitaire_request = {
                "dateOfBirth": infant.date_of_birth,
                "gender": infant.gender,
                "name": {
                    "first": infant.first,
                    "last": infant.last
                }
            }
            passenger_infant_response = session.put(
                f"{self.host}{passenger_infant_endpoint}",
                    headers={
                        "content-type": "application/json",
                        "Authorization": f"Bearer {self.get_api_token()}"
                    },
                    data=json.dumps(passenger_infant_navitaire_request))
            if passenger_infant_response.status_code != 200:
                raise get_error_from_response(passenger_infant_response)
            
    def add_document(self, infants: InfantsRequest):
        for infant_request in infants.passengers:
            passenger_infant_endpoint = f"/api/nsk/v2/booking/passengers/{infant_request.passenger_key}/infant/documents/"
            session = SessionManager().get()
            infant = infant_request
            passenger_infant_navitaire_request =  {
                "documentTypeCode": infant.document_type_code,
                "name": {
                    "first": infant.first,
                    "middle": infant.middle,
                    "last": infant.last,
                },
                "number": infant.document_number,
                "gender": infant.gender,
                "dateOfBirth": infant.date_of_birth,
                "issuedByCode": infant.issued_by_code,
                "nationality": infant.nationality
            }
            headers={
                "content-type": "application/json",
                "Authorization": f"Bearer {self.get_api_token()}"
            }
            passenger_infant_response = session.post(
                f"{self.host}{passenger_infant_endpoint}",
                headers=headers,
                json=passenger_infant_navitaire_request)

            if passenger_infant_response.status_code != 201:
                print("error")
                raise get_error_from_response(passenger_infant_response)