from cifparse.functions.field import extract_field
from cifparse.records.waypoint.widths import w_pri as a_w_pri
from cifparse.records.airway_marker.widths import w_pri as m_w_pri
from cifparse.records.hold.widths import w_pri as p_w_pri
from cifparse.records.airway_point.widths import w_pri as r_w_pri
from cifparse.records.preferred_route.widths import w_pri as t_w_pri
from cifparse.records.airway_restrictions import w_aex as u_w_pri
from cifparse.records.enroute_comm.widths import w_pri as v_w_pri


class SectionE:
    subsection_a: list[str]  # Enroute Waypoints
    subsection_m: list[str]  # Airway Markers
    subsection_p: list[str]  # Holding Patterns
    subsection_r: list[str]  # Airways
    subsection_t: list[str]  # Preferred Routes
    subsection_u: list[str]  # Airway Restrictions
    subsection_v: list[str]  # Communication

    def __init__(self, lines: list[str]):
        self.subsection_a = []
        self.subsection_m = []
        self.subsection_p = []
        self.subsection_r = []
        self.subsection_t = []
        self.subsection_u = []
        self.subsection_v = []

        for line in lines:
            if extract_field(line, a_w_pri.sub_code) == "A":
                self.subsection_a.append(line)
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
            if extract_field(line, t_w_pri.sub_code) == "T":
                self.subsection_t.append(line)
                continue
            if extract_field(line, u_w_pri.sub_code) == "U":
                self.subsection_u.append(line)
                continue
            if extract_field(line, v_w_pri.sub_code) == "V":
                self.subsection_v.append(line)
                continue

    def get_enroute_waypoints(self) -> list[str]:
        return self.subsection_a

    def get_airway_markers(self) -> list[str]:
        return self.subsection_m

    def get_holding_patterns(self) -> list[str]:
        return self.subsection_p

    def get_airway_points(self) -> list[str]:
        return self.subsection_r

    def get_preferred_routes(self) -> list[str]:
        return self.subsection_t

    def get_airway_restrictions(self) -> list[str]:
        return self.subsection_u

    def get_communication(self) -> list[str]:
        return self.subsection_v
