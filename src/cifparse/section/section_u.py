from cifparse.functions.field import extract_field
from cifparse.records.controlled.widths import w_pri as c_w_pri
from cifparse.records.fir_uir.widths import w_pri as f_w_pri
from cifparse.records.restrictive.widths import w_pri as r_w_pri


class SectionU:
    subsection_c: list[str]  # Controlled
    subsection_f: list[str]  # FIR/UIR
    subsection_r: list[str]  # Restrictive

    def __init__(self, lines: list[str]):
        self.subsection_c = []
        self.subsection_f = []
        self.subsection_r = []

        for line in lines:
            if extract_field(line, c_w_pri.sub_code) == "C":
                self.subsection_c.append(line)
                continue
            if extract_field(line, f_w_pri.sub_code) == "F":
                self.subsection_f.append(line)
                continue
            if extract_field(line, r_w_pri.sub_code) == "R":
                self.subsection_r.append(line)
                continue

    def get_controlled(self) -> list[str]:
        return self.subsection_c

    def get_fir_uir(self) -> list[str]:
        return self.subsection_f

    def get_restrictive(self) -> list[str]:
        return self.subsection_r
