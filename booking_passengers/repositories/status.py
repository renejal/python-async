from dotrez.v2.booking_management.repositories.booking import Booking
class StatusRepository:

    def __init__(self):
        self.__response_list = []
        self.booking_info = []
    
    def  register(self, response):
        self.__response_list.append(response)

    def number_passenger_processed(self):
        index = 0
        for passenger in self.__response_list:
            if passenger.get("status"):
                index += 1
        return index

    def register_booking_info_details(self, booking: Booking):
        booking_info_details = {}
        booking_info_details["number_passenger_processed"] = self.number_passenger_processed()
        for index, journey in enumerate(booking.journeys):
            booking_info_details["origin"] =journey.designator.origin
            booking_info_details["destination"] =journey.designator.destination
            booking_info_details["arrival"] = journey.designator.arrival
            booking_info_details["departure"]=journey.designator.departure
            for segment in journey.segments:
                booking_info_details["identifier"]=segment.identifier.identifier
                booking_info_details["carrier_code"]=segment.identifier.carrier_code
            self.booking_info.append(booking_info_details)
        
    @property
    def response_list(self):
        return self.__response_list

        
    def get_response(self):
        return {"passengers":self.response_list, "booking":self.booking_info}
    
    
