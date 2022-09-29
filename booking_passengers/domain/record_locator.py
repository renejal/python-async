import dataclasses

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class RecordLocator(FromDictMixin):
    record_locator_key: str = None
    system_domain_code: str = None
    owning_system_code: str = None
    booking_system_code: str = None
    record_code: str = None
    hosted_carrier_code: str = None
    interaction_purpose: str = None
