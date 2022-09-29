import dataclasses

from utils.dataclass_classmethods import FromDictMixin
from typing import List

from .journey_details import JourneyDetails
from .ssr import Ssr


@dataclasses.dataclass
class JourneySsr(FromDictMixin):
    journey_key: str
    journey_details: JourneyDetails
    ssrs: List[Ssr]

    @classmethod
    def from_dict(cls, obj, page_settings, especials=False, assistant=False):
        ssrs = []
        for ssr in obj['ssrs']:
            ssr = Ssr.from_dict(ssr, page_settings)
            # print(ssr)
            if ssr.ssr_type:
                if especials == True and ssr.ssr_type == "Especiales":
                    ssrs.append(ssr)
                elif ssr.ssr_type != "Especiales" and ssr.ssr_type != "Asistencia" and especials == False and assistant == False:
                    ssrs.append(ssr)
                elif assistant == True and ssr.ssr_type == "Asistencia":
                    ssrs.append(ssr)
        return cls(
            journey_key = obj['journeyKey'],
            journey_details= JourneyDetails.from_dict(obj['journeyDetails']),
            ssrs= ssrs
        )