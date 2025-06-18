from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    sub_code: str
    from_1: str
    from_region_1: str
    from_sec_code_1: str
    from_sub_code_1: str
    from_2: str
    from_region_2: str
    from_sec_code_2: str
    from_sub_code_2: str
    company_route_id: str
    seq_no: int
    record_number: int
    cycle_data: str

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.st = None
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.from_1 = None
        self.from_region_1 = None
        self.from_sec_code_1 = None
        self.from_sub_code_1 = None
        self.from_2 = None
        self.from_region_2 = None
        self.from_sec_code_2 = None
        self.from_sub_code_2 = None
        self.company_route_id = None
        self.seq_no = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.company_route_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.from_1 = extract_field(line, w_bas.from_1)
        self.from_region_1 = extract_field(line, w_bas.from_region_1)
        self.from_sec_code_1 = extract_field(line, w_bas.from_sec_code_1)
        self.from_sub_code_1 = extract_field(line, w_bas.from_sub_code_1)
        self.from_2 = extract_field(line, w_bas.from_2)
        self.from_region_2 = extract_field(line, w_bas.from_region_2)
        self.from_sec_code_2 = extract_field(line, w_bas.from_sec_code_2)
        self.from_sub_code_2 = extract_field(line, w_bas.from_sub_code_2)
        self.company_route_id = extract_field(line, w_bas.company_route_id)
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
            "from_1",
            "from_region_1",
            "from_sec_code_1",
            "from_sub_code_1",
            "from_2",
            "from_region_2",
            "from_sec_code_2",
            "from_sub_code_2",
            "company_route_id",
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
            "from_1": self.from_1,
            "from_region_1": self.from_region_1,
            "from_sec_code_1": self.from_sec_code_1,
            "from_sub_code_1": self.from_sub_code_1,
            "from_2": self.from_2,
            "from_region_2": self.from_region_2,
            "from_sec_code_2": self.from_sec_code_2,
            "from_sub_code_2": self.from_sub_code_2,
            "company_route_id": self.company_route_id,
            "seq_no": self.seq_no,
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
