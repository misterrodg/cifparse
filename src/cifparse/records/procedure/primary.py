from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    desc_code: str
    turn_direction: str
    rnp: float
    path_term: str
    tdv: str
    rec_vhf: str
    rec_vhf_region: str
    arc_radius: float
    theta: float
    rho: float
    course: float
    true: bool
    dist_time: float
    time: int
    rec_vhf_sec_code: str
    rec_vhf_sub_code: str
    alt_desc: str
    atc: str
    alt_1: int
    fl_1: int
    alt_2: int
    fl_2: int
    trans_alt: int
    speed_limit: int
    vert_angle: float
    center_fix: str
    mult_code: str
    center_fix_region: str
    center_fix_sec_code: str
    center_fix_sub_code: str
    gns_fms_id: str
    speed_desc: str
    rte_qual_1: str
    rte_qual_2: str

    def __init__(self):
        super().__init__("procedure_points")
        self.cont_rec_no = None
        self.desc_code = None
        self.turn_direction = None
        self.rnp = None
        self.path_term = None
        self.tdv = None
        self.rec_vhf = None
        self.rec_vhf_region = None
        self.arc_radius = None
        self.theta = None
        self.rho = None
        self.course = None
        self.true = None
        self.dist_time = None
        self.time = None
        self.rec_vhf_sec_code = None
        self.rec_vhf_sub_code = None
        self.alt_desc = None
        self.atc = None
        self.alt_1 = None
        self.fl_1 = None
        self.alt_2 = None
        self.fl_2 = None
        self.trans_alt = None
        self.speed_limit = None
        self.vert_angle = None
        self.center_fix = None
        self.mult_code = None
        self.center_fix_region = None
        self.center_fix_sec_code = None
        self.center_fix_sub_code = None
        self.gns_fms_id = None
        self.speed_desc = None
        self.rte_qual_1 = None
        self.rte_qual_2 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.procedure_id}, {self.transition_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.desc_code = extract_field(line, w_pri.desc_code)
        self.turn_direction = extract_field(line, w_pri.turn_direction)
        self.rnp = extract_field(line, w_pri.rnp)
        self.path_term = extract_field(line, w_pri.path_term)
        self.tdv = extract_field(line, w_pri.tdv)
        self.rec_vhf = extract_field(line, w_pri.rec_vhf)
        self.rec_vhf_region = extract_field(line, w_pri.rec_vhf_region)
        self.arc_radius = extract_field(line, w_pri.arc_radius)
        self.theta = extract_field(line, w_pri.theta)
        self.rho = extract_field(line, w_pri.rho)
        self.true, self.course = extract_field(line, w_pri.course)
        self.time, self.dist_time = extract_field(line, w_pri.dist_time)
        self.rec_vhf_sec_code = extract_field(line, w_pri.rec_vhf_sec_code)
        self.rec_vhf_sub_code = extract_field(line, w_pri.rec_vhf_sub_code)
        self.alt_desc = extract_field(line, w_pri.alt_desc)
        self.atc = extract_field(line, w_pri.atc)
        self.fl_1, self.alt_1 = extract_field(line, w_pri.alt_1)
        self.fl_2, self.alt_2 = extract_field(line, w_pri.alt_2)
        self.trans_alt = extract_field(line, w_pri.trans_alt)
        self.speed_limit = extract_field(line, w_pri.speed_limit)
        self.vert_angle = extract_field(line, w_pri.vert_angle)
        self.center_fix = extract_field(line, w_pri.center_fix)
        self.mult_code = extract_field(line, w_pri.mult_code)
        self.center_fix_region = extract_field(line, w_pri.center_fix_region)
        self.center_fix_sec_code = extract_field(line, w_pri.center_fix_sec_code)
        self.center_fix_sub_code = extract_field(line, w_pri.center_fix_sub_code)
        self.gns_fms_id = extract_field(line, w_pri.gns_fms_id)
        self.speed_desc = extract_field(line, w_pri.speed_desc)
        self.rte_qual_1 = extract_field(line, w_pri.rte_qual_1)
        self.rte_qual_2 = extract_field(line, w_pri.rte_qual_2)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "desc_code",
                "turn_direction",
                "rnp",
                "path_term",
                "tdv",
                "rec_vhf",
                "rec_vhf_region",
                "arc_radius",
                "theta",
                "rho",
                "course",
                "true",
                "dist_time",
                "time",
                "rec_vhf_sec_code",
                "rec_vhf_sub_code",
                "alt_desc",
                "atc",
                "alt_1",
                "fl_1",
                "alt_2",
                "fl_2",
                "trans_alt",
                "speed_limit",
                "vert_angle",
                "center_fix",
                "mult_code",
                "center_fix_region",
                "center_fix_sec_code",
                "center_fix_sub_code",
                "gns_fms_id",
                "speed_desc",
                "rte_qual_1",
                "rte_qual_2",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "desc_code": self.desc_code,
            "turn_direction": self.turn_direction,
            "rnp": self.rnp,
            "path_term": self.path_term,
            "tdv": self.tdv,
            "rec_vhf": self.rec_vhf,
            "rec_vhf_region": self.rec_vhf_region,
            "arc_radius": self.arc_radius,
            "theta": self.theta,
            "rho": self.rho,
            "course": self.course,
            "true": self.true,
            "dist_time": self.dist_time,
            "time": self.time,
            "rec_vhf_sec_code": self.rec_vhf_sec_code,
            "rec_vhf_sub_code": self.rec_vhf_sub_code,
            "alt_desc": self.alt_desc,
            "atc": self.atc,
            "alt_1": self.alt_1,
            "fl_1": self.fl_1,
            "alt_2": self.alt_2,
            "fl_2": self.fl_2,
            "trans_alt": self.trans_alt,
            "speed_limit": self.speed_limit,
            "vert_angle": self.vert_angle,
            "center_fix": self.center_fix,
            "mult_code": self.mult_code,
            "center_fix_region": self.center_fix_region,
            "center_fix_sec_code": self.center_fix_sec_code,
            "center_fix_sub_code": self.center_fix_sub_code,
            "gns_fms_id": self.gns_fms_id,
            "speed_desc": self.speed_desc,
            "rte_qual_1": self.rte_qual_1,
            "rte_qual_2": self.rte_qual_2,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
