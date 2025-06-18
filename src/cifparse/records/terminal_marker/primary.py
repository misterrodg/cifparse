from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    frequency: float
    runway_id: str
    marker_lat: float
    marker_lon: float
    true_bearing: float
    locator_lat: float
    locator_lon: float
    locator_class: str
    locator_fac_char: str
    locator_id: str
    mag_var: float
    fac_elev: int

    def __init__(self):
        super().__init__("terminal_markers")
        self.cont_rec_no = None
        self.frequency = None
        self.runway_id = None
        self.marker_lat = None
        self.marker_lon = None
        self.true_bearing = None
        self.locator_lat = None
        self.locator_lon = None
        self.locator_class = None
        self.locator_fac_char = None
        self.locator_id = None
        self.mag_var = None
        self.fac_elev = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.loc_id}, {self.locator_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.frequency = extract_field(line, w_pri.frequency, self.marker_type)
        self.runway_id = extract_field(line, w_pri.runway_id)
        self.marker_lat = extract_field(line, w_pri.marker_lat)
        self.marker_lon = extract_field(line, w_pri.marker_lon)
        self.true_bearing = extract_field(line, w_pri.true_bearing)
        self.locator_lon = extract_field(line, w_pri.locator_lon)
        self.locator_lat = extract_field(line, w_pri.locator_lat)
        self.locator_class = extract_field(line, w_pri.locator_class)
        self.locator_fac_char = extract_field(line, w_pri.locator_fac_char)
        self.locator_id = extract_field(line, w_pri.locator_id)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.fac_elev = extract_field(line, w_pri.fac_elev)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "frequency",
                "runway_id",
                "marker_lat",
                "marker_lon",
                "true_bearing",
                "locator_lat",
                "locator_lon",
                "locator_class",
                "locator_fac_char",
                "locator_id",
                "mag_var",
                "fac_elev",
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
            "runway_id": self.runway_id,
            "marker_lat": self.marker_lat,
            "marker_lon": self.marker_lon,
            "true_bearing": self.true_bearing,
            "locator_lat": self.locator_lat,
            "locator_lon": self.locator_lon,
            "locator_class": self.locator_class,
            "locator_fac_char": self.locator_fac_char,
            "locator_id": self.locator_id,
            "mag_var": self.mag_var,
            "fac_elev": self.fac_elev,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
