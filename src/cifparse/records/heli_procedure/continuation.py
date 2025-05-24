from cifparse.functions.field import clean_value, extract_field

from .base import Base
from .widths import w_con


class Continuation(Base):
    cont_rec_no: int
    application: str
    dh_cat_a: int
    dh_cat_b: int
    dh_cat_c: int
    dh_cat_d: int
    mda_cat_a: int
    mda_cat_b: int
    mda_cat_c: int
    mda_cat_d: int
    tch: int
    alt_desc: str
    loc_alt: int
    vert_angle: float
    rnp: str
    rte_qual_1: str
    rte_qual_2: str

    def __init__(self):
        super().__init__("heli_procedure_point_continuations")
        self.cont_rec_no = None
        self.application = None
        self.dh_cat_a = None
        self.dh_cat_b = None
        self.dh_cat_c = None
        self.dh_cat_d = None
        self.mda_cat_a = None
        self.mda_cat_b = None
        self.mda_cat_c = None
        self.mda_cat_d = None
        self.tch = None
        self.alt_desc = None
        self.loc_alt = None
        self.vert_angle = None
        self.rnp = None
        self.rte_qual_1 = None
        self.rte_qual_2 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.procedure_id}"

    def from_line(self, line: str) -> "Continuation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_con.cont_rec_no)
        self.application = extract_field(line, w_con.application)
        self.dh_cat_a = extract_field(line, w_con.dh_cat_a)
        self.dh_cat_b = extract_field(line, w_con.dh_cat_b)
        self.dh_cat_c = extract_field(line, w_con.dh_cat_c)
        self.dh_cat_d = extract_field(line, w_con.dh_cat_d)
        self.mda_cat_a = extract_field(line, w_con.mda_cat_a)
        self.mda_cat_b = extract_field(line, w_con.mda_cat_b)
        self.mda_cat_c = extract_field(line, w_con.mda_cat_c)
        self.mda_cat_d = extract_field(line, w_con.mda_cat_d)
        self.tch = extract_field(line, w_con.tch)
        self.alt_desc = extract_field(line, w_con.alt_desc)
        self.loc_alt = extract_field(line, w_con.loc_alt)
        self.vert_angle = extract_field(line, w_con.vert_angle)
        self.rnp = extract_field(line, w_con.rnp)
        self.rte_qual_1 = extract_field(line, w_con.rte_qual_1)
        self.rte_qual_2 = extract_field(line, w_con.rte_qual_2)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "dh_cat_a",
                "dh_cat_b",
                "dh_cat_c",
                "dh_cat_d",
                "mda_cat_a",
                "mda_cat_b",
                "mda_cat_c",
                "mda_cat_d",
                "tch",
                "alt_desc",
                "loc_alt",
                "vert_angle",
                "rnp",
                "rte_qual_1",
                "rte_qual_2",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": clean_value(self.cont_rec_no),
            "application": clean_value(self.application),
            "dh_cat_a": clean_value(self.dh_cat_a),
            "dh_cat_b": clean_value(self.dh_cat_b),
            "dh_cat_c": clean_value(self.dh_cat_c),
            "dh_cat_d": clean_value(self.dh_cat_d),
            "mda_cat_a": clean_value(self.mda_cat_a),
            "mda_cat_b": clean_value(self.mda_cat_b),
            "mda_cat_c": clean_value(self.mda_cat_c),
            "mda_cat_d": clean_value(self.mda_cat_d),
            "tch": clean_value(self.tch),
            "alt_desc": clean_value(self.alt_desc),
            "loc_alt": clean_value(self.loc_alt),
            "vert_angle": clean_value(self.vert_angle),
            "rnp": clean_value(self.rnp),
            "rte_qual_1": clean_value(self.rte_qual_1),
            "rte_qual_2": clean_value(self.rte_qual_2),
        }
        return {**leading_dict, **this_dict, **trailing_dict}
