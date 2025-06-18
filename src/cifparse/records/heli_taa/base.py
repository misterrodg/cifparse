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
    iap_id: str
    taa_si: str
    procedure_turn: str
    iaf_point_id: str
    iaf_point_region: str
    iaf_point_sec_code: str
    iaf_point_sub_code: str
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
        self.iap_id = None
        self.taa_si = None
        self.procedure_turn = None
        self.iaf_point_id = None
        self.iaf_point_region = None
        self.iaf_point_sec_code = None
        self.iaf_point_sub_code = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.heliport_id}, {self.iap_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.heliport_id = extract_field(line, w_bas.heliport_id)
        self.heliport_region = extract_field(line, w_bas.heliport_region)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.iap_id = extract_field(line, w_bas.iap_id)
        self.taa_si = extract_field(line, w_bas.taa_si)
        self.procedure_turn = extract_field(line, w_bas.procedure_turn)
        self.iaf_point_id = extract_field(line, w_bas.iaf_point_id)
        self.iaf_point_region = extract_field(line, w_bas.iaf_point_region)
        self.iaf_point_sec_code = extract_field(line, w_bas.iaf_point_sec_code)
        self.iaf_point_sub_code = extract_field(line, w_bas.iaf_point_sub_code)
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
            "iap_id",
            "taa_si",
            "procedure_turn",
            "iaf_point_id",
            "iaf_point_region",
            "iaf_point_sec_code",
            "iaf_point_sub_code",
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
            "iap_id": self.iap_id,
            "taa_si": self.taa_si,
            "procedure_turn": self.procedure_turn,
            "iaf_point_id": self.iaf_point_id,
            "iaf_point_region": self.iaf_point_region,
            "iaf_point_sec_code": self.iaf_point_sec_code,
            "iaf_point_sub_code": self.iaf_point_sub_code,
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
