from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    dta_1: str
    alt_type_1: str
    alt_id_1: str
    dta_2: str
    alt_type_2: str
    alt_id_2: str
    dta_3: str
    alt_type_3: str
    alt_id_3: str
    dta_4: str
    alt_type_4: str
    alt_id_4: str
    dta_5: str
    alt_type_5: str
    alt_id_5: str
    dta_6: str
    alt_type_6: str
    alt_id_6: str

    def __init__(self):
        super().__init__("alternate_records")
        self.dta_1 = None
        self.alt_type_1 = None
        self.alt_id_1 = None
        self.dta_2 = None
        self.alt_type_2 = None
        self.alt_id_2 = None
        self.dta_3 = None
        self.alt_type_3 = None
        self.alt_id_3 = None
        self.dta_4 = None
        self.alt_type_4 = None
        self.alt_id_4 = None
        self.dta_5 = None
        self.alt_type_5 = None
        self.alt_id_5 = None
        self.dta_6 = None
        self.alt_type_6 = None
        self.alt_id_6 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.point_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.dta_1 = extract_field(line, w_pri.dta_1)
        self.alt_type_1 = extract_field(line, w_pri.alt_type_1)
        self.alt_id_1 = extract_field(line, w_pri.alt_id_1)
        self.dta_2 = extract_field(line, w_pri.dta_2)
        self.alt_type_2 = extract_field(line, w_pri.alt_type_2)
        self.alt_id_2 = extract_field(line, w_pri.alt_id_2)
        self.dta_3 = extract_field(line, w_pri.dta_3)
        self.alt_type_3 = extract_field(line, w_pri.alt_type_3)
        self.alt_id_3 = extract_field(line, w_pri.alt_id_3)
        self.dta_4 = extract_field(line, w_pri.dta_4)
        self.alt_type_4 = extract_field(line, w_pri.alt_type_4)
        self.alt_id_4 = extract_field(line, w_pri.alt_id_4)
        self.dta_5 = extract_field(line, w_pri.dta_5)
        self.alt_type_5 = extract_field(line, w_pri.alt_type_5)
        self.alt_id_5 = extract_field(line, w_pri.alt_id_5)
        self.dta_6 = extract_field(line, w_pri.dta_6)
        self.alt_type_6 = extract_field(line, w_pri.alt_type_6)
        self.alt_id_6 = extract_field(line, w_pri.alt_id_6)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "dta_1",
                "alt_type_1",
                "alt_id_1",
                "dta_2",
                "alt_type_2",
                "alt_id_2",
                "dta_3",
                "alt_type_3",
                "alt_id_3",
                "dta_4",
                "alt_type_4",
                "alt_id_4",
                "dta_5",
                "alt_type_5",
                "alt_id_5",
                "dta_6",
                "alt_type_6",
                "alt_id_6",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "dta_1": self.dta_1,
            "alt_type_1": self.alt_type_1,
            "alt_id_1": self.alt_id_1,
            "dta_2": self.dta_2,
            "alt_type_2": self.alt_type_2,
            "alt_id_2": self.alt_id_2,
            "dta_3": self.dta_3,
            "alt_type_3": self.alt_type_3,
            "alt_id_3": self.alt_id_3,
            "dta_4": self.dta_4,
            "alt_type_4": self.alt_type_4,
            "alt_id_4": self.alt_id_4,
            "dta_5": self.dta_5,
            "alt_type_5": self.alt_type_5,
            "alt_id_5": self.alt_id_5,
            "dta_6": self.dta_6,
            "alt_type_6": self.alt_type_6,
            "alt_id_6": self.alt_id_6,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
