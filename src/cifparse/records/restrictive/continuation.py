from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_con


class Continuation(Base):
    cont_rec_no: int
    application: str
    se_ind: str
    se_date: str

    def __init__(self):
        super().__init__("restrictive_continuations")
        self.cont_rec_no = None
        self.application = None
        self.se_ind = None
        self.se_date = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.restrictive_id}"

    def from_line(self, line: str) -> "Continuation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_con.cont_rec_no)
        self.application = extract_field(line, w_con.application)
        self.se_ind = extract_field(line, w_con.se_ind)
        self.se_date = extract_field(line, w_con.se_date)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "se_ind",
                "se_date",
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
            "se_ind": self.se_ind,
            "se_date": self.se_date,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
