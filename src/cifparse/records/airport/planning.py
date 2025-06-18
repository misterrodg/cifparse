from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pla


class Planning(Base):
    cont_rec_no: int
    application: str
    fir_ident: str
    uir_ident: str
    se_ind: str
    se_date: str
    as_ind: str
    as_airport_id: str
    as_code: str

    def __init__(self):
        super().__init__("airport_plannings")
        self.cont_rec_no = None
        self.application = None
        self.fir_ident = None
        self.uir_ident = None
        self.se_ind = None
        self.se_date = None
        self.as_ind = None
        self.as_airport_id = None
        self.as_code = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.fir_ident}, {self.uir_ident}"

    def from_line(self, line: str) -> "Planning":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pla.cont_rec_no)
        self.application = extract_field(line, w_pla.application)
        self.fir_ident = extract_field(line, w_pla.fir_ident)
        self.uir_ident = extract_field(line, w_pla.uir_ident)
        self.se_ind = extract_field(line, w_pla.se_ind)
        self.se_date = extract_field(line, w_pla.se_date)
        self.as_ind = extract_field(line, w_pla.as_ind)
        self.as_airport_id = extract_field(line, w_pla.as_airport_id)
        self.as_code = extract_field(line, w_pla.as_code)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "fir_ident",
                "uir_ident",
                "se_ind",
                "se_date",
                "as_ind",
                "as_airport_id",
                "as_code",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "application": self.application,
            "fir_ident": self.fir_ident,
            "uir_ident": self.uir_ident,
            "se_ind": self.se_ind,
            "se_date": self.se_date,
            "as_ind": self.as_ind,
            "as_airport_id": self.as_airport_id,
            "as_code": self.as_code,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
