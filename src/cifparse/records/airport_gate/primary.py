from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    lat: float
    lon: float
    gate_name: str

    def __init__(self):
        super().__init__("airport_gates")
        self.cont_rec_no = None
        self.lat = None
        self.lon = None
        self.gate_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.gate_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.gate_name = extract_field(line, w_pri.gate_name)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "lat",
                "lon",
                "gate_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "lat": self.lat,
            "lon": self.lon,
            "gate_name": self.gate_name,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
