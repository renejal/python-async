import re
from unittest import result
from request_objects.passenger import PassengersRequest
from dotrez.v1.booking_management.domain.booking import Booking
from dotrez.v2.booking_management.repositories.user import UserRepository

class BookingValidator:
    
    def issued_email(self, booking: Booking, request: PassengersRequest):
        email = next(email.email_address for email in booking.contacts.values())
        if email in request.emails:
            return True
        return False

    def owning_carrier_code(self, booking: Booking):
        if booking.info.owning_carrier_code in ["VH", "VV"]:
            return True
        return False


    def is_booking_charter(self, booking: Booking):
        for journey in booking.journeys:
            for segement in journey.segments:
                print("identifier",segement.identifier.identifier)
                if str(segement.identifier.identifier)[:1] != "8":
                    print("no lleva sillas")
                    return False
        return True
    
    def is_organization(self, User: UserRepository):
        rol = User.get_user_roles()
        rol = rol["data"][0]
        if rol["roleCode"] in ["FPNL"]:
            return True
        return False

        



    
        