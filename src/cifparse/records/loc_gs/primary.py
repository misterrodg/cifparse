from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    frequency: float
    runway_id: str
    loc_lat: float
    loc_lon: float
    true: bool
    loc_bearing: float
    gs_lat: float
    gs_lon: float
    loc_dist: int
    plus_minus: str
    gs_thr_dist: int
    loc_width: float
    gs_angle: float
    mag_var: float
    tch: int
    gs_elevation: int
    support_fac: str
    support_region: str
    support_sec_code: str
    support_sub_code: str

    def __init__(self):
        super().__init__("loc_gss")
        self.cont_rec_no = None
        self.frequency = None
        self.runway_id = None
        self.loc_lat = None
        self.loc_lon = None
        self.true = None
        self.loc_bearing = None
        self.gs_lat = None
        self.gs_lon = None
        self.loc_dist = None
        self.plus_minus = None
        self.gs_thr_dist = None
        self.loc_width = None
        self.gs_angle = None
        self.mag_var = None
        self.tch = None
        self.gs_elevation = None
        self.support_fac = None
        self.support_region = None
        self.support_sec_code = None
        self.support_sub_code = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.runway_id}, {self.loc_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.frequency = extract_field(line, w_pri.frequency)
        self.runway_id = extract_field(line, w_pri.runway_id)
        self.loc_lat = extract_field(line, w_pri.loc_lat)
        self.loc_lon = extract_field(line, w_pri.loc_lon)
        self.true, self.loc_bearing = extract_field(line, w_pri.loc_bearing)
        self.gs_lat = extract_field(line, w_pri.gs_lat)
        self.gs_lon = extract_field(line, w_pri.gs_lon)
        self.loc_dist = extract_field(line, w_pri.loc_dist)
        self.plus_minus = extract_field(line, w_pri.plus_minus)
        self.gs_thr_dist = extract_field(line, w_pri.gs_thr_dist)
        self.loc_width = extract_field(line, w_pri.loc_width)
        self.gs_angle = extract_field(line, w_pri.gs_angle)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.tch = extract_field(line, w_pri.tch)
        self.gs_elevation = extract_field(line, w_pri.gs_elevation)
        self.support_fac = extract_field(line, w_pri.support_fac)
        self.support_region = extract_field(line, w_pri.support_region)
        self.support_sec_code = extract_field(line, w_pri.support_sec_code)
        self.support_sub_code = extract_field(line, w_pri.support_sub_code)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "frequency",
                "runway_id",
                "loc_lat",
                "loc_lon",
                "true",
                "loc_bearing",
                "gs_lat",
                "gs_lon",
                "loc_dist",
                "plus_minus",
                "gs_thr_dist",
                "loc_width",
                "gs_angle",
                "mag_var",
                "tch",
                "gs_elevation",
                "support_fac",
                "support_region",
                "support_sec_code",
                "support_sub_code",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "frequency": self.frequency,
            "runway_id": self.runway_id,
            "loc_lat": self.loc_lat,
            "loc_lon": self.loc_lon,
            "true": self.true,
            "loc_bearing": self.loc_bearing,
            "gs_lat": self.gs_lat,
            "gs_lon": self.gs_lon,
            "loc_dist": self.loc_dist,
            "plus_minus": self.plus_minus,
            "gs_thr_dist": self.gs_thr_dist,
            "loc_width": self.loc_width,
            "gs_angle": self.gs_angle,
            "mag_var": self.mag_var,
            "tch": self.tch,
            "gs_elevation": self.gs_elevation,
            "support_fac": self.support_fac,
            "support_region": self.support_region,
            "support_sec_code": self.support_sec_code,
            "support_sub_code": self.support_sub_code,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
