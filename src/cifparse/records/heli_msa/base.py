from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    heliport_id: str
    heliport_region: str
    sub_code: str
    msa_center: str
    msa_center_region: str
    msa_center_sec_code: str
    msa_center_sub_code: str
    mult_code: str
    record_number: int
    cycle_data: str

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.st = None
        self.area = None
        self.sec_code = None
        self.heliport_id = None
        self.heliport_region = None
        self.sub_code = None
        self.msa_center = None
        self.msa_center_region = None
        self.msa_center_sec_code = None
        self.msa_center_sub_code = None
        self.mult_code = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.heliport_id}, {self.msa_center}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.heliport_id = extract_field(line, w_bas.heliport_id)
        self.heliport_region = extract_field(line, w_bas.heliport_region)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.msa_center = extract_field(line, w_bas.msa_center)
        self.msa_center_region = extract_field(line, w_bas.msa_center_region)
        self.msa_center_sec_code = extract_field(line, w_bas.msa_center_sec_code)
        self.msa_center_sub_code = extract_field(line, w_bas.msa_center_sub_code)
        self.mult_code = extract_field(line, w_bas.mult_code)
        self.record_number = extract_field(line, w_bas.record_number)
        self.cycle_data = extract_field(line, w_bas.cycle_data)
        return self

    def ordered_leading(self) -> list:
        return [
            "st",
            "area",
            "sec_code",
            "heliport_id",
            "heliport_region",
            "sub_code",
            "msa_center",
            "msa_center_region",
            "msa_center_sec_code",
            "msa_center_sub_code",
            "mult_code",
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
            "heliport_id": self.heliport_id,
            "heliport_region": self.heliport_region,
            "sub_code": self.sub_code,
            "msa_center": self.msa_center,
            "msa_center_region": self.msa_center_region,
            "msa_center_sec_code": self.msa_center_sec_code,
            "msa_center_sub_code": self.msa_center_sub_code,
            "mult_code": self.mult_code,
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
