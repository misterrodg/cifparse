from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    via: str
    path_id: str
    path_area: str
    to_1: str
    to_region_1: str
    to_sec_code_1: str
    to_sub_code_1: str
    runway_transition: str
    enroute_transition: str
    cruise_altitude: str
    term_alt_ref: str
    term_alt_region: str
    alt_dist: str
    cost_index: str
    enrt_alt_ref: str

    def __init__(self):
        super().__init__("company_routes")
        self.via = None
        self.path_id = None
        self.path_area = None
        self.to_1 = None
        self.to_region_1 = None
        self.to_sec_code_1 = None
        self.to_sub_code_1 = None
        self.runway_transition = None
        self.enroute_transition = None
        self.cruise_altitude = None
        self.term_alt_ref = None
        self.term_alt_region = None
        self.alt_dist = None
        self.cost_index = None
        self.enrt_alt_ref = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.company_route_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.via = extract_field(line, w_pri.via)
        self.path_id = extract_field(line, w_pri.path_id)
        self.path_area = extract_field(line, w_pri.path_area)
        self.to_1 = extract_field(line, w_pri.to_1)
        self.to_region_1 = extract_field(line, w_pri.to_region_1)
        self.to_sec_code_1 = extract_field(line, w_pri.to_sec_code_1)
        self.to_sub_code_1 = extract_field(line, w_pri.to_sub_code_1)
        self.runway_transition = extract_field(line, w_pri.runway_transition)
        self.enroute_transition = extract_field(line, w_pri.enroute_transition)
        self.cruise_altitude = extract_field(line, w_pri.cruise_altitude)
        self.term_alt_ref = extract_field(line, w_pri.term_alt_ref)
        self.term_alt_region = extract_field(line, w_pri.term_alt_region)
        self.alt_dist = extract_field(line, w_pri.alt_dist)
        self.cost_index = extract_field(line, w_pri.cost_index)
        self.enrt_alt_ref = extract_field(line, w_pri.enrt_alt_ref)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "via",
                "path_id",
                "path_area",
                "to_1",
                "to_region_1",
                "to_sec_code_1",
                "to_sub_code_1",
                "runway_transition",
                "enroute_transition",
                "cruise_altitude",
                "term_alt_ref",
                "term_alt_region",
                "alt_dist",
                "cost_index",
                "enrt_alt_ref",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "via": self.via,
            "path_id": self.path_id,
            "path_area": self.path_area,
            "to_1": self.to_1,
            "to_region_1": self.to_region_1,
            "to_sec_code_1": self.to_sec_code_1,
            "to_sub_code_1": self.to_sub_code_1,
            "runway_transition": self.runway_transition,
            "enroute_transition": self.enroute_transition,
            "cruise_altitude": self.cruise_altitude,
            "term_alt_ref": self.term_alt_ref,
            "term_alt_region": self.term_alt_region,
            "alt_dist": self.alt_dist,
            "cost_index": self.cost_index,
            "enrt_alt_ref": self.enrt_alt_ref,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
