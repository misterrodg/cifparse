from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_aec


class AltExcContinuation(Base):
    cont_rec_no: int
    application: str
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
        super().__init__("restriction_altitude_continuations")
        self.cont_rec_no = None
        self.application = None
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

    def from_line(self, line: str) -> "AltExcContinuation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_aec.cont_rec_no)
        self.application = extract_field(line, w_aec.application)
        self.time_zone = extract_field(line, w_aec.time_zone)
        self.daylight_ind = extract_field(line, w_aec.daylight_ind)
        self.op_time_1 = extract_field(line, w_aec.op_time_1)
        self.op_time_2 = extract_field(line, w_aec.op_time_2)
        self.op_time_3 = extract_field(line, w_aec.op_time_3)
        self.op_time_4 = extract_field(line, w_aec.op_time_4)
        self.exc_ind = extract_field(line, w_aec.exc_ind)
        self.alt_desc = extract_field(line, w_aec.alt_desc)
        self.rest_alt_1 = extract_field(line, w_aec.rest_alt_1)
        self.blk_id_1 = extract_field(line, w_aec.blk_id_1)
        self.rest_alt_2 = extract_field(line, w_aec.rest_alt_2)
        self.blk_id_2 = extract_field(line, w_aec.blk_id_2)
        self.rest_alt_3 = extract_field(line, w_aec.rest_alt_3)
        self.blk_id_3 = extract_field(line, w_aec.blk_id_3)
        self.rest_alt_4 = extract_field(line, w_aec.rest_alt_4)
        self.blk_id_4 = extract_field(line, w_aec.blk_id_4)
        self.rest_alt_5 = extract_field(line, w_aec.rest_alt_5)
        self.blk_id_5 = extract_field(line, w_aec.blk_id_5)
        self.rest_alt_6 = extract_field(line, w_aec.rest_alt_6)
        self.blk_id_6 = extract_field(line, w_aec.blk_id_6)
        self.rest_alt_7 = extract_field(line, w_aec.rest_alt_7)
        self.blk_id_7 = extract_field(line, w_aec.blk_id_7)
        return self

    def ordered_fields(self):
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
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
            "application": self.application,
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
