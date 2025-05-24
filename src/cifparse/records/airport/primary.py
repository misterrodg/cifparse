from cifparse.functions.field import clean_value, extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    fl: int
    limit_alt: str
    longest: int
    is_ifr: int
    longest_surface: str
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
    mag_true: str
    datum_code: str
    airport_name: str

    def __init__(self):
        super().__init__("airports")
        self.cont_rec_no = None
        self.fl = None
        self.limit_alt = None
        self.longest = None
        self.is_ifr = None
        self.longest_surface = None
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
        self.mag_true = None
        self.datum_code = None
        self.airport_name = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.airport_name}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.fl, self.limit_alt = extract_field(line, w_pri.limit_alt)
        self.longest = extract_field(line, w_pri.longest)
        self.is_ifr = extract_field(line, w_pri.is_ifr)
        self.longest_surface = extract_field(line, w_pri.longest_surface)
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
        self.mag_true = extract_field(line, w_pri.mag_true)
        self.datum_code = extract_field(line, w_pri.datum_code)
        self.airport_name = extract_field(line, w_pri.airport_name)
        return self

    def ordered_fields(self) -> dict:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "fl",
                "limit_alt",
                "longest",
                "is_ifr",
                "longest_surface",
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
                "mag_true",
                "datum_code",
                "airport_name",
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
            "longest": clean_value(self.longest),
            "is_ifr": clean_value(self.is_ifr),
            "longest_surface": clean_value(self.longest_surface),
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
            "mag_true": clean_value(self.mag_true),
            "datum_code": clean_value(self.datum_code),
            "airport_name": clean_value(self.airport_name),
        }
        return {**leading_dict, **this_dict, **trailing_dict}
