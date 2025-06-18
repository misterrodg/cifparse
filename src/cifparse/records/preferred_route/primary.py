from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    fix_id: str
    fix_region: str
    fix_sec_code: str
    fix_sub_code: str
    via: str
    path_id: str
    path_area: str
    level: str
    route_type: str
    int_point: str
    int_region: str
    int_sec_code: str
    int_sub_code: str
    term_point: str
    term_region: str
    term_sec_code: str
    term_sub_code: str
    min_alt: int
    min_fl: int
    max_alt: int
    max_fl: int
    time_zone: str
    aircraft_use: str
    direction: str
    alt_desc: str
    alt_1: int
    fl_1: int
    alt_2: int
    fl_2: int

    def __init__(self):
        super().__init__("preferred_routes")
        self.cont_rec_no = None
        self.fix_id = None
        self.fix_region = None
        self.fix_sec_code = None
        self.fix_sub_code = None
        self.via = None
        self.path_id = None
        self.path_area = None
        self.level = None
        self.route_type = None
        self.int_point = None
        self.int_region = None
        self.int_sec_code = None
        self.int_sub_code = None
        self.term_point = None
        self.term_region = None
        self.term_sec_code = None
        self.term_sub_code = None
        self.min_alt = None
        self.min_fl = None
        self.max_alt = None
        self.max_fl = None
        self.time_zone = None
        self.aircraft_use = None
        self.direction = None
        self.alt_desc = None
        self.alt_1 = None
        self.fl_1 = None
        self.alt_2 = None
        self.fl_2 = None

    def __repr__(self):
        return (
            f"{self.__class__.__name__}: {self.route_id}, {self.seq_no}, {self.fix_id}"
        )

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.fix_id = extract_field(line, w_pri.fix_id)
        self.fix_region = extract_field(line, w_pri.fix_region)
        self.fix_sec_code = extract_field(line, w_pri.fix_sec_code)
        self.fix_sub_code = extract_field(line, w_pri.fix_sub_code)
        self.via = extract_field(line, w_pri.via)
        self.path_id = extract_field(line, w_pri.path_id)
        self.path_area = extract_field(line, w_pri.path_area)
        self.level = extract_field(line, w_pri.level)
        self.route_type = extract_field(line, w_pri.route_type)
        self.int_point = extract_field(line, w_pri.int_point)
        self.int_region = extract_field(line, w_pri.int_region)
        self.int_sec_code = extract_field(line, w_pri.int_sec_code)
        self.int_sub_code = extract_field(line, w_pri.int_sub_code)
        self.term_point = extract_field(line, w_pri.term_point)
        self.term_region = extract_field(line, w_pri.term_region)
        self.term_sec_code = extract_field(line, w_pri.term_sec_code)
        self.term_sub_code = extract_field(line, w_pri.term_sub_code)
        self.min_fl, self.min_alt = extract_field(line, w_pri.min_alt)
        self.max_fl, self.max_alt = extract_field(line, w_pri.max_alt)
        self.time_zone = extract_field(line, w_pri.time_zone)
        self.aircraft_use = extract_field(line, w_pri.aircraft_use)
        self.direction = extract_field(line, w_pri.direction)
        self.alt_desc = extract_field(line, w_pri.alt_desc)
        self.fl_1, self.alt_1 = extract_field(line, w_pri.alt_1)
        self.fl_2, self.alt_2 = extract_field(line, w_pri.alt_2)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "fix_id",
                "fix_region",
                "fix_sec_code",
                "fix_sub_code",
                "via",
                "path_id",
                "path_area",
                "level",
                "route_type",
                "int_point",
                "int_region",
                "int_sec_code",
                "int_sub_code",
                "term_point",
                "term_region",
                "term_sec_code",
                "term_sub_code",
                "min_alt",
                "min_fl",
                "max_alt",
                "max_fl",
                "time_zone",
                "aircraft_use",
                "direction",
                "alt_desc",
                "alt_1",
                "fl_1",
                "alt_2",
                "fl_2",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "fix_id": self.fix_id,
            "fix_region": self.fix_region,
            "fix_sec_code": self.fix_sec_code,
            "fix_sub_code": self.fix_sub_code,
            "via": self.via,
            "path_id": self.path_id,
            "path_area": self.path_area,
            "level": self.level,
            "route_type": self.route_type,
            "int_point": self.int_point,
            "int_region": self.int_region,
            "int_sec_code": self.int_sec_code,
            "int_sub_code": self.int_sub_code,
            "term_point": self.term_point,
            "term_region": self.term_region,
            "term_sec_code": self.term_sec_code,
            "term_sub_code": self.term_sub_code,
            "min_alt": self.min_alt,
            "min_fl": self.min_fl,
            "max_alt": self.max_alt,
            "max_fl": self.max_fl,
            "time_zone": self.time_zone,
            "aircraft_use": self.aircraft_use,
            "direction": self.direction,
            "alt_desc": self.alt_desc,
            "alt_1": self.alt_1,
            "fl_1": self.fl_1,
            "alt_2": self.alt_2,
            "fl_2": self.fl_2,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
