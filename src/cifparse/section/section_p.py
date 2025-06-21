from cifparse.functions.field import extract_field
from cifparse.records.airport.widths import w_pri as a_w_pri
from cifparse.records.airport_gate.widths import w_pri as b_w_pri
from cifparse.records.waypoint.widths import w_pri as c_w_pri
from cifparse.records.procedure.widths import w_pri as def_w_pri
from cifparse.records.runway.widths import w_pri as g_w_pri
from cifparse.records.loc_gs.widths import w_pri as i_w_pri
from cifparse.records.taa.widths import w_pri as k_w_pri
from cifparse.records.mls.widths import w_pri as l_w_pri
from cifparse.records.terminal_marker.widths import w_pri as m_w_pri
from cifparse.records.path_point.widths import w_pri as p_w_pri
from cifparse.records.flight_planning.widths import w_pri as r_w_pri
from cifparse.records.msa.widths import w_pri as s_w_pri
from cifparse.records.gls.widths import w_pri as t_w_pri
from cifparse.records.terminal_comm.widths import w_pri as v_w_pri


class SectionP:
    subsection_a: list[str]  # Airport
    subsection_b: list[str]  # Airport Gate
    subsection_c: list[str]  # Terminal Waypoints
    subsection_d: list[str]  # SID
    subsection_e: list[str]  # STAR
    subsection_f: list[str]  # IAP
    subsection_g: list[str]  # Runway
    subsection_i: list[str]  # LOC/GS
    subsection_k: list[str]  # TAA
    subsection_l: list[str]  # MLS
    subsection_m: list[str]  # Markers
    subsection_p: list[str]  # Path Point
    subsection_r: list[str]  # Flight Planning
    subsection_s: list[str]  # MSA
    subsection_t: list[str]  # GLS
    subsection_v: list[str]  # Communication

    def __init__(self, lines: list[str]):
        self.subsection_a = []
        self.subsection_b = []
        self.subsection_c = []
        self.subsection_d = []
        self.subsection_e = []
        self.subsection_f = []
        self.subsection_g = []
        self.subsection_i = []
        self.subsection_k = []
        self.subsection_l = []
        self.subsection_m = []
        self.subsection_p = []
        self.subsection_r = []
        self.subsection_s = []
        self.subsection_t = []
        self.subsection_v = []

        for line in lines:
            if extract_field(line, a_w_pri.sub_code) == "A":
                self.subsection_a.append(line)
                continue
            if extract_field(line, b_w_pri.sub_code) == "B":
                self.subsection_b.append(line)
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
            if extract_field(line, g_w_pri.sub_code) == "G":
                self.subsection_g.append(line)
                continue
            if extract_field(line, i_w_pri.sub_code) == "I":
                self.subsection_i.append(line)
                continue
            if extract_field(line, k_w_pri.sub_code) == "K":
                self.subsection_k.append(line)
                continue
            if extract_field(line, l_w_pri.sub_code) == "L":
                self.subsection_l.append(line)
                continue
            if extract_field(line, m_w_pri.sub_code) == "M":
                self.subsection_m.append(line)
                continue
            if extract_field(line, p_w_pri.sub_code) == "P":
                self.subsection_p.append(line)
                continue
            if extract_field(line, r_w_pri.sub_code) == "R":
                self.subsection_r.append(line)
                continue
            if extract_field(line, s_w_pri.sub_code) == "S":
                self.subsection_s.append(line)
                continue
            if extract_field(line, t_w_pri.sub_code) == "T":
                self.subsection_t.append(line)
                continue
            if extract_field(line, v_w_pri.sub_code) == "V":
                self.subsection_v.append(line)
                continue

    def get_airports(self) -> list[str]:
        return self.subsection_a

    def get_airport_gates(self) -> list[str]:
        return self.subsection_b

    def get_terminal_waypoints(self) -> list[str]:
        return self.subsection_c

    def get_sids(self) -> list[str]:
        return self.subsection_d

    def get_stars(self) -> list[str]:
        return self.subsection_e

    def get_iaps(self) -> list[str]:
        return self.subsection_f

    def get_runways(self) -> list[str]:
        return self.subsection_g

    def get_loc_gss(self) -> list[str]:
        return self.subsection_i

    def get_taas(self) -> list[str]:
        return self.subsection_k

    def get_mlss(self) -> list[str]:
        return self.subsection_l

    def get_markers(self) -> list[str]:
        return self.subsection_m

    def get_path_points(self) -> list[str]:
        return self.subsection_p

    def get_flight_plannings(self) -> list[str]:
        return self.subsection_r

    def get_msas(self) -> list[str]:
        return self.subsection_s

    def get_glss(self) -> list[str]:
        return self.subsection_t

    def get_communications(self) -> list[str]:
        return self.subsection_v
