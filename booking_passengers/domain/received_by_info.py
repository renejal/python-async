import dataclasses

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class ReceivedByInfo(FromDictMixin):
    received_by:str = None
    latest_received_by:str = None
    received_reference:str = None
    latest_received_reference:str = None
    referral_code:str = None