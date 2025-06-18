from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_sim


class Simulation(Base):
    cont_rec_no: str
    application: str
    fas_block: str
    fas_service: str
    l_vnav_block: str
    l_vnav_service: str
    lnav_block: str
    lnav_service: str
    app_rte_type_1: str
    app_rte_type_2: str

    def __init__(self):
        super().__init__("procedure_point_simulations")
        self.cont_rec_no = None
        self.application = None
        self.fas_block = None
        self.fas_service = None
        self.l_vnav_block = None
        self.l_vnav_service = None
        self.lnav_block = None
        self.lnav_service = None
        self.app_rte_type_1 = None
        self.app_rte_type_2 = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.procedure_id}"

    def from_line(self, line: str) -> "Simulation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_sim.cont_rec_no)
        self.application = extract_field(line, w_sim.application)
        self.fas_block = extract_field(line, w_sim.fas_block)
        self.fas_service = extract_field(line, w_sim.fas_service)
        self.l_vnav_block = extract_field(line, w_sim.l_vnav_block)
        self.l_vnav_service = extract_field(line, w_sim.l_vnav_service)
        self.lnav_block = extract_field(line, w_sim.lnav_block)
        self.lnav_service = extract_field(line, w_sim.lnav_service)
        self.app_rte_type_1 = extract_field(line, w_sim.app_rte_type_1)
        self.app_rte_type_2 = extract_field(line, w_sim.app_rte_type_2)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "fas_block",
                "fas_service",
                "l_vnav_block",
                "l_vnav_service",
                "lnav_block",
                "lnav_service",
                "app_rte_type_1",
                "app_rte_type_2",
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
            "fas_block": self.fas_block,
            "fas_service": self.fas_service,
            "l_vnav_block": self.l_vnav_block,
            "l_vnav_service": self.l_vnav_service,
            "lnav_block": self.lnav_block,
            "lnav_service": self.lnav_service,
            "app_rte_type_1": self.app_rte_type_1,
            "app_rte_type_2": self.app_rte_type_2,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
