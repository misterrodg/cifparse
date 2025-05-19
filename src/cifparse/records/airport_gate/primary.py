from cifparse.functions.record import (
    clean_value,
    convert_lat_dms,
    convert_lon_dms,
    convert_mag_hdg,
    extract_field,
    translate_cont_rec_no,
)

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    lat: float
    lon: float
    mag_hdg: float
    gate_name: str

    def __init__(self):
        super().__init__("airport_gates")
        self.cont_rec_no = None
        self.lat = None
        self.lon = None
        self.mag_hdg = None
        self.gate_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.gate_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = translate_cont_rec_no(extract_field(line, w_pri.cont_rec_no))
        self.lat = convert_lat_dms(extract_field(line, w_pri.lat))
        self.lon = convert_lon_dms(extract_field(line, w_pri.lon))
        self.mag_hdg = convert_mag_hdg(extract_field(line, w_pri.mag_hdg))
        self.gate_name = extract_field(line, w_pri.gate_name)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "lat",
                "lon",
                "mag_hdg",
                "gate_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": clean_value(self.cont_rec_no),
            "lat": clean_value(self.lat),
            "lon": clean_value(self.lon),
            "mag_hdg": clean_value(self.mag_hdg),
            "gate_name": clean_value(self.gate_name),
        }
        return {**leading_dict, **this_dict, **trailing_dict}
