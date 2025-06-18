from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    sub_code: str
    center_region: str
    airspace_type: str
    center_id: str
    center_sec_code: str
    center_sub_code: str
    airspace_class: str
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
        self.center_region = None
        self.airspace_type = None
        self.center_id = None
        self.center_sec_code = None
        self.center_sub_code = None
        self.airspace_class = None
        self.mult_code = None
        self.seq_no = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.center_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.center_region = extract_field(line, w_bas.center_region)
        self.airspace_type = extract_field(line, w_bas.airspace_type)
        self.center_id = extract_field(line, w_bas.center_id)
        self.center_sec_code = extract_field(line, w_bas.center_sec_code)
        self.center_sub_code = extract_field(line, w_bas.center_sub_code)
        self.airspace_class = extract_field(line, w_bas.airspace_class)
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
            "center_region",
            "airspace_type",
            "center_id",
            "center_sec_code",
            "center_sub_code",
            "airspace_class",
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
            "center_region": self.center_region,
            "airspace_type": self.airspace_type,
            "center_id": self.center_id,
            "center_sec_code": self.center_sec_code,
            "center_sub_code": self.center_sub_code,
            "airspace_class": self.airspace_class,
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
