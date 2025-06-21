from cifparse.functions.field import extract_field
from cifparse.records.cruise_table.widths import w_pri as c_w_pri
from cifparse.records.reference_table.widths import w_pri as g_w_pri


class SectionT:
    subsection_c: list[str]  # Cruise Table
    subsection_g: list[str]  # Reference Table

    def __init__(self, lines: list[str]):
        self.subsection_c = []
        self.subsection_g = []

        for line in lines:
            if extract_field(line, c_w_pri.sub_code) == "C":
                self.subsection_c.append(line)
                continue
            if extract_field(line, g_w_pri.sub_code) == "G":
                self.subsection_g.append(line)
                continue

    def get_cruise_tables(self) -> list[str]:
        return self.subsection_c

    def get_reference_tables(self) -> list[str]:
        return self.subsection_g
