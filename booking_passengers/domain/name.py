import dataclasses

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class Name(FromDictMixin):
    first: str = None
    middle: str = None
    last: str = None
    suffix: str = None
    title: str = None