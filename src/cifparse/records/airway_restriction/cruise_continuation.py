from cifparse.functions.field import clean_value, extract_field

from .base import Base
from .widths import w_crc


class CruiseContinuation(Base):
    cont_rec_no: int
    application: str
    time_zone: str
    daylight_ind: str
    op_time_1: str
    op_time_2: str
    op_time_3: str
    op_time_4: str
    cruise_id: str

    def __init__(self):
        super().__init__("restriction_cruise_continuations")
        self.cont_rec_no = None
        self.application = None
        self.time_zone = None
        self.daylight_ind = None
        self.op_time_1 = None
        self.op_time_2 = None
        self.op_time_3 = None
        self.op_time_4 = None
        self.cruise_id = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.route_id}, {self.rest_id}"

    def from_line(self, line: str) -> "CruiseContinuation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_crc.cont_rec_no)
        self.application = extract_field(line, w_crc.application)
        self.time_zone = extract_field(line, w_crc.time_zone)
        self.daylight_ind = extract_field(line, w_crc.daylight_ind)
        self.op_time_1 = extract_field(line, w_crc.op_time_1)
        self.op_time_2 = extract_field(line, w_crc.op_time_2)
        self.op_time_3 = extract_field(line, w_crc.op_time_3)
        self.op_time_4 = extract_field(line, w_crc.op_time_4)
        self.cruise_id = extract_field(line, w_crc.cruise_id)
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
                "cruise_id",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": clean_value(self.cont_rec_no),
            "application": clean_value(self.application),
            "time_zone": clean_value(self.time_zone),
            "daylight_ind": clean_value(self.daylight_ind),
            "op_time_1": clean_value(self.op_time_1),
            "op_time_2": clean_value(self.op_time_2),
            "op_time_3": clean_value(self.op_time_3),
            "op_time_4": clean_value(self.op_time_4),
            "cruise_id": clean_value(self.cruise_id),
        }
        return {**leading_dict, **this_dict, **trailing_dict}
