from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    type: str
    usage: str
    lat: float
    lon: float
    mag_var: float
    datum_code: str
    name_indicator: str
    name_description: str

    def __init__(self):
        super().__init__("heli_terminal_waypoints")
        self.cont_rec_no = None
        self.type = None
        self.usage = None
        self.lat = None
        self.lon = None
        self.mag_var = None
        self.datum_code = None
        self.name_indicator = None
        self.name_description = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.waypoint_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.type = extract_field(line, w_pri.type)
        self.usage = extract_field(line, w_pri.usage)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.datum_code = extract_field(line, w_pri.datum_code)
        self.name_indicator = extract_field(line, w_pri.name_indicator)
        self.name_description = extract_field(line, w_pri.name_description)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "type",
                "usage",
                "lat",
                "lon",
                "mag_var",
                "datum_code",
                "name_indicator",
                "name_description",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "type": self.type,
            "usage": self.usage,
            "lat": self.lat,
            "lon": self.lon,
            "mag_var": self.mag_var,
            "datum_code": self.datum_code,
            "name_indicator": self.name_indicator,
            "name_description": self.name_description,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
