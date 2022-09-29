import dataclasses
import enum
import datetime
from typing import Dict, List

class PassengerScore(enum.Enum):
    guest_value_code: str
    score: int = 0
    passenger_key: str = None