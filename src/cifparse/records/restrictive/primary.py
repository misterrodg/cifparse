from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    level: str
    time_zone: str
    notam: str
    boundary_via: str
    lat: float
    lon: float
    arc_lat: float
    arc_lon: float
    arc_dist: float
    arc_bearing: float
    lower_limit: str
    lower_unit: str
    upper_limit: str
    upper_unit: str
    restrictive_name: str

    def __init__(self):
        super().__init__("restrictive_points")
        self.cont_rec_no = None
        self.level = None
        self.time_zone = None
        self.notam = None
        self.boundary_via = None
        self.lat = None
        self.lon = None
        self.arc_lat = None
        self.arc_lon = None
        self.arc_dist = None
        self.arc_bearing = None
        self.lower_limit = None
        self.lower_unit = None
        self.upper_limit = None
        self.upper_unit = None
        self.restrictive_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.restrictive_id}, {self.restrictive_type}, {self.restrictive_name}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.level = extract_field(line, w_pri.level)
        self.time_zone = extract_field(line, w_pri.time_zone)
        self.notam = extract_field(line, w_pri.notam)
        self.boundary_via = extract_field(line, w_pri.boundary_via)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.arc_lat = extract_field(line, w_pri.arc_lat)
        self.arc_lon = extract_field(line, w_pri.arc_lon)
        self.arc_dist = extract_field(line, w_pri.arc_dist)
        self.arc_bearing = extract_field(line, w_pri.arc_bearing)
        self.lower_limit = extract_field(line, w_pri.lower_limit)
        self.lower_unit = extract_field(line, w_pri.lower_unit)
        self.upper_limit = extract_field(line, w_pri.upper_limit)
        self.upper_unit = extract_field(line, w_pri.upper_unit)
        self.restrictive_name = extract_field(line, w_pri.restrictive_name)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "level",
                "time_zone",
                "notam",
                "boundary_via",
                "lat",
                "lon",
                "arc_lat",
                "arc_lon",
                "arc_dist",
                "arc_bearing",
                "lower_limit",
                "lower_unit",
                "upper_limit",
                "upper_unit",
                "restrictive_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "level": self.level,
            "time_zone": self.time_zone,
            "notam": self.notam,
            "boundary_via": self.boundary_via,
            "lat": self.lat,
            "lon": self.lon,
            "arc_lat": self.arc_lat,
            "arc_lon": self.arc_lon,
            "arc_dist": self.arc_dist,
            "arc_bearing": self.arc_bearing,
            "lower_limit": self.lower_limit,
            "lower_unit": self.lower_unit,
            "upper_limit": self.upper_limit,
            "upper_unit": self.upper_unit,
            "restrictive_name": self.restrictive_name,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
