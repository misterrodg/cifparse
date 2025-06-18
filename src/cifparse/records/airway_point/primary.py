from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    desc_code: str
    bound_code: str
    route_type: str
    level: str
    direct: str
    cruise_id: str
    eu_ind: str
    rec_vhf: str
    rec_vhf_region: str
    rnp: float
    theta: float
    rho: float
    out_true: bool
    out_mag_crs: float
    time: bool
    from_dist: float
    in_true: bool
    in_mag_crs: float
    min_fl_1: int
    min_alt_1: int
    min_fl_2: int
    min_alt_2: int
    max_fl: int
    max_alt: int
    fix_radius: float

    def __init__(self):
        super().__init__("airway_points")
        self.cont_rec_no = None
        self.desc_code = None
        self.bound_code = None
        self.route_type = None
        self.level = None
        self.direct = None
        self.cruise_id = None
        self.eu_ind = None
        self.rec_vhf = None
        self.rec_vhf_region = None
        self.rnp = None
        self.theta = None
        self.rho = None
        self.out_true = None
        self.out_mag_crs = None
        self.time = None
        self.from_dist = None
        self.in_true = None
        self.in_mag_crs = None
        self.min_fl_1 = None
        self.min_alt_1 = None
        self.min_fl_2 = None
        self.min_alt_2 = None
        self.max_fl = None
        self.max_alt = None
        self.fix_radius = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airway_id}, {self.fix_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.desc_code = extract_field(line, w_pri.desc_code)
        self.bound_code = extract_field(line, w_pri.bound_code)
        self.route_type = extract_field(line, w_pri.route_type)
        self.level = extract_field(line, w_pri.level)
        self.direct = extract_field(line, w_pri.direct)
        self.cruise_id = extract_field(line, w_pri.cruise_id)
        self.eu_ind = extract_field(line, w_pri.eu_ind)
        self.rec_vhf = extract_field(line, w_pri.rec_vhf)
        self.rec_vhf_region = extract_field(line, w_pri.rec_vhf_region)
        self.rnp = extract_field(line, w_pri.rnp)
        self.theta = extract_field(line, w_pri.theta)
        self.rho = extract_field(line, w_pri.rho)
        self.out_true, self.out_mag_crs = extract_field(line, w_pri.out_mag_crs)
        self.time, self.from_dist = extract_field(line, w_pri.from_dist)
        self.in_true, self.in_mag_crs = extract_field(line, w_pri.in_mag_crs)
        self.min_fl_1, self.min_alt_1 = extract_field(line, w_pri.min_alt_1)
        self.min_fl_2, self.min_alt_2 = extract_field(line, w_pri.min_alt_2)
        self.max_fl, self.max_alt = extract_field(line, w_pri.max_alt)
        self.fix_radius = extract_field(line, w_pri.fix_radius)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "desc_code",
                "bound_code",
                "route_type",
                "level",
                "direct",
                "cruise_id",
                "eu_ind",
                "rec_vhf",
                "rec_vhf_region",
                "rnp",
                "theta",
                "rho",
                "out_true",
                "out_mag_crs",
                "time",
                "from_dist",
                "in_true",
                "in_mag_crs",
                "min_alt_1",
                "min_fl_1",
                "min_alt_2",
                "min_fl_2",
                "max_alt",
                "max_fl",
                "fix_radius",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self):
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "desc_code": self.desc_code,
            "bound_code": self.bound_code,
            "route_type": self.route_type,
            "level": self.level,
            "direct": self.direct,
            "cruise_id": self.cruise_id,
            "eu_ind": self.eu_ind,
            "rec_vhf": self.rec_vhf,
            "rec_vhf_region": self.rec_vhf_region,
            "rnp": self.rnp,
            "theta": self.theta,
            "rho": self.rho,
            "out_true": self.out_true,
            "out_mag_crs": self.out_mag_crs,
            "time": self.time,
            "from_dist": self.from_dist,
            "in_true": self.in_true,
            "in_mag_crs": self.in_mag_crs,
            "min_alt_1": self.min_alt_1,
            "min_fl_1": self.min_fl_1,
            "min_alt_2": self.min_alt_2,
            "min_fl_2": self.min_fl_2,
            "max_alt": self.max_alt,
            "max_fl": self.max_fl,
            "fix_radius": self.fix_radius,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
