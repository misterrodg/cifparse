from cifparse.functions.field import extract_field
from cifparse.records.mora.widths import w_pri as __w_pri
from cifparse.records.alternate_record.widths import w_pri as a_w_pri


class SectionR:
    subsection__: list[str]  # Company Routes
    subsection_a: list[str]  # Alternate Record

    def __init__(self, lines: list[str]):
        self.subsection__ = []
        self.subsection_a = []

        for line in lines:
            if extract_field(line, __w_pri.sub_code) == " ":
                self.subsection__.append(line)
                continue
            if extract_field(line, a_w_pri.sub_code) == "A":
                self.subsection_a.append(line)
                continue

    def get_company_routes(self) -> list[str]:
        return self.subsection__

    def get_alternate_records(self) -> list[str]:
        return self.subsection_a
