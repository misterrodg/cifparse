from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_con


class Continuation(Base):
    cont_rec_no: int
    application: str
    intermediate_id_1: str
    intermediate_region_1: str
    intermediate_sec_code_1: str
    intermediate_sub_code_1: str
    intermediate_atd_1: str
    frt_code_1: str
    intermediate_id_2: str
    intermediate_region_2: str
    intermediate_sec_code_2: str
    intermediate_sub_code_2: str
    intermediate_atd_2: str
    frt_code_2: str
    intermediate_id_3: str
    intermediate_region_3: str
    intermediate_sec_code_3: str
    intermediate_sub_code_3: str
    intermediate_atd_3: str
    frt_code_3: str
    intermediate_id_4: str
    intermediate_region_4: str
    intermediate_sec_code_4: str
    intermediate_sub_code_4: str
    intermediate_atd_4: str
    frt_code_4: str

    def __init__(self):
        super().__init__("flight_planning_continuations")
        self.cont_rec_no = None
        self.application = None
        self.intermediate_id_1 = None
        self.intermediate_region_1 = None
        self.intermediate_sec_code_1 = None
        self.intermediate_sub_code_1 = None
        self.intermediate_atd_1 = None
        self.frt_code_1 = None
        self.intermediate_id_2 = None
        self.intermediate_region_2 = None
        self.intermediate_sec_code_2 = None
        self.intermediate_sub_code_2 = None
        self.intermediate_atd_2 = None
        self.frt_code_2 = None
        self.intermediate_id_3 = None
        self.intermediate_region_3 = None
        self.intermediate_sec_code_3 = None
        self.intermediate_sub_code_3 = None
        self.intermediate_atd_3 = None
        self.frt_code_3 = None
        self.intermediate_id_4 = None
        self.intermediate_region_4 = None
        self.intermediate_sec_code_4 = None
        self.intermediate_sub_code_4 = None
        self.intermediate_atd_4 = None
        self.frt_code_4 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.procedure_type}, {self.procedure_id}"

    def from_line(self, line: str) -> "Continuation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_con.cont_rec_no)
        self.application = extract_field(line, w_con.application)
        self.intermediate_id_1 = extract_field(line, w_con.intermediate_id_1)
        self.intermediate_region_1 = extract_field(line, w_con.intermediate_region_1)
        self.intermediate_sec_code_1 = extract_field(
            line, w_con.intermediate_sec_code_1
        )
        self.intermediate_sub_code_1 = extract_field(
            line, w_con.intermediate_sub_code_1
        )
        self.intermediate_atd_1 = extract_field(line, w_con.intermediate_atd_1)
        self.frt_code_1 = extract_field(line, w_con.frt_code_1)
        self.intermediate_id_2 = extract_field(line, w_con.intermediate_id_2)
        self.intermediate_region_2 = extract_field(line, w_con.intermediate_region_2)
        self.intermediate_sec_code_2 = extract_field(
            line, w_con.intermediate_sec_code_2
        )
        self.intermediate_sub_code_2 = extract_field(
            line, w_con.intermediate_sub_code_2
        )
        self.intermediate_atd_2 = extract_field(line, w_con.intermediate_atd_2)
        self.frt_code_2 = extract_field(line, w_con.frt_code_2)
        self.intermediate_id_3 = extract_field(line, w_con.intermediate_id_3)
        self.intermediate_region_3 = extract_field(line, w_con.intermediate_region_3)
        self.intermediate_sec_code_3 = extract_field(
            line, w_con.intermediate_sec_code_3
        )
        self.intermediate_sub_code_3 = extract_field(
            line, w_con.intermediate_sub_code_3
        )
        self.intermediate_atd_3 = extract_field(line, w_con.intermediate_atd_3)
        self.frt_code_3 = extract_field(line, w_con.frt_code_3)
        self.intermediate_id_4 = extract_field(line, w_con.intermediate_id_4)
        self.intermediate_region_4 = extract_field(line, w_con.intermediate_region_4)
        self.intermediate_sec_code_4 = extract_field(
            line, w_con.intermediate_sec_code_4
        )
        self.intermediate_sub_code_4 = extract_field(
            line, w_con.intermediate_sub_code_4
        )
        self.intermediate_atd_4 = extract_field(line, w_con.intermediate_atd_4)
        self.frt_code_4 = extract_field(line, w_con.frt_code_4)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "intermediate_id_1",
                "intermediate_region_1",
                "intermediate_sec_code_1",
                "intermediate_sub_code_1",
                "intermediate_atd_1",
                "frt_code_1",
                "intermediate_id_2",
                "intermediate_region_2",
                "intermediate_sec_code_2",
                "intermediate_sub_code_2",
                "intermediate_atd_2",
                "frt_code_2",
                "intermediate_id_3",
                "intermediate_region_3",
                "intermediate_sec_code_3",
                "intermediate_sub_code_3",
                "intermediate_atd_3",
                "frt_code_3",
                "intermediate_id_4",
                "intermediate_region_4",
                "intermediate_sec_code_4",
                "intermediate_sub_code_4",
                "intermediate_atd_4",
                "frt_code_4",
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
            "intermediate_id_1": self.intermediate_id_1,
            "intermediate_region_1": self.intermediate_region_1,
            "intermediate_sec_code_1": self.intermediate_sec_code_1,
            "intermediate_sub_code_1": self.intermediate_sub_code_1,
            "intermediate_atd_1": self.intermediate_atd_1,
            "frt_code_1": self.frt_code_1,
            "intermediate_id_2": self.intermediate_id_2,
            "intermediate_region_2": self.intermediate_region_2,
            "intermediate_sec_code_2": self.intermediate_sec_code_2,
            "intermediate_sub_code_2": self.intermediate_sub_code_2,
            "intermediate_atd_2": self.intermediate_atd_2,
            "frt_code_2": self.frt_code_2,
            "intermediate_id_3": self.intermediate_id_3,
            "intermediate_region_3": self.intermediate_region_3,
            "intermediate_sec_code_3": self.intermediate_sec_code_3,
            "intermediate_sub_code_3": self.intermediate_sub_code_3,
            "intermediate_atd_3": self.intermediate_atd_3,
            "frt_code_3": self.frt_code_3,
            "intermediate_id_4": self.intermediate_id_4,
            "intermediate_region_4": self.intermediate_region_4,
            "intermediate_sec_code_4": self.intermediate_sec_code_4,
            "intermediate_sub_code_4": self.intermediate_sub_code_4,
            "intermediate_atd_4": self.intermediate_atd_4,
            "frt_code_4": self.frt_code_4,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
