from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    channel: str
    runway_id: str
    mls_lat: float
    mls_lon: float
    true: bool
    mls_bearing: float
    el_lat: float
    el_lon: float
    mls_dist: int
    plus_minus: str
    el_thr_dist: int
    pro_right: int
    pro_left: int
    cov_right: int
    cov_left: int
    el_angle: float
    mag_var: float
    el_elevation: int
    nom_el_angle: float
    min_el_angle: float
    support_fac: str
    support_region: str
    support_sec_code: str
    support_sub_code: str

    def __init__(self):
        super().__init__("mlss")
        self.cont_rec_no = None
        self.channel = None
        self.runway_id = None
        self.mls_lat = None
        self.mls_lon = None
        self.true = None
        self.mls_bearing = None
        self.el_lat = None
        self.el_lon = None
        self.mls_dist = None
        self.plus_minus = None
        self.el_thr_dist = None
        self.pro_right = None
        self.pro_left = None
        self.cov_right = None
        self.cov_left = None
        self.el_angle = None
        self.mag_var = None
        self.el_elevation = None
        self.nom_el_angle = None
        self.min_el_angle = None
        self.support_fac = None
        self.support_region = None
        self.support_sec_code = None
        self.support_sub_code = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.runway_id}, {self.mls_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.channel = extract_field(line, w_pri.channel)
        self.runway_id = extract_field(line, w_pri.runway_id)
        self.mls_lat = extract_field(line, w_pri.mls_lat)
        self.mls_lon = extract_field(line, w_pri.mls_lon)
        self.true, self.mls_bearing = extract_field(line, w_pri.mls_bearing)
        self.el_lat = extract_field(line, w_pri.el_lat)
        self.el_lon = extract_field(line, w_pri.el_lon)
        self.mls_dist = extract_field(line, w_pri.mls_dist)
        self.plus_minus = extract_field(line, w_pri.plus_minus)
        self.el_thr_dist = extract_field(line, w_pri.el_thr_dist)
        self.pro_right = extract_field(line, w_pri.pro_right)
        self.pro_left = extract_field(line, w_pri.pro_left)
        self.cov_right = extract_field(line, w_pri.cov_right)
        self.cov_left = extract_field(line, w_pri.cov_left)
        self.el_angle = extract_field(line, w_pri.el_angle)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.el_elevation = extract_field(line, w_pri.el_elevation)
        self.nom_el_angle = extract_field(line, w_pri.nom_el_angle)
        self.min_el_angle = extract_field(line, w_pri.min_el_angle)
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
                "channel",
                "runway_id",
                "mls_lat",
                "mls_lon",
                "true",
                "mls_bearing",
                "el_lat",
                "el_lon",
                "mls_dist",
                "plus_minus",
                "el_thr_dist",
                "pro_right",
                "pro_left",
                "cov_right",
                "cov_left",
                "el_angle",
                "mag_var",
                "el_elevation",
                "nom_el_angle",
                "min_el_angle",
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
            "channel": self.channel,
            "runway_id": self.runway_id,
            "mls_lat": self.mls_lat,
            "mls_lon": self.mls_lon,
            "true": self.true,
            "mls_bearing": self.mls_bearing,
            "el_lat": self.el_lat,
            "el_lon": self.el_lon,
            "mls_dist": self.mls_dist,
            "plus_minus": self.plus_minus,
            "el_thr_dist": self.el_thr_dist,
            "pro_right": self.pro_right,
            "pro_left": self.pro_left,
            "cov_right": self.cov_right,
            "cov_left": self.cov_left,
            "el_angle": self.el_angle,
            "mag_var": self.mag_var,
            "el_elevation": self.el_elevation,
            "nom_el_angle": self.nom_el_angle,
            "min_el_angle": self.min_el_angle,
            "support_fac": self.support_fac,
            "support_region": self.support_region,
            "support_sec_code": self.support_sec_code,
            "support_sub_code": self.support_sub_code,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
