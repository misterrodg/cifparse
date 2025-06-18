from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pla


class Planning(Base):
    cont_rec_no: int
    application: str
    se_ind: str
    se_date: str
    rest_1_region: str
    rest_1_type: str
    rest_1_designation: str
    rest_1_mult_code: str
    rest_2_region: str
    rest_2_type: str
    rest_2_designation: str
    rest_2_mult_code: str
    rest_3_region: str
    rest_3_type: str
    rest_3_designation: str
    rest_3_mult_code: str
    rest_4_region: str
    rest_4_type: str
    rest_4_designation: str
    rest_4_mult_code: str
    linked_record: str

    def __init__(self):
        super().__init__("airway_plannings")
        self.cont_rec_no = None
        self.application = None
        self.se_ind = None
        self.se_date = None
        self.rest_1_region = None
        self.rest_1_type = None
        self.rest_1_designation = None
        self.rest_1_mult_code = None
        self.rest_2_region = None
        self.rest_2_type = None
        self.rest_2_designation = None
        self.rest_2_mult_code = None
        self.rest_3_region = None
        self.rest_3_type = None
        self.rest_3_designation = None
        self.rest_3_mult_code = None
        self.rest_4_region = None
        self.rest_4_type = None
        self.rest_4_designation = None
        self.rest_4_mult_code = None
        self.linked_record = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airway_id}, {self.point_id}"

    def from_line(self, line: str) -> "Planning":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pla.cont_rec_no)
        self.application = extract_field(line, w_pla.application)
        self.se_ind = extract_field(line, w_pla.se_ind)
        self.se_date = extract_field(line, w_pla.se_date)
        self.rest_1_region = extract_field(line, w_pla.rest_1_region)
        self.rest_1_type = extract_field(line, w_pla.rest_1_type)
        self.rest_1_designation = extract_field(line, w_pla.rest_1_designation)
        self.rest_1_mult_code = extract_field(line, w_pla.rest_1_mult_code)
        self.rest_2_region = extract_field(line, w_pla.rest_2_region)
        self.rest_2_type = extract_field(line, w_pla.rest_2_type)
        self.rest_2_designation = extract_field(line, w_pla.rest_2_designation)
        self.rest_2_mult_code = extract_field(line, w_pla.rest_2_mult_code)
        self.rest_3_region = extract_field(line, w_pla.rest_3_region)
        self.rest_3_type = extract_field(line, w_pla.rest_3_type)
        self.rest_3_designation = extract_field(line, w_pla.rest_3_designation)
        self.rest_3_mult_code = extract_field(line, w_pla.rest_3_mult_code)
        self.rest_4_region = extract_field(line, w_pla.rest_4_region)
        self.rest_4_type = extract_field(line, w_pla.rest_4_type)
        self.rest_4_designation = extract_field(line, w_pla.rest_4_designation)
        self.rest_4_mult_code = extract_field(line, w_pla.rest_4_mult_code)
        self.linked_record = extract_field(line, w_pla.linked_record)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "se_ind",
                "se_date",
                "rest_1_region",
                "rest_1_type",
                "rest_1_designation",
                "rest_1_mult_code",
                "rest_2_region",
                "rest_2_type",
                "rest_2_designation",
                "rest_2_mult_code",
                "rest_3_region",
                "rest_3_type",
                "rest_3_designation",
                "rest_3_mult_code",
                "rest_4_region",
                "rest_4_type",
                "rest_4_designation",
                "rest_4_mult_code",
                "linked_record",
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
            "se_ind": self.se_ind,
            "se_date": self.se_date,
            "rest_1_region": self.rest_1_region,
            "rest_1_type": self.rest_1_type,
            "rest_1_designation": self.rest_1_designation,
            "rest_1_mult_code": self.rest_1_mult_code,
            "rest_2_region": self.rest_2_region,
            "rest_2_type": self.rest_2_type,
            "rest_2_designation": self.rest_2_designation,
            "rest_2_mult_code": self.rest_2_mult_code,
            "rest_3_region": self.rest_3_region,
            "rest_3_type": self.rest_3_type,
            "rest_3_designation": self.rest_3_designation,
            "rest_3_mult_code": self.rest_3_mult_code,
            "rest_4_region": self.rest_4_region,
            "rest_4_type": self.rest_4_type,
            "rest_4_designation": self.rest_4_designation,
            "rest_4_mult_code": self.rest_4_mult_code,
            "linked_record": self.linked_record,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
