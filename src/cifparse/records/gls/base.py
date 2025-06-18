from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    fac_id: str
    fac_region: str
    sub_code: str
    gls_ref_id: str
    gls_cat: str
    record_number: int
    cycle_data: str

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.st = None
        self.area = None
        self.sec_code = None
        self.fac_id = None
        self.fac_region = None
        self.sub_code = None
        self.gls_ref_id = None
        self.gls_cat = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.fac_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.fac_id = extract_field(line, w_bas.fac_id)
        self.fac_region = extract_field(line, w_bas.fac_region)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.gls_ref_id = extract_field(line, w_bas.gls_ref_id)
        self.gls_cat = extract_field(line, w_bas.gls_cat)
        self.record_number = extract_field(line, w_bas.record_number)
        self.cycle_data = extract_field(line, w_bas.cycle_data)
        return self

    def ordered_leading(self) -> list:
        return [
            "st",
            "area",
            "sec_code",
            "fac_id",
            "fac_region",
            "sub_code",
            "gls_ref_id",
            "gls_cat",
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
            "fac_id": self.fac_id,
            "fac_region": self.fac_region,
            "sub_code": self.sub_code,
            "gls_ref_id": self.gls_ref_id,
            "gls_cat": self.gls_cat,
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
