from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    marker_code: str
    shape: str
    environment_id: str
    lat: float
    lon: float
    true_bearing: float
    true: bool
    mag_var: float
    fac_elev: int
    datum_code: str
    marker_name: str

    def __init__(self):
        super().__init__("markers")
        self.cont_rec_no = None
        self.marker_code = None
        self.shape = None
        self.environment_id = None
        self.lat = None
        self.lon = None
        self.true_bearing = None
        self.mag_var = None
        self.fac_elev = None
        self.datum_code = None
        self.marker_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.marker_id}, {self.marker_name}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.marker_code = extract_field(line, w_pri.marker_code)
        self.shape = extract_field(line, w_pri.shape)
        self.environment_id = extract_field(line, w_pri.environment_id)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.true_bearing = extract_field(line, w_pri.true_bearing)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.fac_elev = extract_field(line, w_pri.fac_elev)
        self.datum_code = extract_field(line, w_pri.datum_code)
        self.marker_name = extract_field(line, w_pri.marker_name)

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "marker_code",
                "shape",
                "environment_id",
                "lat",
                "lon",
                "true_bearing",
                "mag_var",
                "fac_elev",
                "datum_code",
                "marker_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "marker_code": self.marker_code,
            "shape": self.shape,
            "environment_id": self.environment_id,
            "lat": self.lat,
            "lon": self.lon,
            "true_bearing": self.true_bearing,
            "mag_var": self.mag_var,
            "fac_elev": self.fac_elev,
            "datum_code": self.datum_code,
            "marker_name": self.marker_name,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
