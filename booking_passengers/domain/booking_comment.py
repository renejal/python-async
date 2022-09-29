import dataclasses
import enum
from typing import List
import datetime

from utils.dataclass_classmethods import FromDictMixin

from .point_of_sale import PointOfSale

class CommentType(enum.Enum):
    DEFAULT = 0
    ITINERARY = enum.auto()
    MANIFEST = enum.auto()
    ALERT = enum.auto()
    ARCHIVE = enum.auto()


@dataclasses.dataclass
class BookingComment(FromDictMixin):
    comment_type: CommentType = CommentType.DEFAULT
    text: str = None
    created_date: datetime.datetime = None
    point_of_sale: PointOfSale = None
    comment_key: str = None
