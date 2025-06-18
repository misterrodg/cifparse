from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_con


class Continuation(Base):
    cont_rec_no: int
    application: str
    fac_char: str
    baz_lat: float
    baz_lon: float
    true: bool
    baz_mag_bearing: float
    dp_lat: float
    dp_lon: float
    baz_dist: int
    plus_minus: str
    pro_right: float
    pro_left: float
    cov_right: float
    cov_left: float
    baz_true_bearing: float
    baz_source: str
    az_true_bearing: float
    az_source: str
    tch: int

    def __init__(self):
        super().__init__("mls_continuations")
        self.cont_rec_no = None
        self.application = None
        self.fac_char = None
        self.baz_lat = None
        self.baz_lon = None
        self.true = None
        self.baz_mag_bearing = None
        self.dp_lat = None
        self.dp_lon = None
        self.baz_dist = None
        self.plus_minus = None
        self.pro_right = None
        self.pro_left = None
        self.cov_right = None
        self.cov_left = None
        self.baz_true_bearing = None
        self.baz_source = None
        self.az_true_bearing = None
        self.az_source = None
        self.tch = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.runway_id}, {self.mls_id}"

    def from_line(self, line: str) -> "Continuation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_con.cont_rec_no)
        self.application = extract_field(line, w_con.application)
        self.fac_char = extract_field(line, w_con.fac_char)
        self.baz_lat = extract_field(line, w_con.baz_lat)
        self.baz_lon = extract_field(line, w_con.baz_lon)
        self.true, self.baz_mag_bearing = extract_field(line, w_con.baz_mag_bearing)
        self.dp_lat = extract_field(line, w_con.dp_lat)
        self.dp_lon = extract_field(line, w_con.dp_lon)
        self.baz_dist = extract_field(line, w_con.baz_dist)
        self.plus_minus = extract_field(line, w_con.plus_minus)
        self.pro_right = extract_field(line, w_con.pro_right)
        self.pro_left = extract_field(line, w_con.pro_left)
        self.cov_right = extract_field(line, w_con.cov_righ)
        self.cov_left = extract_field(line, w_con.cov_left)
        self.baz_true_bearing = extract_field(line, w_con.baz_true_bearing)
        self.baz_source = extract_field(line, w_con.baz_source)
        self.az_true_bearing = extract_field(line, w_con.az_true_bearing)
        self.az_source = extract_field(line, w_con.az_source)
        self.tch = extract_field(line, w_con.tch)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "fac_char",
                "baz_lat",
                "baz_lon",
                "true",
                "baz_mag_bearing",
                "dp_lat",
                "dp_lon",
                "baz_dist",
                "plus_minus",
                "pro_right",
                "pro_left",
                "cov_right",
                "cov_left",
                "baz_true_bearing",
                "baz_source",
                "az_true_bearing",
                "az_source",
                "tch",
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
            "baz_lat": self.baz_lat,
            "baz_lon": self.baz_lon,
            "true": self.true,
            "baz_mag_bearing": self.baz_mag_bearing,
            "dp_lat": self.dp_lat,
            "dp_lon": self.dp_lon,
            "baz_dist": self.baz_dist,
            "plus_minus": self.plus_minus,
            "pro_right": self.pro_right,
            "pro_left": self.pro_left,
            "cov_right": self.cov_right,
            "cov_left": self.cov_left,
            "baz_true_bearing": self.baz_true_bearing,
            "baz_source": self.baz_source,
            "az_true_bearing": self.az_true_bearing,
            "az_source": self.az_source,
            "tch": self.tch,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
