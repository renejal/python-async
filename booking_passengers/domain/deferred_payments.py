import dataclasses
import datetime
import re
import uuid

EXITO_REF_RE = r"\(415\)(?P<IAC>\d{13})\(?8020\)?(?P<reference>\d{18})\(3900\)(?P<value>\d{14})\(96\)(?P<date>\d{8})"


@dataclasses.dataclass
class ExitoPaymentReference:
    IAC:str
    reference: str
    value: str
    date: str

    @classmethod
    def from_dict(cls, d):
        return cls(
            IAC=d['IAC'].lstrip("0"),
            reference=d['reference'].lstrip("0"),
            value=d['value'].lstrip("0"),
            date=d['date'].lstrip("0")
        )

    @classmethod
    def from_str(cls, s):
        regex = re.compile(EXITO_REF_RE)
        re_match = regex.match(s)
        if re_match:
            return cls.from_dict(re_match.groupdict())
        return None
    
    def get_reference(self):
        return f"(415){self.IAC.zfill(13)}8020{self.reference.zfill(18)}(3900){self.value.zfill(14)}(96){self.date.zfill(8)}"

    def get_barcode_str(self):
        return f"(415){self.IAC.zfill(13)}(8020){self.reference.zfill(18)}(3900){self.value.zfill(14)}(96){self.date.zfill(8)}"

    def get_legacy_output(self):
        return self.get_reference()
    
@dataclasses.dataclass
class DeferredPaymentComment:
    type: str
    id: uuid.UUID
    reference: str = ""
    elements:"typing.List[str]" = dataclasses.field(default_factory=list)
    barcode:str =""

    def __post_init__(self):
        self.elements = ["PAYMENT",self.type,self.reference, self.barcode,"","",str(self.id)]

    @classmethod
    def new(cls, type):
        id = uuid.uuid4()
        return cls(
            type=type,
            id=id,
            elements=["PAYMENT",type,"","","","",str(id)]
        )
    
    @classmethod
    def from_str(cls, d):
        elements = d.split("|")
        if elements[0] == "PAYMENT" and elements[2]:
            try:
                return cls(
                    type=elements[1],
                    reference=elements[2],
                    id=uuid.UUID(elements[-1]),
                    elements=elements,
                    barcode=elements[3]
                )
            except ValueError:
                # This happens when the string in the UUID(...) constructor is not a valid uuid
                return None
        return None
    
    def __str__(self):
        if not self.elements:
            self.elements = ["PAYMENT",self.type,self.reference, self.barcode,"","",str(self.id)]
        return "|".join(self.elements)

#{
#     "reference":"708602",
#     "barcode":null,
#     "legacyOutput":"708602"
#}

#{
#  "reference":"(415)7709998300040802000000000000708602(3900)00000000563618(96)20210312",
#  "barcode":"(415)7709998300040(8020)00000000000708602(3900)00000000563618(96)20210312",
#  "legacyOutput":"(415)7709998300040802000000000000708602(3900)00000000563618(96)20210312"
#}
#{
# (415)7709998300040(8020)00000000000708602(3900)00000000563618(96)20210312",
# (415)7709998300040(8020)00000000000708602(3900)00000000563618(96)20210312",
# (415)7709998300040(8020)00000000000708602(3900)00000000563618(96)20210312"
#}
