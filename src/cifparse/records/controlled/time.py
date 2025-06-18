from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_tim


class Time(Base):
    cont_rec_no: int
    application: str
    time_zone: str
    notam: str
    daylight_ind: str
    op_time_1: str
    op_time_2: str
    op_time_3: str
    op_time_4: str
    op_time_5: str
    op_time_6: str
    op_time_7: str
    controlling_agency: str

    def __init__(self):
        super().__init__("controlled_point_times")
        self.cont_rec_no = None
        self.application = None
        self.time_zone = None
        self.notam = None
        self.daylight_ind = None
        self.op_time_1 = None
        self.op_time_2 = None
        self.op_time_3 = None
        self.op_time_4 = None
        self.op_time_5 = None
        self.op_time_6 = None
        self.op_time_7 = None
        self.controlling_agency = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.center_id}, {self.controlling_agency}"

    def from_line(self, line: str) -> "Time":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_tim.cont_rec_no)
        self.application = extract_field(line, w_tim.application)
        self.time_zone = extract_field(line, w_tim.time_zone)
        self.notam = extract_field(line, w_tim.notam)
        self.daylight_ind = extract_field(line, w_tim.daylight_ind)
        self.op_time_1 = extract_field(line, w_tim.op_time_1)
        self.op_time_2 = extract_field(line, w_tim.op_time_2)
        self.op_time_3 = extract_field(line, w_tim.op_time_3)
        self.op_time_4 = extract_field(line, w_tim.op_time_4)
        self.op_time_5 = extract_field(line, w_tim.op_time_5)
        self.op_time_6 = extract_field(line, w_tim.op_time_6)
        self.op_time_7 = extract_field(line, w_tim.op_time_7)
        self.controlling_agency = extract_field(line, w_tim.controlling_agency)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "time_zone",
                "notam",
                "daylight_ind",
                "op_time_1",
                "op_time_2",
                "op_time_3",
                "op_time_4",
                "op_time_5",
                "op_time_6",
                "op_time_7",
                "controlling_agency",
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
            "notam": self.notam,
            "daylight_ind": self.daylight_ind,
            "op_time_1": self.op_time_1,
            "op_time_2": self.op_time_2,
            "op_time_3": self.op_time_3,
            "op_time_4": self.op_time_4,
            "op_time_5": self.op_time_5,
            "op_time_6": self.op_time_6,
            "op_time_7": self.op_time_7,
            "controlling_agency": self.controlling_agency,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
