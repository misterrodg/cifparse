from cifparse.functions.records import split_lines_by_char

from .section.section_a import SectionA
from .section.section_d import SectionD
from .section.section_e import SectionE
from .section.section_h import SectionH
from .section.section_p import SectionP
from .section.section_r import SectionR
from .section.section_t import SectionT
from .section.section_u import SectionU


class Sections:
    header_lines: list[str]
    section_a_lines: list[str]
    section_d_lines: list[str]
    section_e_lines: list[str]
    section_h_lines: list[str]
    section_p_lines: list[str]
    section_r_lines: list[str]
    section_t_lines: list[str]
    section_u_lines: list[str]
    header: str
    section_a: SectionA
    section_d: SectionD
    section_e: SectionE
    section_h: SectionH
    section_p: SectionP
    section_r: SectionR
    section_t: SectionT
    section_u: SectionU

    def __init__(self, lines: list[str]):
        self.header_lines = []
        self.section_a_lines = []
        self.section_d_lines = []
        self.section_e_lines = []
        self.section_h_lines = []
        self.section_p_lines = []
        self.section_r_lines = []
        self.section_t_lines = []
        self.section_u_lines = []
        self.header = ""
        self.section_a = None
        self.section_d = None
        self.section_e = None
        self.section_h = None
        self.section_p = None
        self.section_r = None
        self.section_t = None
        self.section_u = None

        line_count = 0
        record_lines = []
        for line in lines:
            line_count += 1
            if line[0:3] == "HDR":
                if line[0:5] == "HDR04":
                    self.header = line
                self.header_lines.append(line)
            else:
                record_lines.append(line)

        section_data = split_lines_by_char(record_lines, (4, 5))

        self.section_a_lines = section_data.get("A", [])
        self.section_a = SectionA(self.section_a_lines)

        self.section_d_lines = section_data.get("D", [])
        self.section_d = SectionD(self.section_d_lines)

        self.section_e_lines = section_data.get("E", [])
        self.section_e = SectionE(self.section_e_lines)

        self.section_h_lines = section_data.get("H", [])
        self.section_h = SectionH(self.section_h_lines)

        self.section_p_lines = section_data.get("P", [])
        self.section_p = SectionP(self.section_p_lines)

        self.section_r_lines = section_data.get("R", [])
        self.section_r = SectionR(self.section_r_lines)

        self.section_t_lines = section_data.get("T", [])
        self.section_t = SectionT(self.section_t_lines)

        self.section_u_lines = section_data.get("U", [])
        self.section_u = SectionU(self.section_u_lines)

        header_count = len(self.header_lines)
        header_line = f" ({header_count} header lines) " if header_count > 0 else " "
        print(
            f"\n    Found {len(record_lines)} records{header_line}in {line_count} lines.\n"
        )

    def get_header_lines(self) -> list[str]:
        return self.header_lines

    def get_header(self) -> str:
        return self.header

    def get_section_a_lines(self) -> list[str]:
        return self.section_a_lines

    def get_section_a(self) -> SectionA:
        return self.section_a

    def get_section_d_lines(self) -> list[str]:
        return self.section_d_lines

    def get_section_d(self) -> SectionD:
        return self.section_d

    def get_section_e_lines(self) -> list[str]:
        return self.section_e_lines

    def get_section_e(self) -> SectionE:
        return self.section_e

    def get_section_h_lines(self) -> list[str]:
        return self.section_h_lines

    def get_section_h(self) -> SectionH:
        return self.section_h

    def get_section_p_lines(self) -> list[str]:
        return self.section_p_lines

    def get_section_p(self) -> SectionP:
        return self.section_p

    def get_section_r_lines(self) -> list[str]:
        return self.section_r_lines

    def get_section_r(self) -> SectionP:
        return self.section_r

    def get_section_t_lines(self) -> list[str]:
        return self.section_t_lines

    def get_section_t(self) -> SectionT:
        return self.section_t

    def get_section_u_lines(self) -> list[str]:
        return self.section_u_lines

    def get_section_u(self) -> SectionU:
        return self.section_u
