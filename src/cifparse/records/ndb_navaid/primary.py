from cifparse.functions.field import clean_value, extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    frequency: float
    nav_class: str
    lat: float
    lon: float
    mag_var: float
    datum_code: str
    ndb_name: str

    def __init__(self):
        super().__init__("ndb_navaids")
        self.cont_rec_no = None
        self.frequency = None
        self.nav_class = None
        self.lat = None
        self.lon = None
        self.mag_var = None
        self.datum_code = None
        self.ndb_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.ndb_id}, {self.ndb_name}, {self.frequency}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.frequency = extract_field(line, w_pri.frequency, "NDB")
        self.nav_class = extract_field(line, w_pri.nav_class)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.datum_code = extract_field(line, w_pri.datum_code)
        self.ndb_name = extract_field(line, w_pri.ndb_name)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "frequency",
                "nav_class",
                "lat",
                "lon",
                "mag_var",
                "datum_code",
                "ndb_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        base_dict = super().to_dict()
        this_dict = {
            "cont_rec_no": clean_value(self.cont_rec_no),
            "frequency": clean_value(self.frequency),
            "nav_class": clean_value(self.nav_class),
            "lat": clean_value(self.lat),
            "lon": clean_value(self.lon),
            "mag_var": clean_value(self.mag_var),
            "datum_code": clean_value(self.datum_code),
            "ndb_name": clean_value(self.ndb_name),
        }
        return {**base_dict, **this_dict}
