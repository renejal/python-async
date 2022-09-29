import json
from rest_framework.request import Request
from azure.servicebus import ServiceBusClient, ServiceBusMessage

class BusServiceRepository:

    def __init__(self, request: Request, id_message: str, settings) -> None:
        self.__request = request
        self.connection_str = settings.CONNECTION_STR 
        self.azure_queue = settings.AZURE_QUEUE
        self.__data = f"{request.data}".replace('\'','"')
        self.id_message = id_message
    
    def __send_message(self, sender):
        message = ServiceBusMessage(
            self.__data,
            session_id=self.id_message,
            application_properties={'token': self.__request.user.navitaire_token},
            label='MyLabel')
        sender.send_messages(message)

    def send(self):
        servicebus_client = ServiceBusClient.from_connection_string(conn_str=self.connection_str, logging_enable=True)
        with servicebus_client:
            sender = servicebus_client.get_queue_sender(queue_name=self.azure_queue)
            with sender:
                self.__send_message(sender)
        
        

