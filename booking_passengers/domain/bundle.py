import dataclasses
from typing import Dict, List

from utils.dataclass_classmethods import FromDictMixin


@dataclasses.dataclass
class Bundle(FromDictMixin):
    bundle_code: str
    total_price: float
    tax_total: float
    currency_code: str = ""
    
    @classmethod
    def from_dict(cls, obj):
        price_obj = list(obj['pricesByJourney'].values())[0]
        return cls(
            bundle_code = obj['bundleCode'],
            total_price = price_obj['prices'][0]['totalPrice'],
            tax_total = price_obj['prices'][0]['taxTotal'],
            currency_code = "COP" if price_obj['prices'][0]['totalPrice'] >= 10000 else "USD"
        )

