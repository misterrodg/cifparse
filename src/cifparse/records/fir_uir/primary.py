from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: str
    adj_fir_id: str
    adj_uir_id: str
    rus: str
    rua: str
    entry: bool
    boundary_via: str
    fir_uir_lat: float
    fir_uir_lon: float
    arc_lat: float
    arc_lon: float
    arc_dist: float
    arc_bearing: float
    fir_upper_limit: str
    uir_lower_limit: str
    uir_upper_limit: str
    cruise_id: str
    fir_uir_name: str

    def __init__(self):
        super().__init__("fir_uirs")
        self.cont_rec_no = None
        self.adj_fir_id = None
        self.adj_uir_id = None
        self.rus = None
        self.rua = None
        self.entry = None
        self.boundary_via = None
        self.fir_uir_lat = None
        self.fir_uir_lon = None
        self.arc_lat = None
        self.arc_lon = None
        self.arc_dist = None
        self.arc_bearing = None
        self.fir_upper_limit = None
        self.uir_lower_limit = None
        self.uir_upper_limit = None
        self.cruise_id = None
        self.fir_uir_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.fir_uir_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.adj_fir_id = extract_field(line, w_pri.adj_fir_id)
        self.adj_uir_id = extract_field(line, w_pri.adj_uir_id)
        self.rus = extract_field(line, w_pri.rus)
        self.rua = extract_field(line, w_pri.rua)
        self.entry = extract_field(line, w_pri.entry)
        self.boundary_via = extract_field(line, w_pri.boundary_via)
        self.fir_uir_lat = extract_field(line, w_pri.fir_uir_lat)
        self.fir_uir_lon = extract_field(line, w_pri.fir_uir_lon)
        self.arc_lat = extract_field(line, w_pri.arc_lat)
        self.arc_lon = extract_field(line, w_pri.arc_lon)
        self.arc_dist = extract_field(line, w_pri.arc_dist)
        self.arc_bearing = extract_field(line, w_pri.arc_bearing)
        self.fir_upper_limit = extract_field(line, w_pri.fir_upper_limit)
        self.uir_lower_limit = extract_field(line, w_pri.uir_lower_limit)
        self.uir_upper_limit = extract_field(line, w_pri.uir_upper_limit)
        self.cruise_id = extract_field(line, w_pri.cruise_id)
        self.fir_uir_name = extract_field(line, w_pri.fir_uir_name)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "adj_fir_id",
                "adj_uir_id",
                "rus",
                "rua",
                "entry",
                "boundary_via",
                "fir_uir_lat",
                "fir_uir_lon",
                "arc_lat",
                "arc_lon",
                "arc_dist",
                "arc_bearing",
                "fir_upper_limit",
                "uir_lower_limit",
                "uir_upper_limit",
                "cruise_id",
                "fir_uir_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "adj_fir_id": self.adj_fir_id,
            "adj_uir_id": self.adj_uir_id,
            "rus": self.rus,
            "rua": self.rua,
            "entry": self.entry,
            "boundary_via": self.boundary_via,
            "fir_uir_lat": self.fir_uir_lat,
            "fir_uir_lon": self.fir_uir_lon,
            "arc_lat": self.arc_lat,
            "arc_lon": self.arc_lon,
            "arc_dist": self.arc_dist,
            "arc_bearing": self.arc_bearing,
            "fir_upper_limit": self.fir_upper_limit,
            "uir_lower_limit": self.uir_lower_limit,
            "uir_upper_limit": self.uir_upper_limit,
            "cruise_id": self.cruise_id,
            "fir_uir_name": self.fir_uir_name,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
