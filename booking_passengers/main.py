from ast import Pass
from request_objects.passenger import PassengerRequest
import json
def upload_request():
    with open("prueba1.json", encoding="utf8") as file:
        file_json = json.load(file)

def main():
    # implemtacion asyncio and aiohttp 
    data = upload_request()
    passengers = PassengerRequest.from_dict(data)
    print(passengers)
    


main()
