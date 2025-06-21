from cifparse.functions.field import extract_field
from cifparse.records.mora.widths import w_pri


class SectionA:
    subsection_s: list[str]  # Grid MORA

    def __init__(self, lines: list[str]):
        self.subsection_s = []

        for line in lines:
            if extract_field(line, w_pri.sub_code) == "S":
                self.subsection_s.append(line)
                continue

    def get_moras(self) -> list[str]:
        return self.subsection_s
