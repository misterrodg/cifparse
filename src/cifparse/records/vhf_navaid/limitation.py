from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_lim


class Limitation(Base):
    cont_rec_no: int
    application: str
    nlc: str
    cai: str
    seq_no: int
    sector_1: str
    dist_desc_1: str
    dist_limit_1: str
    alt_desc_1: str
    alt_limit_1: str
    sector_2: str
    dist_desc_2: str
    dist_limit_2: str
    alt_desc_2: str
    alt_limit_2: str
    sector_3: str
    dist_desc_3: str
    dist_limit_3: str
    alt_desc_3: str
    alt_limit_3: str
    sector_4: str
    dist_desc_4: str
    dist_limit_4: str
    alt_desc_4: str
    alt_limit_4: str
    sector_5: str
    dist_desc_5: str
    dist_limit_5: str
    alt_desc_5: str
    alt_limit_5: str
    seq_ind: str

    def __init__(self):
        super().__init__("vhf_limitations")
        self.cont_rec_no = None
        self.application = None
        self.nlc = None
        self.cai = None
        self.seq_no = None
        self.sector_1 = None
        self.dist_desc_1 = None
        self.dist_limit_1 = None
        self.alt_desc_1 = None
        self.alt_limit_1 = None
        self.sector_2 = None
        self.dist_desc_2 = None
        self.dist_limit_2 = None
        self.alt_desc_2 = None
        self.alt_limit_2 = None
        self.sector_3 = None
        self.dist_desc_3 = None
        self.dist_limit_3 = None
        self.alt_desc_3 = None
        self.alt_limit_3 = None
        self.sector_4 = None
        self.dist_desc_4 = None
        self.dist_limit_4 = None
        self.alt_desc_4 = None
        self.alt_limit_4 = None
        self.sector_5 = None
        self.dist_desc_5 = None
        self.dist_limit_5 = None
        self.alt_desc_5 = None
        self.alt_limit_5 = None
        self.seq_ind = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.vhf_id}, {self.nlc}, {self.cai}"

    def from_line(self, line: str) -> "Limitation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_lim.cont_rec_no)
        self.application = extract_field(line, w_lim.application)
        self.nlc = extract_field(line, w_lim.nlc)
        self.cai = extract_field(line, w_lim.cai)
        self.seq_no = extract_field(line, w_lim.seq_no)
        self.sector_1 = extract_field(line, w_lim.sector_1)
        self.dist_desc_1 = extract_field(line, w_lim.dist_desc_1)
        self.dist_limit_1 = extract_field(line, w_lim.dist_limit_1)
        self.alt_desc_1 = extract_field(line, w_lim.alt_desc_1)
        self.alt_limit_1 = extract_field(line, w_lim.alt_limit_1)
        self.sector_2 = extract_field(line, w_lim.sector_2)
        self.dist_desc_2 = extract_field(line, w_lim.dist_desc_2)
        self.dist_limit_2 = extract_field(line, w_lim.dist_limit_2)
        self.alt_desc_2 = extract_field(line, w_lim.alt_desc_2)
        self.alt_limit_2 = extract_field(line, w_lim.alt_limit_2)
        self.sector_3 = extract_field(line, w_lim.sector_3)
        self.dist_desc_3 = extract_field(line, w_lim.dist_desc_3)
        self.dist_limit_3 = extract_field(line, w_lim.dist_limit_3)
        self.alt_desc_3 = extract_field(line, w_lim.alt_desc_3)
        self.alt_limit_3 = extract_field(line, w_lim.alt_limit_3)
        self.sector_4 = extract_field(line, w_lim.sector_4)
        self.dist_desc_4 = extract_field(line, w_lim.dist_desc_4)
        self.dist_limit_4 = extract_field(line, w_lim.dist_limit_4)
        self.alt_desc_4 = extract_field(line, w_lim.alt_desc_4)
        self.alt_limit_4 = extract_field(line, w_lim.alt_limit_4)
        self.sector_5 = extract_field(line, w_lim.sector_5)
        self.dist_desc_5 = extract_field(line, w_lim.dist_desc_5)
        self.dist_limit_5 = extract_field(line, w_lim.dist_limit_5)
        self.alt_desc_5 = extract_field(line, w_lim.alt_desc_5)
        self.alt_limit_5 = extract_field(line, w_lim.alt_limit_5)
        self.seq_ind = extract_field(line, w_lim.seq_ind)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "nlc",
                "cai",
                "seq_no",
                "sector_1",
                "dist_desc_1",
                "dist_limit_1",
                "alt_desc_1",
                "alt_limit_1",
                "sector_2",
                "dist_desc_2",
                "dist_limit_2",
                "alt_desc_2",
                "alt_limit_2",
                "sector_3",
                "dist_desc_3",
                "dist_limit_3",
                "alt_desc_3",
                "alt_limit_3",
                "sector_4",
                "dist_desc_4",
                "dist_limit_4",
                "alt_desc_4",
                "alt_limit_4",
                "sector_5",
                "dist_desc_5",
                "dist_limit_5",
                "alt_desc_5",
                "alt_limit_5",
                "seq_ind",
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
            "nlc": self.nlc,
            "cai": self.cai,
            "seq_no": self.seq_no,
            "sector_1": self.sector_1,
            "dist_desc_1": self.dist_desc_1,
            "dist_limit_1": self.dist_limit_1,
            "alt_desc_1": self.alt_desc_1,
            "alt_limit_1": self.alt_limit_1,
            "sector_2": self.sector_2,
            "dist_desc_2": self.dist_desc_2,
            "dist_limit_2": self.dist_limit_2,
            "alt_desc_2": self.alt_desc_2,
            "alt_limit_2": self.alt_limit_2,
            "sector_3": self.sector_3,
            "dist_desc_3": self.dist_desc_3,
            "dist_limit_3": self.dist_limit_3,
            "alt_desc_3": self.alt_desc_3,
            "alt_limit_3": self.alt_limit_3,
            "sector_4": self.sector_4,
            "dist_desc_4": self.dist_desc_4,
            "dist_limit_4": self.dist_limit_4,
            "alt_desc_4": self.alt_desc_4,
            "alt_limit_4": self.alt_limit_4,
            "sector_5": self.sector_5,
            "dist_desc_5": self.dist_desc_5,
            "dist_limit_5": self.dist_limit_5,
            "alt_desc_5": self.alt_desc_5,
            "alt_limit_5": self.alt_limit_5,
            "seq_ind": self.seq_ind,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
