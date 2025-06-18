from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_not


class NotePrimary(Base):
    cont_rec_no: int
    start_point_id: str
    start_point_region: str
    start_point_sec_code: str
    start_point_sub_code: str
    end_point_id: str
    end_point_region: str
    end_point_sec_code: str
    end_point_sub_code: str
    start_date: str
    end_date: str
    notes: str

    def __init__(self):
        super().__init__("restriction_notes")
        self.cont_rec_no = None
        self.start_point_id = None
        self.start_point_region = None
        self.start_point_sec_code = None
        self.start_point_sub_code = None
        self.end_point_id = None
        self.end_point_region = None
        self.end_point_sec_code = None
        self.end_point_sub_code = None
        self.start_date = None
        self.end_date = None
        self.notes = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.route_id}, {self.rest_id}"

    def from_line(self, line: str) -> "NotePrimary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_not.cont_rec_no)
        self.start_point_id = extract_field(line, w_not.start_point_id)
        self.start_point_region = extract_field(line, w_not.end_point_region)
        self.start_point_sec_code = extract_field(line, w_not.end_point_sec_code)
        self.start_point_sub_code = extract_field(line, w_not.end_point_sub_code)
        self.end_point_id = extract_field(line, w_not.end_point_id)
        self.end_point_region = extract_field(line, w_not.end_point_region)
        self.end_point_sec_code = extract_field(line, w_not.end_point_sec_code)
        self.end_point_sub_code = extract_field(line, w_not.end_point_sub_code)
        self.start_date = extract_field(line, w_not.start_date)
        self.end_date = extract_field(line, w_not.end_date)
        self.notes = extract_field(line, w_not.notes)
        return self

    def ordered_fields(self):
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "start_point_id",
                "start_point_region",
                "start_point_sec_code",
                "start_point_sub_code",
                "end_point_id",
                "end_point_region",
                "end_point_sec_code",
                "end_point_sub_code",
                "start_date",
                "end_date",
                "notes",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "start_point_id": self.start_point_id,
            "start_point_region": self.start_point_region,
            "start_point_sec_code": self.start_point_sec_code,
            "start_point_sub_code": self.start_point_sub_code,
            "end_point_id": self.end_point_id,
            "end_point_region": self.end_point_region,
            "end_point_sec_code": self.end_point_sec_code,
            "end_point_sub_code": self.end_point_sub_code,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "notes": self.notes,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
