from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_aex


class AltExcPrimary(Base):
    cont_rec_no: int
    start_point_id: str
    start_point_region: str
    start_point_sec_code: str
    start_point_sub_code: str
    end_point_id: str
    end_point_region: str
    end_point_sec_code: str
    end_point_sub_code: str
    start_date: str
    end_date: str
    time_zone: str
    daylight_ind: str
    op_time_1: str
    op_time_2: str
    op_time_3: str
    op_time_4: str
    exc_ind: str
    alt_desc: str
    rest_alt_1: str
    blk_id_1: str
    rest_alt_2: str
    blk_id_2: str
    rest_alt_3: str
    blk_id_3: str
    rest_alt_4: str
    blk_id_4: str
    rest_alt_5: str
    blk_id_5: str
    rest_alt_6: str
    blk_id_6: str
    rest_alt_7: str
    blk_id_7: str

    def __init__(self):
        super().__init__("restriction_altitudes")
        self.cont_rec_no = None
        self.start_point_id = None
        self.start_point_region = None
        self.start_point_sec_code = None
        self.start_point_sub_code = None
        self.end_point_id = None
        self.end_point_region = None
        self.end_point_sec_code = None
        self.end_point_sub_code = None
        self.start_date = None
        self.end_date = None
        self.time_zone = None
        self.daylight_ind = None
        self.op_time_1 = None
        self.op_time_2 = None
        self.op_time_3 = None
        self.op_time_4 = None
        self.exc_ind = None
        self.alt_desc = None
        self.rest_alt_1 = None
        self.blk_id_1 = None
        self.rest_alt_2 = None
        self.blk_id_2 = None
        self.rest_alt_3 = None
        self.blk_id_3 = None
        self.rest_alt_4 = None
        self.blk_id_4 = None
        self.rest_alt_5 = None
        self.blk_id_5 = None
        self.rest_alt_6 = None
        self.blk_id_6 = None
        self.rest_alt_7 = None
        self.blk_id_7 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.route_id}, {self.rest_id}"

    def from_line(self, line: str) -> "AltExcPrimary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_aex.cont_rec_no)
        self.start_point_id = extract_field(line, w_aex.start_point_id)
        self.start_point_region = extract_field(line, w_aex.end_point_region)
        self.start_point_sec_code = extract_field(line, w_aex.end_point_sec_code)
        self.start_point_sub_code = extract_field(line, w_aex.end_point_sub_code)
        self.end_point_id = extract_field(line, w_aex.end_point_id)
        self.end_point_region = extract_field(line, w_aex.end_point_region)
        self.end_point_sec_code = extract_field(line, w_aex.end_point_sec_code)
        self.end_point_sub_code = extract_field(line, w_aex.end_point_sub_code)
        self.start_date = extract_field(line, w_aex.start_date)
        self.end_date = extract_field(line, w_aex.end_date)
        self.time_zone = extract_field(line, w_aex.time_zone)
        self.daylight_ind = extract_field(line, w_aex.daylight_ind)
        self.op_time_1 = extract_field(line, w_aex.op_time_1)
        self.op_time_2 = extract_field(line, w_aex.op_time_2)
        self.op_time_3 = extract_field(line, w_aex.op_time_3)
        self.op_time_4 = extract_field(line, w_aex.op_time_4)
        self.exc_ind = extract_field(line, w_aex.exc_ind)
        self.alt_desc = extract_field(line, w_aex.alt_desc)
        self.rest_alt_1 = extract_field(line, w_aex.rest_alt_1)
        self.blk_id_1 = extract_field(line, w_aex.blk_id_1)
        self.rest_alt_2 = extract_field(line, w_aex.rest_alt_2)
        self.blk_id_2 = extract_field(line, w_aex.blk_id_2)
        self.rest_alt_3 = extract_field(line, w_aex.rest_alt_3)
        self.blk_id_3 = extract_field(line, w_aex.blk_id_3)
        self.rest_alt_4 = extract_field(line, w_aex.rest_alt_4)
        self.blk_id_4 = extract_field(line, w_aex.blk_id_4)
        self.rest_alt_5 = extract_field(line, w_aex.rest_alt_5)
        self.blk_id_5 = extract_field(line, w_aex.blk_id_5)
        self.rest_alt_6 = extract_field(line, w_aex.rest_alt_6)
        self.blk_id_6 = extract_field(line, w_aex.blk_id_6)
        self.rest_alt_7 = extract_field(line, w_aex.rest_alt_7)
        self.blk_id_7 = extract_field(line, w_aex.blk_id_7)
        return self

    def ordered_fields(self):
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "start_point_id",
                "start_point_region",
                "start_point_sec_code",
                "start_point_sub_code",
                "end_point_id",
                "end_point_region",
                "end_point_sec_code",
                "end_point_sub_code",
                "start_date",
                "end_date",
                "time_zone",
                "daylight_ind",
                "op_time_1",
                "op_time_2",
                "op_time_3",
                "op_time_4",
                "exc_ind",
                "alt_desc",
                "rest_alt_1",
                "blk_id_1",
                "rest_alt_2",
                "blk_id_2",
                "rest_alt_3",
                "blk_id_3",
                "rest_alt_4",
                "blk_id_4",
                "rest_alt_5",
                "blk_id_5",
                "rest_alt_6",
                "blk_id_6",
                "rest_alt_7",
                "blk_id_7",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "start_point_id": self.start_point_id,
            "start_point_region": self.start_point_region,
            "start_point_sec_code": self.start_point_sec_code,
            "start_point_sub_code": self.start_point_sub_code,
            "end_point_id": self.end_point_id,
            "end_point_region": self.end_point_region,
            "end_point_sec_code": self.end_point_sec_code,
            "end_point_sub_code": self.end_point_sub_code,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "time_zone": self.time_zone,
            "daylight_ind": self.daylight_ind,
            "op_time_1": self.op_time_1,
            "op_time_2": self.op_time_2,
            "op_time_3": self.op_time_3,
            "op_time_4": self.op_time_4,
            "exc_ind": self.exc_ind,
            "alt_desc": self.alt_desc,
            "rest_alt_1": self.rest_alt_1,
            "blk_id_1": self.blk_id_1,
            "rest_alt_2": self.rest_alt_2,
            "blk_id_2": self.blk_id_2,
            "rest_alt_3": self.rest_alt_3,
            "blk_id_3": self.blk_id_3,
            "rest_alt_4": self.rest_alt_4,
            "blk_id_4": self.blk_id_4,
            "rest_alt_5": self.rest_alt_5,
            "blk_id_5": self.blk_id_5,
            "rest_alt_6": self.rest_alt_6,
            "blk_id_6": self.blk_id_6,
            "rest_alt_7": self.rest_alt_7,
            "blk_id_7": self.blk_id_7,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
