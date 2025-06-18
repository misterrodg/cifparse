from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: str
    true: bool
    in_course: float
    turn_dir: str
    leg_length: int
    leg_time: int
    min_alt: int
    min_fl: int
    max_alt: int
    max_fl: int
    hold_speed: int
    rnp: float
    arc_radius: float
    hold_name: str

    def __init__(self):
        super().__init__("holds")
        self.cont_rec_no = None
        self.true = None
        self.in_course = None
        self.turn_dir = None
        self.leg_length = None
        self.leg_time = None
        self.min_alt = None
        self.min_fl = None
        self.max_alt = None
        self.max_fl = None
        self.hold_speed = None
        self.rnp = None
        self.arc_radius = None
        self.hold_name = None

    def __repr__(self):
        return f"{self.__class__.__hold_name__}: {self.environment_id}, {self.fix_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.true, self.in_course = extract_field(line, w_pri.in_course)
        self.turn_dir = extract_field(line, w_pri.turn_dir)
        self.leg_length = extract_field(line, w_pri.leg_length)
        self.leg_time = extract_field(line, w_pri.leg_time)
        self.min_fl, self.min_alt = extract_field(line, w_pri.min_alt)
        self.max_fl, self.max_alt = extract_field(line, w_pri.max_alt)
        self.hold_speed = extract_field(line, w_pri.hold_speed)
        self.rnp = extract_field(line, w_pri.rnp)
        self.arc_radius = extract_field(line, w_pri.arc_radius)
        self.hold_name = extract_field(line, w_pri.hold_name)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "true",
                "in_course",
                "turn_dir",
                "leg_length",
                "leg_time",
                "min_alt",
                "min_fl",
                "max_alt",
                "max_fl",
                "hold_speed",
                "rnp",
                "arc_radius",
                "hold_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "true": self.true,
            "in_course": self.in_course,
            "turn_dir": self.turn_dir,
            "leg_length": self.leg_length,
            "leg_time": self.leg_time,
            "min_alt": self.min_alt,
            "min_fl": self.min_fl,
            "max_alt": self.max_alt,
            "max_fl": self.max_fl,
            "hold_speed": self.hold_speed,
            "rnp": self.rnp,
            "arc_radius": self.arc_radius,
            "hold_name": self.hold_name,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
