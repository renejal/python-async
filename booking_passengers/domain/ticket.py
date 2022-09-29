import dataclasses
import enum
import datetime
from typing import Dict, List

from utils.dataclass_classmethods import FromDictMixin

class TicketIndicator(enum.Enum):
    UNKNOWN = 0
    TICKET_REQUIRED = enum.auto() 
    AUTOMATED_TICKET_LIFT_REQUIRED = enum.auto() 
    MANUAL_TICKET_LIFT_REQUIRED = enum.auto() 
    AUTOMATED_TICKET_NO_LIFT_REQUIRED = enum.auto() 
    MANUAL_TICKET_NO_LIFT_REQUIRED = enum.auto() 
    HOST_ETICKET_NO_LIFT_REQUIRED = enum.auto() 
    ELECTRONIC_TICKET_NO_LIFT_REQUIRED = enum.auto() 

class TicketStatus(enum.Enum):
    UNKNOWN = 0
    TICKET_AVAILABLE_FOR_USE = enum.auto()
    TICKET_UNAVAILABLE_FOR_USE = enum.auto()
    TICKET_REISSUE_REQUIRED_FOR_PASSENGER = enum.auto()
    TICKET_REISSUE_REQUIRED_FOR_INFANT = enum.auto()
    TICKET_REISSUE_REQUIRED_FOR_BOTH = enum.auto()

@dataclasses.dataclass
class Ticket(FromDictMixin):
    ticket_number: str = None
    infant_ticket_number: str = None
    ticket_indicator: TicketIndicator = TicketIndicator.UNKNOWN
    ticket_status: TicketStatus = TicketStatus.UNKNOWN
    passenger_key: str = None
