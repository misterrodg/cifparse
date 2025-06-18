from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    gls_channel: str
    runway_id: str
    true: bool
    gls_bearing: float
    station_lat: float
    station_lon: float
    gls_id: str
    svc_vol: str
    tdma_slots: str
    min_elev_angle: float
    mag_var: float
    station_elev: int
    datum_code: str
    station_type: str
    wgs84_elev: int

    def __init__(self):
        super().__init__("glss")
        self.cont_rec_no = None
        self.gls_channel = None
        self.runway_id = None
        self.true = None
        self.gls_bearing = None
        self.station_lat = None
        self.station_lon = None
        self.gls_id = None
        self.svc_vol = None
        self.tdma_slots = None
        self.min_elev_angle = None
        self.mag_var = None
        self.station_elev = None
        self.datum_code = None
        self.station_type = None
        self.wgs84_elev = None

    def __repr__(self):
        return (
            f"{self.__class__.__name__}: {self.fac_id}, {self.gls_id}, {self.runway_id}"
        )

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.gls_channel = extract_field(line, w_pri.gls_bearing)
        self.runway_id = extract_field(line, w_pri.runway_id)
        self.true, self.gls_bearing = extract_field(line, w_pri.gls_bearing)
        self.station_lat = extract_field(line, w_pri.station_lat)
        self.station_lon = extract_field(line, w_pri.station_lon)
        self.gls_id = extract_field(line, w_pri.gls_id)
        self.svc_vol = extract_field(line, w_pri.svc_vol)
        self.tdma_slots = extract_field(line, w_pri.tdma_slots)
        self.min_elev_angle = extract_field(line, w_pri.min_elev_angle)
        self.mag_var = extract_field(line, w_pri.mag_var)
        self.station_elev = extract_field(line, w_pri.station_elev)
        self.datum_code = extract_field(line, w_pri.datum_code)
        self.station_type = extract_field(line, w_pri.station_type)
        self.wgs84_elev = extract_field(line, w_pri.wgs84_elev)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "gls_channel",
                "runway_id",
                "true",
                "gls_bearing",
                "station_lat",
                "station_lon",
                "gls_id",
                "svc_vol",
                "tdma_slots",
                "min_elev_angle",
                "mag_var",
                "station_elev",
                "datum_code",
                "station_type",
                "wgs84_elev",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "gls_channel": self.gls_channel,
            "runway_id": self.runway_id,
            "true": self.true,
            "gls_bearing": self.gls_bearing,
            "station_lat": self.station_lat,
            "station_lon": self.station_lon,
            "gls_id": self.gls_id,
            "svc_vol": self.svc_vol,
            "tdma_slots": self.tdma_slots,
            "min_elev_angle": self.min_elev_angle,
            "mag_var": self.mag_var,
            "station_elev": self.station_elev,
            "datum_code": self.datum_code,
            "station_type": self.station_type,
            "wgs84_elev": self.wgs84_elev,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
