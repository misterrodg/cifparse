from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    length: int
    bearing: float
    true: bool
    lat: float
    lon: float
    gradient: float
    ellipsoidal_height: int
    threshold_elevation: int
    displaced_threshold: int
    tch: int
    width: int
    tch_id: str
    ls_ident_1: str
    cat_1: str
    stopway: str
    ls_ident_2: str
    cat_2: str
    description: str

    def __init__(self):
        super().__init__("runways")
        self.cont_rec_no = None
        self.length = None
        self.bearing = None
        self.true = None
        self.lat = None
        self.lon = None
        self.gradient = None
        self.ellipsoidal_height = None
        self.threshold_elevation = None
        self.displaced_threshold = None
        self.tch = None
        self.width = None
        self.tch_id = None
        self.ls_ident_1 = None
        self.cat_1 = None
        self.stopway = None
        self.ls_ident_2 = None
        self.cat_2 = None
        self.description = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.runway_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.length = extract_field(line, w_pri.length)
        self.true, self.bearing = extract_field(line, w_pri.bearing)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.gradient = extract_field(line, w_pri.gradient)
        self.ellipsoidal_height = extract_field(line, w_pri.ellipsoidal_height)
        self.threshold_elevation = extract_field(line, w_pri.threshold_elevation)
        self.displaced_threshold = extract_field(line, w_pri.displaced_threshold)
        self.tch = extract_field(line, w_pri.tch)
        self.width = extract_field(line, w_pri.width)
        self.tch_id = extract_field(line, w_pri.tch_id)
        self.ls_ident_1 = extract_field(line, w_pri.ls_ident_1)
        self.cat_1 = extract_field(line, w_pri.cat_1)
        self.stopway = extract_field(line, w_pri.stopway)
        self.ls_ident_2 = extract_field(line, w_pri.ls_ident_2)
        self.cat_2 = extract_field(line, w_pri.cat_2)
        self.description = extract_field(line, w_pri.description)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "length",
                "bearing",
                "true",
                "lat",
                "lon",
                "gradient",
                "ellipsoidal_height",
                "threshold_elevation",
                "displaced_threshold",
                "tch",
                "width",
                "tch_id",
                "ls_ident_1",
                "cat_1",
                "stopway",
                "ls_ident_2",
                "cat_2",
                "description",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "length": self.length,
            "bearing": self.bearing,
            "true": self.true,
            "lat": self.lat,
            "lon": self.lon,
            "gradient": self.gradient,
            "ellipsoidal_height": self.ellipsoidal_height,
            "threshold_elevation": self.threshold_elevation,
            "displaced_threshold": self.displaced_threshold,
            "tch": self.tch,
            "width": self.width,
            "tch_id": self.tch_id,
            "ls_ident_1": self.ls_ident_1,
            "cat_1": self.cat_1,
            "stopway": self.stopway,
            "ls_ident_2": self.ls_ident_2,
            "cat_2": self.cat_2,
            "description": self.description,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
