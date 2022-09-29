import dataclasses
import enum
from typing import List
import datetime

from utils.dataclass_classmethods import FromDictMixin

from .point_of_sale import PointOfSale

class HistoryCategory(enum.Enum):
    UNKNOWN = 0
    BAGGAGE = enum.auto()
    BAG_TAG_PRINT = enum.auto()
    BOARDING_PASS_PRINT = enum.auto()
    CHECK_IN = enum.auto()
    CLASS_OF_SERVICE_CHANGE = enum.auto()
    COMMENT = enum.auto()
    CONFIRMED_SEGMENT = enum.auto()
    CONTACT_CHANGE = enum.auto()
    CONVERTED = enum.auto()
    COUPON_OVERRIDE = enum.auto() 
    DIVIDE_PNR = enum.auto()
    FARE_OVERRIDE = enum.auto()
    FEE = enum.auto()
    FLIGHT_MOVE = enum.auto()
    GROUP_NAME_CHANGE = enum.auto()
    HOLD = enum.auto()
    ITINERARY_SENT = enum.auto()
    MANUAL_PAYMENT = enum.auto()
    MOVE_BACK_PNR = enum.auto()
    NAME_CHANGE = enum.auto()
    NAME_REMOVE = enum.auto()
    PAYMENT = enum.auto()
    PDS = enum.auto()
    PROMOTION = enum.auto()
    QUEUE_PLACE_REMOVE = enum.auto()
    RECORD_LOCATOR = enum.auto()
    SCHEDULE_CANCELLLATION = enum.auto()
    SCHEDULE_CODE_SHARE_CHANGE = enum.auto()
    SCHEDULE_FLIGHT_DESIGNATOR_CHANGE = enum.auto()
    SCHEDULE_TIME_CHANGE = enum.auto()
    SEAT_ASSIGNMENT = enum.auto()
    SEGMENT_CHANGE = enum.auto()
    REPRICE = enum.auto()
    SSR_CHANGE = enum.auto()
    STAND_BY_CHANGE = enum.auto()
    TICKET_NUMBER = enum.auto()
    VERIFIED_TRAVEL_DOCUMENT = enum.auto()
    APPS = enum.auto()
    INHIBITED_OVERRIDE = enum.auto()
    CUSTOM_ID_CHANGE = enum.auto()
    HOLD_DATE_CHANGE = enum.auto()

class HistoryEvent(enum.Enum):
    UNKNOWN = 0
    CONVERTED_HISTORY = enum.auto()
    FLIGHT_TIME_CHANGE = enum.auto()
    FLIGHT_DESIGNATOR_CHANGE = enum.auto()
    ASSIGNED_SEAT = enum.auto()
    REMOVE_SEAT = enum.auto()
    ADDED_FLIGHT = enum.auto()
    DELETED_FLIGHT = enum.auto()
    DELETED_PASSENGER = enum.auto()
    NAME_CHANGE = enum.auto()
    GROUP_NAME_CHANGE = enum.auto()
    CANCELLED_TICKETING = enum.auto()
    SCHEDULE_CHANGE = enum.auto()
    ADDED_PAYMENT = enum.auto()
    SERVICE_FEE = enum.auto()
    QUEUED_PNR = enum.auto()
    UNQUEUED_PNR = enum.auto()
    DELETED_COMMENT = enum.auto()
    DIVIDED = enum.auto()
    CHECKED_IN = enum.auto()
    CHECKED_OUT = enum.auto()
    FARE_OVERRIDE = enum.auto()
    ADDED_BAGGAGE = enum.auto()
    CHANGED_BAGGAGE_WEIGHT = enum.auto()
    CHECKED_BAGGAGE = enum.auto()
    REMOVED_BAGGAGE = enum.auto()
    BOARDED_PASSENGER = enum.auto()
    UNBOARDED_PASSENGER = enum.auto()
    MANUAL_AUTHORIZATION = enum.auto()
    MANUAL_DECLINE = enum.auto()
    UNDO_CANCEL = enum.auto()
    ITINERARY_SENT = enum.auto()
    CONTACT_CHANGE = enum.auto()
    SSR_ADDED = enum.auto()
    FLIGHT_MOVED = enum.auto()
    VERIFIED_DOCUMENT = enum.auto()
    REMOVED_VERIFIED_DOCUMENT = enum.auto()
    PROMOTION = enum.auto()
    BOOKING_COMMENT = enum.auto()
    CANCELLED_SCHEDULE = enum.auto()
    CANCEL_SERVICE_FEE = enum.auto()
    OVERRIDE_SERVICE_FEE = enum.auto()
    ADDED_RECORD_LOCATOR = enum.auto()
    DELETED_RECORD_LOCATOR = enum.auto()
    UPGRADE_CLASS_OF_SERVICE = enum.auto()
    DOWNGRADE_CLASS_OF_SERVICE = enum.auto()
    STANDBY_PRIORITY_CHANGE = enum.auto()
    ASSIGNED_TICKET_NUMBER = enum.auto()
    DELETED_TICKET_NUMBER = enum.auto()
    CONFIRM_SEGMENT_STATUS_CODE_CHANGE = enum.auto()
    CODESHARE_FLIGHT_CHANGED = enum.auto()
    PDS_CANCEL = enum.auto()
    PDS_PENDING = enum.auto()
    PDS_CONFIRM = enum.auto()
    PDS_FINALIZED = enum.auto()
    PDS_DECLINED = enum.auto()
    PDS_EXCEPTION = enum.auto()
    PDS_CANCEL_REFUSED = enum.auto()
    PDS_CANCEL_UNSUCCESSFUL = enum.auto()
    APPS = enum.auto()
    INHIBITED_OVERRIDE = enum.auto()
    PRINTED_BAG_TAG = enum.auto()
    SELF_PRINTED_BAG_TAG = enum.auto()
    PRINTED_BOARDING_PASS = enum.auto()
    ADD_CUSTOMER_ID = enum.auto()
    DELETE_CUSTOMER_ID = enum.auto()
    HOLD_CREATED = enum.auto()
    HOLD_REMOVED = enum.auto()
    HOLD_CHANGED = enum.auto()
    OVERRIDE_COUPON = enum.auto()
    PDS_SYNCHRONIZED = enum.auto()
    PDS_ITEMREMOVED = enum.auto()
    REPRICE = enum.auto()
    CHANNEL_OVERRIDE = enum.auto()
    EMD_CREATED = enum.auto()
    EMD_REMOVED = enum.auto()
    EMD_CHANGED = enum.auto()
    SERVICE_BUNDLE = enum.auto()
    PUBLISHED_FARE_OVERRIDE = enum.auto()
    FARE_CLASS_REALIGNMENT = enum.auto()

@dataclasses.dataclass
class BookingHistory(FromDictMixin):
    history_category: HistoryCategory = HistoryCategory.UNKNOWN
    details: str = None
    event: HistoryEvent = HistoryEvent.UNKNOWN
    point_of_sale: PointOfSale = None
    source_point_of_sale: PointOfSale = None
    received_by: str = None
    received_by_reference: str = None
    created_date: datetime.datetime = None