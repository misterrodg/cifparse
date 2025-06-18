from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    cont_rec_no: int
    route_ind: str
    sbas_spi: str
    ref_path_data_sel: str
    ref_path_data_id: str
    app_pd: str
    ltp_lat: float
    ltp_lon: float
    ltp_ellipsoid_height: int
    gpa: float
    fpap_lat: float
    fpap_lon: float
    course_width: float
    length_offset: int
    path_point_tch: int
    tch_ind: str
    hal: str
    val: str
    crc: str

    def __init__(self):
        super().__init__("path_points")
        self.cont_rec_no = None
        self.route_ind = None
        self.sbas_spi = None
        self.ref_path_data_sel = None
        self.ref_path_data_id = None
        self.app_pd = None
        self.ltp_lat = None
        self.ltp_lon = None
        self.ltp_ellipsoid_height = None
        self.gpa = None
        self.fpap_lat = None
        self.fpap_lon = None
        self.course_width = None
        self.length_offset = None
        self.path_point_tch = None
        self.tch_ind = None
        self.hal = None
        self.val = None
        self.crc = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}, {self.approach_id}"

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_pri.cont_rec_no)
        self.route_ind = extract_field(line, w_pri.route_ind)
        self.sbas_spi = extract_field(line, w_pri.sbas_spi)
        self.ref_path_data_sel = extract_field(line, w_pri.ref_path_data_sel)
        self.ref_path_data_id = extract_field(line, w_pri.ref_path_data_id)
        self.app_pd = extract_field(line, w_pri.app_pd)
        self.ltp_lat = extract_field(line, w_pri.ltp_lat)
        self.ltp_lon = extract_field(line, w_pri.ltp_lon)
        self.ltp_ellipsoid_height = extract_field(line, w_pri.ltp_ellipsoid_height)
        self.gpa = extract_field(line, w_pri.gpa)
        self.fpap_lat = extract_field(line, w_pri.fpap_lat)
        self.fpap_lon = extract_field(line, w_pri.fpap_lon)
        self.course_width = extract_field(line, w_pri.course_width)
        self.length_offset = extract_field(line, w_pri.length_offset)
        tch_type = extract_field(line, w_pri.tch_ind)
        self.path_point_tch = extract_field(line, w_pri.path_point_tch, tch_type)
        self.tch_ind = tch_type
        self.hal = extract_field(line, w_pri.hal)
        self.val = extract_field(line, w_pri.val)
        self.crc = extract_field(line, w_pri.crc)

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "route_ind",
                "sbas_spi",
                "ref_path_data_sel",
                "ref_path_data_id",
                "app_pd",
                "ltp_lat",
                "ltp_lon",
                "ltp_ellipsoid_height",
                "gpa",
                "fpap_lat",
                "fpap_lon",
                "course_width",
                "length_offset",
                "path_point_tch",
                "tch_ind",
                "hal",
                "val",
                "crc",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "route_ind": self.route_ind,
            "sbas_spi": self.sbas_spi,
            "ref_path_data_sel": self.ref_path_data_sel,
            "ref_path_data_id": self.ref_path_data_id,
            "app_pd": self.app_pd,
            "ltp_lat": self.ltp_lat,
            "ltp_lon": self.ltp_lon,
            "ltp_ellipsoid_height": self.ltp_ellipsoid_height,
            "gpa": self.gpa,
            "fpap_lat": self.fpap_lat,
            "fpap_lon": self.fpap_lon,
            "course_width": self.course_width,
            "length_offset": self.length_offset,
            "path_point_tch": self.path_point_tch,
            "tch_ind": self.tch_ind,
            "hal": self.hal,
            "val": self.val,
            "crc": self.crc,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
