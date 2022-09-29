import dataclasses

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class Propierty(FromDictMixin):
    code: str
    value: str
