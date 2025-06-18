from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    bearing_1: str
    min_alt_1: str
    radius_1: str
    bearing_2: str
    min_alt_2: str
    radius_2: str
    bearing_3: str
    min_alt_3: str
    radius_3: str
    bearing_4: str
    min_alt_4: str
    radius_4: str
    bearing_5: str
    min_alt_5: str
    radius_5: str
    bearing_6: str
    min_alt_6: str
    radius_6: str
    bearing_7: str
    min_alt_7: str
    radius_7: str
    mag_true: str

    def __init__(self):
        super().__init__("msas")
        self.cont_rec_no = None
        self.bearing_1 = None
        self.min_alt_1 = None
        self.radius_1 = None
        self.bearing_2 = None
        self.min_alt_2 = None
        self.radius_2 = None
        self.bearing_3 = None
        self.min_alt_3 = None
        self.radius_3 = None
        self.bearing_4 = None
        self.min_alt_4 = None
        self.radius_4 = None
        self.bearing_5 = None
        self.min_alt_5 = None
        self.radius_5 = None
        self.bearing_6 = None
        self.min_alt_6 = None
        self.radius_6 = None
        self.bearing_7 = None
        self.min_alt_7 = None
        self.radius_7 = None
        self.mag_true = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.msa_center}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.bearing_1 = extract_field(line, w_pri.bearing_1)
        self.min_alt_1 = extract_field(line, w_pri.min_alt_1)
        self.radius_1 = extract_field(line, w_pri.radius_1)
        self.bearing_2 = extract_field(line, w_pri.bearing_2)
        self.min_alt_2 = extract_field(line, w_pri.min_alt_2)
        self.radius_2 = extract_field(line, w_pri.radius_2)
        self.bearing_3 = extract_field(line, w_pri.bearing_3)
        self.min_alt_3 = extract_field(line, w_pri.min_alt_3)
        self.radius_3 = extract_field(line, w_pri.radius_3)
        self.bearing_4 = extract_field(line, w_pri.bearing_4)
        self.min_alt_4 = extract_field(line, w_pri.min_alt_4)
        self.radius_4 = extract_field(line, w_pri.radius_4)
        self.bearing_5 = extract_field(line, w_pri.bearing_5)
        self.min_alt_5 = extract_field(line, w_pri.min_alt_5)
        self.radius_5 = extract_field(line, w_pri.radius_5)
        self.bearing_6 = extract_field(line, w_pri.bearing_6)
        self.min_alt_6 = extract_field(line, w_pri.min_alt_6)
        self.radius_6 = extract_field(line, w_pri.radius_6)
        self.bearing_7 = extract_field(line, w_pri.bearing_7)
        self.min_alt_7 = extract_field(line, w_pri.min_alt_7)
        self.radius_7 = extract_field(line, w_pri.radius_7)
        self.mag_true = extract_field(line, w_pri.mag_true)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "bearing_1",
                "min_alt_1",
                "radius_1",
                "bearing_2",
                "min_alt_2",
                "radius_2",
                "bearing_3",
                "min_alt_3",
                "radius_3",
                "bearing_4",
                "min_alt_4",
                "radius_4",
                "bearing_5",
                "min_alt_5",
                "radius_5",
                "bearing_6",
                "min_alt_6",
                "radius_6",
                "bearing_7",
                "min_alt_7",
                "radius_7",
                "mag_true",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "bearing_1": self.bearing_1,
            "min_alt_1": self.min_alt_1,
            "radius_1": self.radius_1,
            "bearing_2": self.bearing_2,
            "min_alt_2": self.min_alt_2,
            "radius_2": self.radius_2,
            "bearing_3": self.bearing_3,
            "min_alt_3": self.min_alt_3,
            "radius_3": self.radius_3,
            "bearing_4": self.bearing_4,
            "min_alt_4": self.min_alt_4,
            "radius_4": self.radius_4,
            "bearing_5": self.bearing_5,
            "min_alt_5": self.min_alt_5,
            "radius_5": self.radius_5,
            "bearing_6": self.bearing_6,
            "min_alt_6": self.min_alt_6,
            "radius_6": self.radius_6,
            "bearing_7": self.bearing_7,
            "min_alt_7": self.min_alt_7,
            "radius_7": self.radius_7,
            "mag_true": self.mag_true,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
