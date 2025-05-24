from cifparse.functions.field import clean_value, extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    sub_code: str
    fir_rdo_id: str
    fir_uir_addr: str
    fir_uir_ind: str
    remote_site_name: str
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
        self.sub_code = None
        self.fir_rdo_id = None
        self.fir_uir_addr = None
        self.fir_uir_ind = None
        self.remote_site_name = None
        self.comm_type = None
        self.comm_freq = None
        self.gt = None
        self.freq_unit = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.fir_rdo_id}, {self.comm_freq}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.fir_rdo_id = extract_field(line, w_bas.fir_rdo_id)
        self.fir_uir_addr = extract_field(line, w_bas.fir_uir_addr)
        self.fir_uir_ind = extract_field(line, w_bas.fir_uir_ind)
        self.remote_site_name = extract_field(line, w_bas.remote_site_name)
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
            "sub_code",
            "fir_rdo_id",
            "fir_uir_addr",
            "fir_uir_ind",
            "remote_site_name",
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
            "st": clean_value(self.st),
            "area": clean_value(self.area),
            "sec_code": clean_value(self.sec_code),
            "sub_code": clean_value(self.sub_code),
            "fir_rdo_id": clean_value(self.fir_rdo_id),
            "fir_uir_addr": clean_value(self.fir_uir_addr),
            "fir_uir_ind": clean_value(self.fir_uir_ind),
            "remote_site_name": clean_value(self.remote_site_name),
            "comm_type": clean_value(self.comm_type),
            "comm_freq": clean_value(self.comm_freq),
            "gt": clean_value(self.gt),
            "freq_unit": clean_value(self.freq_unit),
        }

    def get_trailing_dict(self) -> dict:
        return {
            "record_number": clean_value(self.record_number),
            "cycle_data": clean_value(self.cycle_data),
        }

    def to_dict(self) -> dict:
        leading = self.get_leading_dict()
        trailing = self.get_trailing_dict()
        return {**leading, **trailing}
