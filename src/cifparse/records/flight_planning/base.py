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
    procedure_id: str
    procedure_type: str
    runway_transition_id: str
    runway_transition_point: str
    runway_transition_region: str
    runway_transition_sec_code: str
    runway_transition_sub_code: str
    runway_transition_atd: str
    common_point: str
    common_point_region: str
    common_point_sec_code: str
    common_point_sub_code: str
    common_point_atd: str
    enroute_transition_id: str
    enroute_transition_point: str
    enroute_transition_region: str
    enroute_transition_sec_code: str
    enroute_transition_sub_code: str
    enroute_transition_atd: str
    seq_no: int
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
        self.procedure_id = None
        self.procedure_type = None
        self.runway_transition_id = None
        self.runway_transition_point = None
        self.runway_transition_region = None
        self.runway_transition_sec_code = None
        self.runway_transition_sub_code = None
        self.runway_transition_atd = None
        self.common_point = None
        self.common_point_region = None
        self.common_point_sec_code = None
        self.common_point_sub_code = None
        self.common_point_atd = None
        self.enroute_transition_id = None
        self.enroute_transition_point = None
        self.enroute_transition_region = None
        self.enroute_transition_sec_code = None
        self.enroute_transition_sub_code = None
        self.enroute_transition_atd = None
        self.seq_no = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.procedure_type}, {self.procedure_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.airport_id = extract_field(line, w_bas.airport_id)
        self.airport_region = extract_field(line, w_bas.airport_region)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.procedure_id = extract_field(line, w_bas.procedure_id)
        self.procedure_type = extract_field(line, w_bas.procedure_type)
        self.runway_transition_id = extract_field(line, w_bas.runway_transition_id)
        self.runway_transition_point = extract_field(
            line, w_bas.runway_transition_point
        )
        self.runway_transition_region = extract_field(
            line, w_bas.runway_transition_region
        )
        self.runway_transition_sec_code = extract_field(
            line, w_bas.runway_transition_sec_code
        )
        self.runway_transition_sub_code = extract_field(
            line, w_bas.runway_transition_sub_code
        )
        self.runway_transition_atd = extract_field(line, w_bas.runway_transition_atd)
        self.common_point = extract_field(line, w_bas.common_point)
        self.common_point_region = extract_field(line, w_bas.common_point_region)
        self.common_point_sec_code = extract_field(line, w_bas.common_point_sec_code)
        self.common_point_sub_code = extract_field(line, w_bas.common_point_sub_code)
        self.common_point_atd = extract_field(line, w_bas.common_point_atd)
        self.enroute_transition_id = extract_field(line, w_bas.enroute_transition_id)
        self.enroute_transition_point = extract_field(
            line, w_bas.enroute_transition_point
        )
        self.enroute_transition_region = extract_field(
            line, w_bas.enroute_transition_region
        )
        self.enroute_transition_sec_code = extract_field(
            line, w_bas.enroute_transition_sec_code
        )
        self.enroute_transition_sub_code = extract_field(
            line, w_bas.enroute_transition_sub_code
        )
        self.enroute_transition_atd = extract_field(line, w_bas.enroute_transition_atd)
        self.seq_no = extract_field(line, w_bas.seq_no)
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
            "procedure_id",
            "procedure_type",
            "runway_transition_id",
            "runway_transition_point",
            "runway_transition_region",
            "runway_transition_sec_code",
            "runway_transition_sub_code",
            "runway_transition_atd",
            "common_point",
            "common_point_region",
            "common_point_sec_code",
            "common_point_sub_code",
            "common_point_atd",
            "enroute_transition_id",
            "enroute_transition_point",
            "enroute_transition_region",
            "enroute_transition_sec_code",
            "enroute_transition_sub_code",
            "enroute_transition_atd",
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
            "airport_id": self.airport_id,
            "airport_region": self.airport_region,
            "sub_code": self.sub_code,
            "procedure_id": self.procedure_id,
            "procedure_type": self.procedure_type,
            "runway_transition_id": self.runway_transition_id,
            "runway_transition_point": self.runway_transition_point,
            "runway_transition_region": self.runway_transition_region,
            "runway_transition_sec_code": self.runway_transition_sec_code,
            "runway_transition_sub_code": self.runway_transition_sub_code,
            "runway_transition_atd": self.runway_transition_atd,
            "common_point": self.common_point,
            "common_point_region": self.common_point_region,
            "common_point_sec_code": self.common_point_sec_code,
            "common_point_sub_code": self.common_point_sub_code,
            "common_point_atd": self.common_point_atd,
            "enroute_transition_id": self.enroute_transition_id,
            "enroute_transition_point": self.enroute_transition_point,
            "enroute_transition_region": self.enroute_transition_region,
            "enroute_transition_sec_code": self.enroute_transition_sec_code,
            "enroute_transition_sub_code": self.enroute_transition_sub_code,
            "enroute_transition_atd": self.enroute_transition_atd,
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
