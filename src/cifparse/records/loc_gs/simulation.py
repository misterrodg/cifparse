from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_sim


class Simulation(Base):
    cont_rec_no: int
    application: str
    fac_char: str
    true_bearing: float
    source: str
    beam_width: float
    app_ident_1: str
    app_ident_2: str
    app_ident_3: str
    app_ident_4: str
    app_ident_5: str

    def __init__(self):
        super().__init__("loc_gs_simulations")
        self.cont_rec_no = None
        self.application = None
        self.fac_char = None
        self.true_bearing = None
        self.source = None
        self.beam_width = None
        self.app_ident_1 = None
        self.app_ident_2 = None
        self.app_ident_3 = None
        self.app_ident_4 = None
        self.app_ident_5 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.loc_id}"

    def from_line(self, line: str) -> "Simulation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_sim.cont_rec_no)
        self.application = extract_field(line, w_sim.application)
        self.fac_char = extract_field(line, w_sim.fac_char)
        self.true_bearing = extract_field(line, w_sim.true_bearing)
        self.source = extract_field(line, w_sim.source)
        self.beam_width = extract_field(line, w_sim.beam_width)
        self.app_ident_1 = extract_field(line, w_sim.app_ident_1)
        self.app_ident_2 = extract_field(line, w_sim.app_ident_2)
        self.app_ident_3 = extract_field(line, w_sim.app_ident_3)
        self.app_ident_4 = extract_field(line, w_sim.app_ident_4)
        self.app_ident_5 = extract_field(line, w_sim.app_ident_5)

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "fac_char",
                "true_bearing",
                "source",
                "beam_width",
                "app_ident_1",
                "app_ident_2",
                "app_ident_3",
                "app_ident_4",
                "app_ident_5",
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
            "true_bearing": self.true_bearing,
            "source": self.source,
            "beam_width": self.beam_width,
            "app_ident_1": self.app_ident_1,
            "app_ident_2": self.app_ident_2,
            "app_ident_3": self.app_ident_3,
            "app_ident_4": self.app_ident_4,
            "app_ident_5": self.app_ident_5,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
