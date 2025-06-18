from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    fac_id: str
    fac_region: str
    fac_sub_code: str
    procedure_id: str
    procedure_type: str
    transition_id: str
    seq_no: int
    fix_id: str
    fix_region: str
    fix_sec_code: str
    fix_sub_code: str
    record_number: int
    cycle_data: str

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.st = None
        self.area = None
        self.sec_code = None
        self.fac_id = None
        self.fac_region = None
        self.fac_sub_code = None
        self.procedure_id = None
        self.procedure_type = None
        self.transition_id = None
        self.seq_no = None
        self.fix_id = None
        self.fix_region = None
        self.fix_sec_code = None
        self.fix_sub_code = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.fac_id}, {self.procedure_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.fac_id = extract_field(line, w_bas.fac_id)
        self.fac_region = extract_field(line, w_bas.fac_region)
        self.fac_sub_code = extract_field(line, w_bas.fac_sub_code)
        self.procedure_id = extract_field(line, w_bas.procedure_id)
        self.procedure_type = extract_field(line, w_bas.procedure_type)
        self.transition_id = extract_field(line, w_bas.transition_id)
        self.seq_no = extract_field(line, w_bas.seq_no)
        self.fix_id = extract_field(line, w_bas.fix_id)
        self.fix_region = extract_field(line, w_bas.fix_region)
        self.fix_sec_code = extract_field(line, w_bas.fix_sec_code)
        self.fix_sub_code = extract_field(line, w_bas.fix_sub_code)
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
            "fac_sub_code",
            "procedure_id",
            "procedure_type",
            "transition_id",
            "seq_no",
            "fix_id",
            "fix_region",
            "fix_sec_code",
            "fix_sub_code",
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
            "fac_sub_code": self.fac_sub_code,
            "procedure_id": self.procedure_id,
            "procedure_type": self.procedure_type,
            "transition_id": self.transition_id,
            "seq_no": self.seq_no,
            "fix_id": self.fix_id,
            "fix_region": self.fix_region,
            "fix_sec_code": self.fix_sec_code,
            "fix_sub_code": self.fix_sub_code,
        }

    def get_trailing_dict(self) -> dict:
        return {
            "record_number": self.record_number,
            "cycle_data": self.cycle_data,
        }

    def to_dict(self) -> dict:
        leading = self.get_leading_dict()
        trailing = self.get_trailing_dict
        return {**leading, **trailing}
