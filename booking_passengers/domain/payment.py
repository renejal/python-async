import dataclasses
import enum
from typing import Dict, List
import datetime

from utils.dataclass_classmethods import FromDictMixin
from fixtures.payment_methods import PAYMENT_METHODS


@dataclasses.dataclass
class PaymentAvailable(FromDictMixin):
    payment_method_code: str = None
    allow_deposit: bool = False
    allowed: bool = False
    allow_zero_amount: bool = False
    commissionable: bool = False
    dcc_type: int = 0
    disallow_partial_refund: bool = False
    fee_code: str = None
    in_active: bool = False
    max_installments: int = 0
    name: str = None
    payment_method_fields: Dict[str, dict] = dataclasses.field(default_factory=dict)
    payment_method_type: int = 0
    payment_refund_type: int = 0
    proportional_refund: bool = False
    refundable_by_agent: bool = False
    refund_currency_control: int = 0
    restriction_hours: int = 0
    system_controlled: bool = False
    trace_queueCode: str = None
    validation_required: bool = False
    group: str = None

@dataclasses.dataclass
class PaymentDetails(FromDictMixin):
    account_numberId: int = 0
    parent_paymentId: int = 0
    account_name: str = None
    account_number: str = None
    expiration_date: str = None
    text: str = None
    installments: int = 0
    bin_range: int = 0
    fields: Dict[str, str] = dataclasses.field(default_factory=dict)

@dataclasses.dataclass
class PaymentAmounts(FromDictMixin):
    amount: int = 0
    currency_code: str = None
    collected: int = 0
    collected_currency_code: str = None
    quoted: int = 0
    quoted_currency_code: str = None

@dataclasses.dataclass
class Payment(FromDictMixin):
    payment_key: str = None
    code: str = None
    approval_date: datetime.datetime = None
    details: PaymentDetails = None
    amounts: PaymentAmounts = None
    authorization_code: str = None
    authorization_status: int = 0
    funded_date: str = None
    transaction_code: str = None
    dcc: str = None
    three_d_secure: Dict[str, str] = dataclasses.field(default_factory=dict)
    attachments: List[str] = dataclasses.field(default_factory=list) 
    created_date: datetime.datetime = None
    modified_date: datetime.datetime = None
    type: int = 0
    status: int = 0
    transferred: bool = False
    channel_type: int = 0
    point_of_sale: Dict[str, str] = dataclasses.field(default_factory=dict)
    source_point_of_sale: str = None
    deposit: bool = False
    account_id: int = 0
    voucher: str = None
    added_to_state: bool = False
    created_agent_id: int = 0
    modified_agent_id: int = 0
    reference: int = 0

    def get_payment_type(self):
        return PAYMENT_METHODS.get(self.code, "")

@dataclasses.dataclass
class CashPaymentUrl(FromDictMixin):
    url: str = None
