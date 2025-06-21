from cifparse.functions.field import extract_field
from cifparse.records.ndb_navaid.widths import w_pri as n_w_pri
from cifparse.records.vhf_navaid.widths import w_pri as v_w_pri


class SectionD:
    subsection__: list[str]  # VHF Navaid
    subsection_d: list[str]  # NDB Navaid

    def __init__(self, lines: list[str]):
        self.subsection__ = []
        self.subsection_d = []

        for line in lines:
            if extract_field(line, v_w_pri.sub_code) is None:
                self.subsection__.append(line)
                continue
            if extract_field(line, n_w_pri.sub_code) == "B":
                self.subsection_d.append(line)
                continue

    def get_vhf(self) -> list[str]:
        return self.subsection__

    def get_ndb(self) -> list[str]:
        return self.subsection_d
