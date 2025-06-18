from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_tim


class Time(Base):
    cont_rec_no: int
    application: str
    op_time_1: str
    op_time_2: str
    op_time_3: str
    op_time_4: str
    op_time_5: str
    op_time_6: str

    def __init__(self):
        super().__init__("enroute_comm_times")
        self.cont_rec_no = None
        self.application = None
        self.op_time_1 = None
        self.op_time_2 = None
        self.op_time_3 = None
        self.op_time_4 = None
        self.op_time_5 = None
        self.op_time_6 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.fir_rdo_id}, {self.comm_freq}"

    def from_line(self, line: str) -> "Time":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_tim.cont_rec_no)
        self.application = extract_field(line, w_tim.application)
        self.op_time_1 = extract_field(line, w_tim.op_time_1)
        self.op_time_2 = extract_field(line, w_tim.op_time_2)
        self.op_time_3 = extract_field(line, w_tim.op_time_3)
        self.op_time_4 = extract_field(line, w_tim.op_time_4)
        self.op_time_5 = extract_field(line, w_tim.op_time_5)
        self.op_time_6 = extract_field(line, w_tim.op_time_6)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "op_time_1",
                "op_time_2",
                "op_time_3",
                "op_time_4",
                "op_time_5",
                "op_time_6",
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
            "op_time_1": self.op_time_1,
            "op_time_2": self.op_time_2,
            "op_time_3": self.op_time_3,
            "op_time_4": self.op_time_4,
            "op_time_5": self.op_time_5,
            "op_time_6": self.op_time_6,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
