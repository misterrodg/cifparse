from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_sim


class Simulation(Base):
    cont_rec_no: int
    application: str
    fac_char: str
    fac_elev: int

    def __init__(self):
        super().__init__("ndb_simulation")
        self.cont_rec_no = None
        self.application = None
        self.fac_char = None
        self.fac_elev = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.ndb_id}, {self.fac_char}"

    def from_line(self, line: str) -> "Simulation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_sim.cont_rec_no)
        self.application = extract_field(line, w_sim.application)
        self.fac_char = extract_field(line, w_sim.fac_char)
        self.fac_elev = extract_field(line, w_sim.fac_elev)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "fac_char",
                "fac_elev",
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
            "fac_char": self.fac_char,
            "fac_elev": self.fac_elev,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
