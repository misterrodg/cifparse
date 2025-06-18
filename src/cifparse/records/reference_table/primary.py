from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: str
    pref_route_id_1: str
    et_ind_1: str
    pref_route_id_2: str
    et_ind_2: str
    pref_route_id_3: str
    et_ind_3: str
    pref_route_id_4: str
    et_ind_4: str
    pref_route_id_5: str
    et_ind_5: str
    pref_route_id_6: str
    et_ind_6: str

    def __init__(self):
        super().__init__("reference_tables")
        self.cont_rec_no = None
        self.pref_route_id_1 = None
        self.et_ind_1 = None
        self.pref_route_id_2 = None
        self.et_ind_2 = None
        self.pref_route_id_3 = None
        self.et_ind_3 = None
        self.pref_route_id_4 = None
        self.et_ind_4 = None
        self.pref_route_id_5 = None
        self.et_ind_5 = None
        self.pref_route_id_6 = None
        self.et_ind_6 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.geo_entity}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.pref_route_id_1 = extract_field(line, w_pri.pref_route_id_1)
        self.et_ind_1 = extract_field(line, w_pri.et_ind_1)
        self.pref_route_id_2 = extract_field(line, w_pri.pref_route_id_2)
        self.et_ind_2 = extract_field(line, w_pri.et_ind_2)
        self.pref_route_id_3 = extract_field(line, w_pri.pref_route_id_3)
        self.et_ind_3 = extract_field(line, w_pri.et_ind_3)
        self.pref_route_id_4 = extract_field(line, w_pri.pref_route_id_4)
        self.et_ind_4 = extract_field(line, w_pri.et_ind_4)
        self.pref_route_id_5 = extract_field(line, w_pri.pref_route_id_5)
        self.et_ind_5 = extract_field(line, w_pri.et_ind_5)
        self.pref_route_id_6 = extract_field(line, w_pri.pref_route_id_6)
        self.et_ind_6 = extract_field(line, w_pri.et_ind_6)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "pref_route_id_1",
                "et_ind_1",
                "pref_route_id_2",
                "et_ind_2",
                "pref_route_id_3",
                "et_ind_3",
                "pref_route_id_4",
                "et_ind_4",
                "pref_route_id_5",
                "et_ind_5",
                "pref_route_id_6",
                "et_ind_6",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "pref_route_id_1": self.pref_route_id_1,
            "et_ind_1": self.et_ind_1,
            "pref_route_id_2": self.pref_route_id_2,
            "et_ind_2": self.et_ind_2,
            "pref_route_id_3": self.pref_route_id_3,
            "et_ind_3": self.et_ind_3,
            "pref_route_id_4": self.pref_route_id_4,
            "et_ind_4": self.et_ind_4,
            "pref_route_id_5": self.pref_route_id_5,
            "et_ind_5": self.et_ind_5,
            "pref_route_id_6": self.pref_route_id_6,
            "et_ind_6": self.et_ind_6,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
