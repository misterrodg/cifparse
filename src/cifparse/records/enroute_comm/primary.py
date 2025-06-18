from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    serv_ind: str
    radar: str
    modulation: str
    sig_em: str
    lat: float
    lon: float
    mag_var: float
    fac_elev: int
    h24_ind: str
    alt_desc: str
    alt_1: int
    fl_1: int
    alt_2: int
    fl_2: int
    remote_fac: str
    remote_region: str
    remote_sec_code: str
    remote_sub_code: str

    def __init__(self):
        super().__init__("enroute_comms")
        self.cont_rec_no = None
        self.serv_ind = None
        self.radar = None
        self.modulation = None
        self.sig_em = None
        self.lat = None
        self.lon = None
        self.mag_var = None
        self.fac_elev = None
        self.h24_ind = None
        self.alt_desc = None
        self.alt_1 = None
        self.fl_1 = None
        self.alt_2 = None
        self.fl_2 = None
        self.remote_fac = None
        self.remote_region = None
        self.remote_sec_code = None
        self.remote_sub_code = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.fir_rdo_id}, {self.comm_freq}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.serv_ind = extract_field(line, w_pri.serv_ind)
        self.radar = extract_field(line, w_pri.radar)
        self.modulation = extract_field(line, w_pri.modulation)
        self.sig_em = extract_field(line, w_pri.sig_em)
        self.lat = extract_field(line, w_pri.lat)
        self.lon = extract_field(line, w_pri.lon)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.fac_elev = extract_field(line, w_pri.fac_elev)
        self.h24_ind = extract_field(line, w_pri.h24_ind)
        self.alt_desc = extract_field(line, w_pri.alt_desc)
        self.fl_1, self.alt_1 = extract_field(line, w_pri.alt_1)
        self.fl_2, self.alt_2 = extract_field(line, w_pri.alt_2)
        self.remote_fac = extract_field(line, w_pri.remote_fac)
        self.remote_region = extract_field(line, w_pri.remote_region)
        self.remote_sec_code = extract_field(line, w_pri.remote_sec_code)
        self.remote_sub_code = extract_field(line, w_pri.remote_sub_code)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "serv_ind",
                "radar",
                "modulation",
                "sig_em",
                "lat",
                "lon",
                "mag_var",
                "fac_elev",
                "h24_ind",
                "alt_desc",
                "alt_1",
                "fl_1",
                "alt_2",
                "fl_2",
                "remote_fac",
                "remote_region",
                "remote_sec_code",
                "remote_sub_code",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "serv_ind": self.serv_ind,
            "radar": self.radar,
            "modulation": self.modulation,
            "sig_em": self.sig_em,
            "lat": self.lat,
            "lon": self.lon,
            "mag_var": self.mag_var,
            "fac_elev": self.fac_elev,
            "h24_ind": self.h24_ind,
            "alt_desc": self.alt_desc,
            "alt_1": self.alt_1,
            "fl_1": self.fl_1,
            "alt_2": self.alt_2,
            "fl_2": self.fl_2,
            "remote_fac": self.remote_fac,
            "remote_region": self.remote_region,
            "remote_sec_code": self.remote_sec_code,
            "remote_sub_code": self.remote_sub_code,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
