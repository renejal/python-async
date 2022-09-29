import dataclasses

from utils.dataclass_classmethods import FromDictMixin
from typing import List

from .journey_ssr import JourneySsr


@dataclasses.dataclass
class SsrAvailable(FromDictMixin):
    journey_ssrs: List[JourneySsr] = dataclasses.field(default_factory=list)
    segment_ssrs: list  = dataclasses.field(default_factory=list)
    leg_ssrs: list  = dataclasses.field(default_factory=list)


    @classmethod
    def from_dict(cls, obj, page_settings, especials=False, assitant=False):
        return cls(
            journey_ssrs = [JourneySsr.from_dict(journey_ssr, page_settings, especials, assitant) for journey_ssr in obj['journeySsrs'] ],
            segment_ssrs= obj['segmentSsrs'],
            leg_ssrs= obj['legSsrs']
        )