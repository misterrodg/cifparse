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

        print(f"\n    Found {len(record_lines)} records (in {line_count} lines).\n")

        as_count = len(self.section_a.subsection_s)
        a_total = as_count
        print(f"        A:{a_total}/{len(self.section_a_lines)} (S:{as_count})")
        d__count = len(self.section_d.subsection__)
        db_count = len(self.section_d.subsection_d)
        d_total = d__count + db_count
        print(
            f"        D:{d_total}/{len(self.section_d_lines)} (_:{d__count}/B:{db_count})"
        )
        ea_count = len(self.section_e.subsection_a)
        em_count = len(self.section_e.subsection_m)
        ep_count = len(self.section_e.subsection_p)
        er_count = len(self.section_e.subsection_r)
        et_count = len(self.section_e.subsection_t)
        eu_count = len(self.section_e.subsection_u)
        ev_count = len(self.section_e.subsection_v)
        e_total = (
            ea_count + em_count + ep_count + er_count + et_count + eu_count + ev_count
        )
        print(
            f"        E:{e_total}/{len(self.section_e_lines)} (A:{ea_count}/M:{em_count}/P:{ep_count}/R:{er_count}/T:{et_count}/U:{eu_count}/V:{ev_count})"
        )
        ha_count = len(self.section_h.subsection_a)
        hc_count = len(self.section_h.subsection_c)
        hd_count = len(self.section_h.subsection_d)
        he_count = len(self.section_h.subsection_e)
        hf_count = len(self.section_h.subsection_f)
        hk_count = len(self.section_h.subsection_k)
        hs_count = len(self.section_h.subsection_s)
        hv_count = len(self.section_h.subsection_v)
        h_total = (
            ha_count
            + hc_count
            + hd_count
            + he_count
            + hf_count
            + hk_count
            + hs_count
            + hv_count
        )
        print(
            f"        H:{h_total}/{len(self.section_h_lines)} (A:{ha_count}/C:{hc_count}/D:{hd_count}/E:{he_count}/F:{hf_count}/K:{hk_count}/S:{hs_count}/V:{hv_count})"
        )
        pa_count = len(self.section_p.subsection_a)
        pb_count = len(self.section_p.subsection_b)
        pc_count = len(self.section_p.subsection_c)
        pd_count = len(self.section_p.subsection_d)
        pe_count = len(self.section_p.subsection_e)
        pf_count = len(self.section_p.subsection_f)
        pg_count = len(self.section_p.subsection_g)
        pi_count = len(self.section_p.subsection_i)
        pk_count = len(self.section_p.subsection_k)
        pl_count = len(self.section_p.subsection_l)
        pm_count = len(self.section_p.subsection_m)
        pp_count = len(self.section_p.subsection_p)
        pr_count = len(self.section_p.subsection_r)
        ps_count = len(self.section_p.subsection_s)
        pt_count = len(self.section_p.subsection_t)
        pv_count = len(self.section_p.subsection_v)
        p_total = (
            pa_count
            + pb_count
            + pc_count
            + pd_count
            + pe_count
            + pf_count
            + pg_count
            + pi_count
            + pk_count
            + pl_count
            + pm_count
            + pp_count
            + pr_count
            + ps_count
            + pt_count
            + pv_count
        )
        print(
            f"        P:{p_total}/{len(self.section_p_lines)} (A:{pa_count}/B:{pb_count}/C:{pc_count}/D:{pd_count}/E:{pe_count}/F:{pf_count}/G:{pg_count}/I:{pi_count}/K:{pk_count}/L:{pl_count}/M:{pm_count}/P:{pp_count}/R:{pr_count}/S:{ps_count}/T:{pt_count}/V:{pv_count})"
        )
        r__count = len(self.section_r.subsection__)
        ra_count = len(self.section_r.subsection_a)
        r_total = r__count + ra_count
        print(
            f"        R:{r_total}/{len(self.section_r_lines)} (_:{r__count}/A:{ra_count})"
        )
        tc_count = len(self.section_t.subsection_c)
        tg_count = len(self.section_t.subsection_g)
        t_total = tc_count + tg_count
        print(
            f"        T:{t_total}/{len(self.section_t_lines)} (C:{tc_count}/G:{tg_count})"
        )
        uc_count = len(self.section_u.subsection_c)
        uf_count = len(self.section_u.subsection_f)
        ur_count = len(self.section_u.subsection_r)
        u_total = uc_count + uf_count + ur_count
        print(
            f"        U:{u_total}/{len(self.section_u_lines)} (C:{uc_count}/F:{uf_count}/R:{ur_count})"
        )
        print("        ----------")
        print(
            f"        {a_total + d_total + e_total + h_total + p_total + u_total} // {len(record_lines)}\n"
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
