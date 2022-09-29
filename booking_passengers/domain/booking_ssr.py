import dataclasses
from utils.dataclass_classmethods import FromDictMixin
from typing import List

from .market_information import MarketInformation

@dataclasses.dataclass
class Ssr(FromDictMixin):
	is_confirmed: bool = False
	is_confirming_unheld: bool = False
	ssr_duration: int = 0
	ssr_key: str = ""
	count: int = 0
	ssr_code: str = ""
	in_bundle: bool = False
	passenger_key: str = ""
	market: MarketInformation = None