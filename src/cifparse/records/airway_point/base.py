from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    sub_code: str
    airway_id: str
    six_char: str
    seq_no: int
    point_id: str
    point_region: str
    point_sec_code: str
    point_sub_code: str
    record_number: int
    cycle_data: str

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.st = None
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.airway_id = None
        self.six_char = None
        self.seq_no = None
        self.point_id = None
        self.point_region = None
        self.point_sec_code = None
        self.point_sub_code = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airway_id}, {self.point_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.airway_id = extract_field(line, w_bas.airway_id)
        self.six_char = extract_field(line, w_bas.six_char)
        self.seq_no = extract_field(line, w_bas.seq_no)
        self.point_id = extract_field(line, w_bas.point_id)
        self.point_region = extract_field(line, w_bas.point_region)
        self.point_sec_code = extract_field(line, w_bas.point_sec_code)
        self.point_sub_code = extract_field(line, w_bas.point_sub_code)
        self.record_number = extract_field(line, w_bas.record_number)
        self.cycle_data = extract_field(line, w_bas.cycle_data)
        return self

    def ordered_leading(self) -> list:
        return [
            "st",
            "area",
            "sec_code",
            "sub_code",
            "airway_id",
            "six_char",
            "seq_no",
            "point_id",
            "point_region",
            "point_sec_code",
            "point_sub_code",
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
            "airway_id": self.airway_id,
            "six_char": self.six_char,
            "seq_no": self.seq_no,
            "point_id": self.point_id,
            "point_region": self.point_region,
            "point_sec_code": self.point_sec_code,
            "point_sub_code": self.point_sub_code,
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
