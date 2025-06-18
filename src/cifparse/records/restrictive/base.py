from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    sub_code: str
    region: str
    restrictive_type: str
    restrictive_id: str
    mult_code: str
    seq_no: int
    record_number: int
    cycle_data: str

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.st = None
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.region = None
        self.restrictive_type = None
        self.restrictive_id = None
        self.mult_code = None
        self.seq_no = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.restrictive_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.region = extract_field(line, w_bas.region)
        self.restrictive_type = extract_field(line, w_bas.restrictive_type)
        self.restrictive_id = extract_field(line, w_bas.restrictive_id)
        self.mult_code = extract_field(line, w_bas.mult_code)
        self.seq_no = extract_field(line, w_bas.seq_no)
        self.record_number = extract_field(line, w_bas.record_number)
        self.cycle_data = extract_field(line, w_bas.cycle_data)
        return self

    def ordered_leading(self) -> list:
        return [
            "st",
            "area",
            "sec_code",
            "sub_code",
            "region",
            "restrictive_type",
            "restrictive_id",
            "mult_code",
            "seq_no",
        ]

    def ordered_trailing(self) -> list:
        return [
            "record_number",
            "cycle_data",
        ]

    def ordered_fields(self) -> dict:
        result = []
        result.extend(self.ordered_leading())
        result.extend(self.ordered_trailing())
        return result

    def get_leading_dict(self) -> dict:
        return {
            "st": self.st,
            "area": self.area,
            "sec_code": self.sec_code,
            "sub_code": self.sub_code,
            "region": self.region,
            "restrictive_type": self.restrictive_type,
            "restrictive_id": self.restrictive_id,
            "mult_code": self.mult_code,
            "seq_no": self.seq_no,
        }

    def get_trailing_dict(self) -> dict:
        return {
            "record_number": self.record_number,
            "cycle_data": self.cycle_data,
        }

    def to_dict(self) -> dict:
        leading = self.get_leading_dict()
        trailing = self.get_trailing_dict()
        return {**leading, **trailing}
