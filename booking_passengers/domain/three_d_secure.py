import dataclasses
import enum
from typing import Dict
import datetime

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class ThreeDSecure(FromDictMixin):
    BROWSER_USER_AGENT: str = None
    BROWSER_ACCEPT: str = None
    REMOTE_IP_ADDRESS: str = None
    TERM_URL: str = None
    PA_REQ: str = None
    ACS_URL: str = None
    PA_RES: str = None
    AUTH_RESULT: str = None
    CAVV: str = None
    CAVV_ALGORITHM: str = None
    ECI: str = None
    XID: str = None
    ICABLE: bool = False
    SUCCESSFUL: bool = False