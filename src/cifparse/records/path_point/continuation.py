from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_con


class Continuation(Base):
    cont_rec_no: int
    application: str
    fpap_ell_hgt: str
    fpap_ort_hgt: str
    ltp_ort_hgt: str
    app_type_id: str
    gnss_ch_no: str
    hpc: str

    def __init__(self):
        super().__init__("path_point_continuations")
        self.cont_rec_no = None
        self.application = None
        self.fpap_ell_hgt = None
        self.fpap_ort_hgt = None
        self.ltp_ort_hgt = None
        self.app_type_id = None
        self.gnss_ch_no = None
        self.hpc = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.airport_id}"

    def from_line(self, line: str) -> "Continuation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_con.cont_rec_no)
        self.application = extract_field(line, w_con.application)
        self.fpap_ell_hgt = extract_field(line, w_con.fpap_ell_hgt)
        self.fpap_ort_hgt = extract_field(line, w_con.fpap_ort_hgt)
        self.ltp_ort_hgt = extract_field(line, w_con.ltp_ort_hgt)
        self.app_type_id = extract_field(line, w_con.app_type_id)
        self.gnss_ch_no = extract_field(line, w_con.gnss_ch_no)
        self.hpc = extract_field(line, w_con.hpc)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "fpap_ell_hgt",
                "fpap_ort_hgt",
                "ltp_ort_hgt",
                "app_type_id",
                "gnss_ch_no",
                "hpc",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "application": self.application,
            "fpap_ell_hgt": self.fpap_ell_hgt,
            "fpap_ort_hgt": self.fpap_ort_hgt,
            "ltp_ort_hgt": self.ltp_ort_hgt,
            "app_type_id": self.app_type_id,
            "gnss_ch_no": self.gnss_ch_no,
            "hpc": self.hpc,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
