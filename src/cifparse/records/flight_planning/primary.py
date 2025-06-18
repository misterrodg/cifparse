from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    noe: str
    turbo: str
    rnav: bool
    atc_wc: str
    atc_id: str
    time_zone: str
    description: str
    ltc: str
    rpt: str
    true: bool
    out_mag_crs: float
    alt_desc: str
    fl_1: bool
    alt_1: int
    fl_2: bool
    alt_2: int
    speed_limit: int
    cruise_id: str
    speed_desc: str

    def __init__(self):
        super().__init__("flight_plannings")
        self.cont_rec_no = None
        self.noe = None
        self.turbo = None
        self.rnav = None
        self.atc_wc = None
        self.atc_id = None
        self.time_zone = None
        self.description = None
        self.ltc = None
        self.rpt = None
        self.true = None
        self.out_mag_crs = None
        self.alt_desc = None
        self.fl_1 = None
        self.alt_1 = None
        self.fl_2 = None
        self.alt_2 = None
        self.speed_limit = None
        self.cruise_id = None
        self.speed_desc = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.procedure_type}, {self.procedure_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.noe = extract_field(line, w_pri.noe)
        self.turbo = extract_field(line, w_pri.turbo)
        self.rnav = extract_field(line, w_pri.rnav)
        self.atc_wc = extract_field(line, w_pri.atc_wc)
        self.atc_id = extract_field(line, w_pri.atc_id)
        self.time_zone = extract_field(line, w_pri.time_zone)
        self.description = extract_field(line, w_pri.description)
        self.ltc = extract_field(line, w_pri.ltc)
        self.rpt = extract_field(line, w_pri.rpt)
        self.true, self.out_mag_crs = extract_field(line, w_pri.out_mag_crs)
        self.alt_desc = extract_field(line, w_pri.alt_desc)
        self.fl_1, self.alt_1 = extract_field(line, w_pri.alt_1)
        self.fl_2, self.alt_2 = extract_field(line, w_pri.alt_2)
        self.speed_limit = extract_field(line, w_pri.speed_limit)
        self.cruise_id = extract_field(line, w_pri.cruise_id)
        self.speed_desc = extract_field(line, w_pri.speed_desc)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "noe",
                "turbo",
                "rnav",
                "atc_wc",
                "atc_id",
                "time_zone",
                "description",
                "ltc",
                "rpt",
                "true",
                "out_mag_crs",
                "alt_desc",
                "fl_1",
                "alt_1",
                "fl_2",
                "alt_2",
                "speed_limit",
                "cruise_id",
                "speed_desc",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "noe": self.noe,
            "turbo": self.turbo,
            "rnav": self.rnav,
            "atc_wc": self.atc_wc,
            "atc_id": self.atc_id,
            "time_zone": self.time_zone,
            "description": self.description,
            "ltc": self.ltc,
            "rpt": self.rpt,
            "true": self.true,
            "out_mag_crs": self.out_mag_crs,
            "alt_desc": self.alt_desc,
            "fl_1": self.fl_1,
            "alt_1": self.alt_1,
            "fl_2": self.fl_2,
            "alt_2": self.alt_2,
            "speed_limit": self.speed_limit,
            "cruise_id": self.cruise_id,
            "speed_desc": self.speed_desc,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
