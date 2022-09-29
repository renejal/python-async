import dataclasses

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class JourneyIdentifier(FromDictMixin):
    identifier: str
    carrier_code: str
    op_suffix: str = None
