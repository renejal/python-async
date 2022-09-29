import dataclasses
import datetime
from enum import Enum
from typing import List


from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass()
class PaymentAttachment(FromDictMixin):
    id: int =None
    paymentId: int =None
    attachment: str = None