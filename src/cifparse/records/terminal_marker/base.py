from cifparse.functions.field import extract_field
from cifparse.records.table_base import TableBase

from .widths import w_bas


class Base(TableBase):
    st: str
    area: str
    sec_code: str
    facility_id: str
    facility_region: str
    sub_code: str
    loc_id: str
    marker_type: str
    record_number: int
    cycle_data: str

    def __init__(self, table_name: str):
        super().__init__(table_name)
        self.st = None
        self.area = None
        self.sec_code = None
        self.facility_id = None
        self.facility_region = None
        self.sub_code = None
        self.loc_id = None
        self.marker_type = None
        self.record_number = None
        self.cycle_data = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.facility_id}, {self.loc_id}"

    def from_line(self, line: str) -> "Base":
        self.st = extract_field(line, w_bas.st)
        self.area = extract_field(line, w_bas.area)
        self.sec_code = extract_field(line, w_bas.sec_code)
        self.facility_id = extract_field(line, w_bas.facility_id)
        self.facility_region = extract_field(line, w_bas.facility_region)
        self.sub_code = extract_field(line, w_bas.sub_code)
        self.loc_id = extract_field(line, w_bas.loc_id)
        self.marker_type = extract_field(line, w_bas.marker_type, False)
        self.record_number = extract_field(line, w_bas.record_number)
        self.cycle_data = extract_field(line, w_bas.cycle_data)
        return self

    def ordered_leading(self) -> list:
        return [
            "st",
            "area",
            "sec_code",
            "facility_id",
            "facility_region",
            "sub_code",
            "loc_id",
            "marker_type",
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
            "facility_id": self.facility_id,
            "facility_region": self.facility_region,
            "sub_code": self.sub_code,
            "loc_id": self.loc_id,
            "marker_type": self.marker_type,
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
