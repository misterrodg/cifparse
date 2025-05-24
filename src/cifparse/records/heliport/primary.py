from cifparse.functions.field import clean_value, extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    fl: int
    limit_alt: str
    datum_code: str
    is_ifr: int
    lat: float
    lon: float
    mag_var: float
    elevation: int
    speed_limit: int
    rec_vhf: str
    rec_vhf_region: str
    transition_alt: int
    transition_level: int
    usage: str
    time_zone: str
    daylight_ind: str
    pad_dimensions: str
    mag_true: str
    heliport_name: str

    def __init__(self):
        super().__init__("heliports")
        self.cont_rec_no = None
        self.fl = None
        self.limit_alt = None
        self.datum_code = None
        self.is_ifr = None
        self.lat = None
        self.lon = None
        self.mag_var = None
        self.elevation = None
        self.speed_limit = None
        self.rec_vhf = None
        self.rec_vhf_region = None
        self.transition_alt = None
        self.transition_level = None
        self.usage = None
        self.time_zone = None
        self.daylight_ind = None
        self.pad_dimensions = None
        self.mag_true = None
        self.heliport_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.heliport_id}, {self.pad_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.fl, self.limit_alt = extract_field(line, w_pri.limit_alt)
        self.datum_code = extract_field(line, w_pri.datum_code)
        self.is_ifr = extract_field(line, w_pri.is_ifr)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.elevation = extract_field(line, w_pri.elevation)
        self.speed_limit = extract_field(line, w_pri.speed_limit)
        self.rec_vhf = extract_field(line, w_pri.rec_vhf)
        self.rec_vhf_region = extract_field(line, w_pri.rec_vhf_region)
        self.transition_alt = extract_field(line, w_pri.transition_alt)
        self.transition_level = extract_field(line, w_pri.transition_level)
        self.usage = extract_field(line, w_pri.usage)
        self.time_zone = extract_field(line, w_pri.time_zone)
        self.daylight_ind = extract_field(line, w_pri.daylight_ind)
        self.pad_dimensions = extract_field(line, w_pri.pad_dimensions)
        self.mag_true = extract_field(line, w_pri.mag_true)
        self.heliport_name = extract_field(line, w_pri.heliport_name)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "fl",
                "limit_alt",
                "datum_code",
                "is_ifr",
                "lat",
                "lon",
                "mag_var",
                "elevation",
                "speed_limit",
                "rec_vhf",
                "rec_vhf_region",
                "transition_alt",
                "transition_level",
                "usage",
                "time_zone",
                "daylight_ind",
                "pad_dimensions",
                "mag_true",
                "heliport_name",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": clean_value(self.cont_rec_no),
            "fl": clean_value(self.fl),
            "limit_alt": clean_value(self.limit_alt),
            "datum_code": clean_value(self.datum_code),
            "is_ifr": clean_value(self.is_ifr),
            "lat": clean_value(self.lat),
            "lon": clean_value(self.lon),
            "mag_var": clean_value(self.mag_var),
            "elevation": clean_value(self.elevation),
            "speed_limit": clean_value(self.speed_limit),
            "rec_vhf": clean_value(self.rec_vhf),
            "rec_vhf_region": clean_value(self.rec_vhf_region),
            "transition_alt": clean_value(self.transition_alt),
            "transition_level": clean_value(self.transition_level),
            "usage": clean_value(self.usage),
            "time_zone": clean_value(self.time_zone),
            "daylight_ind": clean_value(self.daylight_ind),
            "pad_dimensions": clean_value(self.pad_dimensions),
            "mag_true": clean_value(self.mag_true),
            "heliport_name": clean_value(self.heliport_name),
        }
        return {**leading_dict, **this_dict, **trailing_dict}
