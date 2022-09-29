from typing import List
from domain.booking import Booking
from domain.booking_comment import BookingComment
from repositories.error_response import get_error_from_response
from conf.settings import SessionManager
from domain.authentication import Token

from conf import settings

class BookingRepository(Token):
    def put_add_comment(self, comments: List[BookingComment]):
        booking_endpoint = "/api/nsk/v3/booking"
        session = SessionManager().get()
        comments_request = [
            {"type": comment.comment_type.value, "text": comment.text} for comment in comments]
        booking_response = session.put(f"{settings.NAVITAIRE_HOST}{booking_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                }, json={"comments": comments_request})

        if booking_response.status_code != 200:
            raise get_error_from_response(booking_response)
        else:
            return booking_response

    def get_booking_by_record_locator(self, record_locator) -> Booking:
        booking_endpoint = f"/api/nsk/v1/booking/retrieve/byRecordLocator/{record_locator}"
        session = SessionManager().get()
        booking_response = session.get(
            f"{settings.NAVITAIRE_HOST}{booking_endpoint}",
            headers={
                "content-type": "application/json",
                "Authorization": f"Bearer {self.token.get_api_token()}"
            },
            verify=False)
        if booking_response.status_code != 200:
            raise get_error_from_response(booking_response)
        else:
            booking_response = booking_response.json()
            booking = Booking.from_dict(booking_response['data'])
            return booking
    
    def get_booking(self) -> Booking:
        booking_endpoint = f"/api/nsk/v1/booking"
        session = SessionManager().get()
        booking_response = session.get(f"{settings.NAVITAIRE_HOST}{booking_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                })
        if booking_response.status_code != 200:
            raise get_error_from_response(booking_response)
        else:
            booking_response = booking_response.json()
            booking = Booking.from_dict(booking_response['data'])
            return booking

    def add_booking_comment(self, comment, notify_contacts=False):
        booking_endpoint = "/api/nsk/v3/booking"
        session = SessionManager().get()
        request_body = {
            "comments": [{"text": comment}]
        }
        if notify_contacts:
            request_body["notifyContacts"] = notify_contacts

        booking_response = session.put(f"{settings.NAVITAIRE_HOST}{booking_endpoint}",
                headers={
                    "content-type": "application/json",
                    "Authorization": f"Bearer {self.token.get_api_token()}"
                },
                json=request_body)

        if booking_response.status_code != 200:
            raise get_error_from_response(booking_response)

    def add_comment_stateless(self, record_locator, comment):
        body = [{
            "type": "Manifest",
            "text": comment,
            "sendToBookingSource": True,
        }]
        session = SessionManager().get()
        response = session.post(
            f"{settings.NAVITAIRE_HOST}/api/nsk/v2/bookings/{record_locator}/comments",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token.get_api_token()}"
            },
            verify=False,
            json=body)
        if response.status_code == 201:
            return response.json()
        raise get_error_from_response(response)
