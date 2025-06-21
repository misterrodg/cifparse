from cifparse.functions.field import extract_field
from cifparse.records.heliport.widths import w_pri as a_w_pri
from cifparse.records.waypoint.widths import w_pri as c_w_pri
from cifparse.records.heli_procedure.widths import w_pri as def_w_pri
from cifparse.records.heli_taa.widths import w_pri as k_w_pri
from cifparse.records.heli_msa.widths import w_pri as s_w_pri
from cifparse.records.heli_terminal_comm.widths import w_pri as v_w_pri


class SectionH:
    subsection_a: list[str]  # Heliport
    subsection_c: list[str]  # Terminal Waypoints
    subsection_d: list[str]  # SID
    subsection_e: list[str]  # STAR
    subsection_f: list[str]  # IAP
    subsection_k: list[str]  # TAA
    subsection_s: list[str]  # MSA
    subsection_v: list[str]  # Communication

    def __init__(self, lines: list[str]):
        self.subsection_a = []
        self.subsection_c = []
        self.subsection_d = []
        self.subsection_e = []
        self.subsection_f = []
        self.subsection_k = []
        self.subsection_s = []
        self.subsection_v = []

        for line in lines:
            if extract_field(line, a_w_pri.sub_code) == "A":
                self.subsection_a.append(line)
                continue
            if extract_field(line, c_w_pri.environment_sub_code) == "C":
                self.subsection_c.append(line)
                continue
            if extract_field(line, def_w_pri.fac_sub_code) == "D":
                self.subsection_d.append(line)
                continue
            if extract_field(line, def_w_pri.fac_sub_code) == "E":
                self.subsection_e.append(line)
                continue
            if extract_field(line, def_w_pri.fac_sub_code) == "F":
                self.subsection_f.append(line)
                continue
            if extract_field(line, k_w_pri.sub_code) == "K":
                self.subsection_k.append(line)
                continue
            if extract_field(line, s_w_pri.sub_code) == "S":
                self.subsection_s.append(line)
                continue
            if extract_field(line, v_w_pri.sub_code) == "V":
                self.subsection_v.append(line)
                continue

    def get_heliports(self) -> list[str]:
        return self.subsection_a

    def get_terminal_waypoints(self) -> list[str]:
        return self.subsection_c

    def get_sids(self) -> list[str]:
        return self.subsection_d

    def get_stars(self) -> list[str]:
        return self.subsection_e

    def get_iaps(self) -> list[str]:
        return self.subsection_f

    def get_taas(self) -> list[str]:
        return self.subsection_k

    def get_msas(self) -> list[str]:
        return self.subsection_s

    def get_communications(self) -> list[str]:
        return self.subsection_v
