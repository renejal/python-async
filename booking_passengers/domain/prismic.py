import dataclasses
import datetime
from utils.dataclass_classmethods import FromDictMixin
from typing import List


@dataclasses.dataclass
class CachingSettings:
    expiration_time: int  # seconds
    enabled: bool
    prefix: str


@dataclasses.dataclass
class SsrInfo:
    text: str
    order: int


@dataclasses.dataclass
class ExtraIcon:
    dimensions: list = None
    url: str = None

    @classmethod
    def from_dict(cls, obj):
        return cls(
            dimensions=obj.get('dimensions'),
            url=obj.get("url")
        )


@dataclasses.dataclass
class Ssr:
    group: str
    name: str
    ssr_info: List[SsrInfo]
    ssr_type: str
    extra_icon: ExtraIcon = None

    @classmethod
    def from_dict(cls, obj):
        return cls(
            group=obj['group'],
            ssr_info=[SsrInfo(**info) for info in obj['etra_info']],
            name=obj['extra_text'],
            ssr_type=obj['extra_type'],
            extra_icon=ExtraIcon.from_dict(obj.get("extra_icon"))
        )


@dataclasses.dataclass
class Settings:
    ssrs: list
    ssr_info_cache: CachingSettings

@dataclasses.dataclass
class Payment:
    colombia: bool = False
    peru: bool = False
    code: str = None
    name: str = None
    time_restriction: float = 0.0
    franchise: str = None
    payment_group: str = None
    hold_time_type: str = None
    hold_time: str = None

    @classmethod
    def from_dict(cls, data):
        return cls(
            colombia = data['colombia'],
            peru = data['peru'],
            code = data['code'],
            name = data['name'],
            time_restriction = data['time_restriction'],
            franchise = data['franchise'],
            payment_group = data['payment_group'],
            hold_time_type = data['hold_time_type'],
            hold_time = data['hold_time']
        )
