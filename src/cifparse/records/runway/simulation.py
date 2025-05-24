from cifparse.functions.field import clean_value, extract_field

from .base import Base
from .widths import w_sim


class Simulation(Base):
    cont_rec_no: int
    application: str
    true_bearing: float
    source: str
    location: str
    tdz_elev: int

    def __init__(self):
        super().__init__("runway_simulations")
        self.cont_rec_no = None
        self.application = None
        self.true_bearing = None
        self.source = None
        self.location = None
        self.tdz_elev = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.runway_id}"

    def from_line(self, line: str) -> "Simulation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_sim.cont_rec_no)
        self.application = extract_field(line, w_sim.application)
        self.true_bearing = extract_field(line, w_sim.true_bearing)
        self.source = extract_field(line, w_sim.source)
        self.location = extract_field(line, w_sim.location)
        self.tdz_elev = extract_field(line, w_sim.tdz_elev)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "true_bearing",
                "source",
                "location",
                "tdz_elev",
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
            "true_bearing": clean_value(self.true_bearing),
            "source": clean_value(self.source),
            "location": clean_value(self.location),
            "tdz_elev": clean_value(self.tdz_elev),
        }
        return {**leading_dict, **this_dict, **trailing_dict}
