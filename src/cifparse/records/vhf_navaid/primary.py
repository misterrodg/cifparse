from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    frequency: float
    nav_class: str
    lat: float
    lon: float
    dme_id: str
    dme_lat: float
    dme_lon: float
    mag_var: float
    dme_elevation: int
    figure_of_merit: str
    dme_bias: str
    frequency_protection: str
    datum_code: str
    vhf_name: str

    def __init__(self):
        super().__init__("vhf_navaids")
        self.cont_rec_no = None
        self.frequency = None
        self.nav_class = None
        self.lat = None
        self.lon = None
        self.dme_id = None
        self.dme_lat = None
        self.dme_lon = None
        self.mag_var = None
        self.dme_elevation = None
        self.figure_of_merit = None
        self.dme_bias = None
        self.frequency_protection = None
        self.datum_code = None
        self.vhf_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.vhf_id}, {self.vhf_name}, {self.frequency}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.frequency = extract_field(line, w_pri.frequency, "VOR")
        self.nav_class = extract_field(line, w_pri.nav_class)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.dme_id = extract_field(line, w_pri.dme_id)
        self.dme_lat = extract_field(line, w_pri.dme_lat)
        self.dme_lon = extract_field(line, w_pri.dme_lon)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.dme_elevation = extract_field(line, w_pri.dme_elevation)
        self.figure_of_merit = extract_field(line, w_pri.figure_of_merit)
        self.dme_bias = extract_field(line, w_pri.dme_bias)
        self.frequency_protection = extract_field(line, w_pri.frequency_protection)
        self.datum_code = extract_field(line, w_pri.datum_code)
        self.vhf_name = extract_field(line, w_pri.vhf_name)
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
                "dme_id",
                "dme_lat",
                "dme_lon",
                "mag_var",
                "dme_elevation",
                "figure_of_merit",
                "dme_bias",
                "frequency_protection",
                "datum_code",
                "vhf_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "frequency": self.frequency,
            "nav_class": self.nav_class,
            "lat": self.lat,
            "lon": self.lon,
            "dme_id": self.dme_id,
            "dme_lat": self.dme_lat,
            "dme_lon": self.dme_lon,
            "mag_var": self.mag_var,
            "dme_elevation": self.dme_elevation,
            "figure_of_merit": self.figure_of_merit,
            "dme_bias": self.dme_bias,
            "frequency_protection": self.frequency_protection,
            "datum_code": self.datum_code,
            "vhf_name": self.vhf_name,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
