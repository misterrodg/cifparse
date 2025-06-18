from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    course_from: float
    course_to: float
    mt_ind: str
    level_from_1: str
    vert_sep_1: str
    level_to_1: str
    level_from_2: str
    vert_sep_2: str
    level_to_2: str
    level_from_3: str
    vert_sep_3: str
    level_to_3: str
    level_from_4: str
    vert_sep_4: str
    level_to_4: str

    def __init__(self):
        super().__init__("cruise_tables")
        self.course_from = None
        self.course_to = None
        self.mt_ind = None
        self.level_from_1 = None
        self.vert_sep_1 = None
        self.level_to_1 = None
        self.level_from_2 = None
        self.vert_sep_2 = None
        self.level_to_2 = None
        self.level_from_3 = None
        self.vert_sep_3 = None
        self.level_to_3 = None
        self.level_from_4 = None
        self.vert_sep_4 = None
        self.level_to_4 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.cruise_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.course_from = extract_field(line, w_pri.course_from)
        self.course_to = extract_field(line, w_pri.course_to)
        self.mt_ind = extract_field(line, w_pri.mt_ind)
        self.level_from_1 = extract_field(line, w_pri.level_from_1)
        self.vert_sep_1 = extract_field(line, w_pri.vert_sep_1)
        self.level_to_1 = extract_field(line, w_pri.level_to_1)
        self.level_from_2 = extract_field(line, w_pri.level_from_2)
        self.vert_sep_2 = extract_field(line, w_pri.vert_sep_2)
        self.level_to_2 = extract_field(line, w_pri.level_to_2)
        self.level_from_3 = extract_field(line, w_pri.level_from_3)
        self.vert_sep_3 = extract_field(line, w_pri.vert_sep_3)
        self.level_to_3 = extract_field(line, w_pri.level_to_3)
        self.level_from_4 = extract_field(line, w_pri.level_from_4)
        self.vert_sep_4 = extract_field(line, w_pri.vert_sep_4)
        self.level_to_4 = extract_field(line, w_pri.level_to_4)

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "course_from",
                "course_to",
                "mt_ind",
                "level_from_1",
                "vert_sep_1",
                "level_to_1",
                "level_from_2",
                "vert_sep_2",
                "level_to_2",
                "level_from_3",
                "vert_sep_3",
                "level_to_3",
                "level_from_4",
                "vert_sep_4",
                "level_to_4",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "course_from": self.course_from,
            "course_to": self.course_to,
            "mt_ind": self.mt_ind,
            "level_from_1": self.level_from_1,
            "vert_sep_1": self.vert_sep_1,
            "level_to_1": self.level_to_1,
            "level_from_2": self.level_from_2,
            "vert_sep_2": self.vert_sep_2,
            "level_to_2": self.level_to_2,
            "level_from_3": self.level_from_3,
            "vert_sep_3": self.vert_sep_3,
            "level_to_3": self.level_to_3,
            "level_from_4": self.level_from_4,
            "vert_sep_4": self.vert_sep_4,
            "level_to_4": self.level_to_4,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
