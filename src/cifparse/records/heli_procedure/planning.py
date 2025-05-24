from cifparse.functions.field import clean_value, extract_field

from .base import Base
from .widths import w_pla


class Planning(Base):
    cont_rec_no: int
    application: str
    se_ind: str
    se_date: str
    leg_dist: float

    def __init__(self):
        super().__init__("heli_procedure_point_plannings")
        self.cont_rec_no = None
        self.application = None
        self.se_ind = None
        self.se_date = None
        self.leg_dist = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.procedure_id}"

    def from_line(self, line: str) -> "Planning":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pla.cont_rec_no)
        self.application = extract_field(line, w_pla.application)
        self.se_ind = extract_field(line, w_pla.se_ind)
        self.se_date = extract_field(line, w_pla.se_date)
        self.leg_dist = extract_field(line, w_pla.leg_dist)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "se_ind",
                "se_date",
                "leg_dist",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": clean_value(self.cont_rec_no),
            "application": clean_value(self.application),
            "se_ind": clean_value(self.se_ind),
            "se_date": clean_value(self.se_date),
            "leg_dist": clean_value(self.leg_dist),
        }
        return {**leading_dict, **this_dict, **trailing_dict}
