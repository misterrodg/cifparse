from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    airport_id: str
    airport_region: str
    sub_code: str
    comm_type: str
    comm_freq: float
    gt: str
    freq_unit: str
    record_number: int
    cycle_data: str

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.st = None
        self.area = None
        self.sec_code = None
        self.airport_id = None
        self.airport_region = None
        self.sub_code = None
        self.comm_type = None
        self.comm_freq = None
        self.gt = None
        self.freq_unit = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.comm_freq}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.airport_id = extract_field(line, w_bas.airport_id)
        self.airport_region = extract_field(line, w_bas.airport_region)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.comm_type = extract_field(line, w_bas.comm_type)
        self.comm_freq = extract_field(line, w_bas.comm_freq, self.comm_type)
        self.gt = extract_field(line, w_bas.gt)
        self.freq_unit = extract_field(line, w_bas.freq_unit)
        self.record_number = extract_field(line, w_bas.record_number)
        self.cycle_data = extract_field(line, w_bas.cycle_data)
        return self

    def ordered_leading(self) -> list:
        return [
            "st",
            "area",
            "sec_code",
            "airport_id",
            "airport_region",
            "sub_code",
            "comm_type",
            "comm_freq",
            "gt",
            "freq_unit",
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
            "airport_id": self.airport_id,
            "airport_region": self.airport_region,
            "sub_code": self.sub_code,
            "comm_type": self.comm_type,
            "comm_freq": self.comm_freq,
            "gt": self.gt,
            "freq_unit": self.freq_unit,
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
