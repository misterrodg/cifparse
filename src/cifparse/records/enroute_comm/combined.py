from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_com


class Combined(Base):
    cont_rec_no: int
    application: str
    time_zone: str
    notam: str
    daylight_ind: str
    op_time: str
    callsign: str

    def __init__(self):
        super().__init__("enroute_comm_combineds")
        self.cont_rec_no = None
        self.application = None
        self.time_zone = None
        self.notam = None
        self.daylight_ind = None
        self.op_time = None
        self.callsign = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.fir_rdo_id}, {self.comm_freq}, {self.callsign}"

    def from_line(self, line: str) -> "Combined":
        super().from_lien(line)
        self.cont_rec_no = extract_field(line, w_com.cont_rec_no)
        self.application = extract_field(line, w_com.application)
        self.time_zone = extract_field(line, w_com.time_zone)
        self.notam = extract_field(line, w_com.notam)
        self.daylight_ind = extract_field(line, w_com.daylight_ind)
        self.op_time = extract_field(line, w_com.op_time)
        self.callsign = extract_field(line, w_com.callsign)
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
                "op_time",
                "callsign",
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
            "op_time": self.op_time,
            "callsign": self.callsign,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
