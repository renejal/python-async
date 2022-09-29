import dataclasses
from typing import List



@dataclasses.dataclass
class PaymentFee:
    amount: float
    fee_code: str
    pax_type: str

@dataclasses.dataclass
class PaymentReferenceRequest:
    amount: float
    currency_of_payment: str
    api_key: str
    origin_system_timestamp: str
    pnr: str
    payment_provider: str
    payment_fees: List[PaymentFee] = dataclasses.field(default_factory=list)
    document_id: str = None
    email: str = None
    channel: str = "WEB"
    is_deposit_payment: bool = False
    pnr_data: bool = True
    retry: bool = False

@dataclasses.dataclass
class PaymentReferenceResponse:
    payment_reference: str
    status_code: str
    status_description: str
    token: str

