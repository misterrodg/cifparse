from cifparse.functions.record import (
    clean_value,
    convert_altitude_fl,
    convert_course,
    convert_distance,
    convert_radius,
    convert_rnp,
    extract_field,
    translate_cont_rec_no,
)

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    desc_code: str
    bound_code: str
    route_type: str
    level: str
    direct: str
    tc_ind: str
    eu_ind: str
    rec_vhf: str
    rec_vhf_region: str
    rnp: float
    theta: float
    rho: float
    out_mag_crs: float
    from_dist: float
    in_mag_crs: float
    min_alt_1: int
    min_fl_1: int
    min_alt_2: int
    min_fl_2: int
    max_alt: int
    max_fl: int
    fix_radius: float

    def __init__(self):
        super().__init__("airway_points")
        self.cont_rec_no = None
        self.desc_code = None
        self.bound_code = None
        self.route_type = None
        self.level = None
        self.direct = None
        self.tc_ind = None
        self.eu_ind = None
        self.rec_vhf = None
        self.rec_vhf_region = None
        self.rnp = None
        self.theta = None
        self.rho = None
        self.out_mag_crs = None
        self.from_dist = None
        self.in_mag_crs = None
        self.min_alt_1 = None
        self.min_fl_1 = None
        self.min_alt_2 = None
        self.min_fl_2 = None
        self.max_alt = None
        self.max_fl = None
        self.fix_radius = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airway_id}, {self.fix_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = translate_cont_rec_no(extract_field(line, w_pri.cont_rec_no))
        self.desc_code = extract_field(line, w_pri.desc_code)
        self.bound_code = extract_field(line, w_pri.bound_code)
        self.route_type = extract_field(line, w_pri.route_type)
        self.level = extract_field(line, w_pri.level)
        self.direct = extract_field(line, w_pri.direct)
        self.tc_ind = extract_field(line, w_pri.tc_ind)
        self.eu_ind = extract_field(line, w_pri.eu_ind)
        self.rec_vhf = extract_field(line, w_pri.rec_vhf)
        self.rec_vhf_region = extract_field(line, w_pri.rec_vhf_region)
        self.rnp = convert_rnp(extract_field(line, w_pri.rnp))
        self.theta = extract_field(line, w_pri.theta)
        self.rho = extract_field(line, w_pri.rho)
        self.out_mag_crs = convert_course(extract_field(line, w_pri.out_mag_crs))
        self.from_dist = convert_distance(extract_field(line, w_pri.from_dist))
        self.in_mag_crs = convert_course(extract_field(line, w_pri.in_mag_crs))
        self.min_alt_1, self.min_fl_1 = convert_altitude_fl(
            extract_field(line, w_pri.min_alt_1)
        )
        self.min_alt_2, self.min_fl_2 = convert_altitude_fl(
            extract_field(line, w_pri.min_alt_2)
        )
        self.max_alt, self.max_fl = convert_altitude_fl(
            extract_field(line, w_pri.max_alt)
        )
        self.fix_radius = convert_radius(extract_field(line, w_pri.fix_radius))
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
                "tc_ind",
                "eu_ind",
                "rec_vhf",
                "rec_vhf_region",
                "rnp",
                "theta",
                "rho",
                "out_mag_crs",
                "from_dist",
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
            "cont_rec_no": clean_value(self.cont_rec_no),
            "desc_code": clean_value(self.desc_code),
            "bound_code": clean_value(self.bound_code),
            "route_type": clean_value(self.route_type),
            "level": clean_value(self.level),
            "direct": clean_value(self.direct),
            "tc_ind": clean_value(self.tc_ind),
            "eu_ind": clean_value(self.eu_ind),
            "rec_vhf": clean_value(self.rec_vhf),
            "rec_vhf_region": clean_value(self.rec_vhf_region),
            "rnp": clean_value(self.rnp),
            "theta": clean_value(self.theta),
            "rho": clean_value(self.rho),
            "out_mag_crs": clean_value(self.out_mag_crs),
            "from_dist": clean_value(self.from_dist),
            "in_mag_crs": clean_value(self.in_mag_crs),
            "min_alt_1": clean_value(self.min_alt_1),
            "min_fl_1": clean_value(self.min_fl_1),
            "min_alt_2": clean_value(self.min_alt_2),
            "min_fl_2": clean_value(self.min_fl_2),
            "max_alt": clean_value(self.max_alt),
            "max_fl": clean_value(self.max_fl),
            "fix_radius": clean_value(self.fix_radius),
        }
        return {**leading_dict, **this_dict, **trailing_dict}
