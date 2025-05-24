from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.airport_id = (6, 10, field_56)
        self.airport_region = (10, 12, field_514)
        # PAD 1
        self.vhf_id = (13, 17, field_533)
        # PAD 2
        self.vhf_region = (19, 21, field_514)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.frequency = (22, 27, field_534)
        self.nav_class = (27, 32, field_535)
        self.lat = (32, 41, field_536)
        self.lon = (41, 51, field_537)
        self.dme_id = (51, 55, field_538)
        self.dme_lat = (55, 64, field_536)
        self.dme_lon = (64, 74, field_537)
        self.mag_var = (74, 79, field_566)
        self.dme_elevation = (79, 84, field_540)
        self.figure_of_merit = (84, 85, field_5149)
        self.dme_bias = (85, 87, field_590)
        self.frequency_protection = (87, 90, field_5150)
        self.datum_code = (90, 93, field_5197)
        self.vhf_name = (93, 123, field_571)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        self.notes = (23, 92, field_561)
        # RESERVED 31


class SimulationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        # PAD 4
        self.fac_char = (27, 32, field_593)
        # PAD 42
        self.d_mag_var = (74, 79, field_539)
        self.fac_elev = (79, 84, field_592)
        # RESERVED 39


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        self.fir_ident = (23, 27, field_5116)
        self.uir_ident = (27, 31, field_5116)
        self.se_ind = (31, 32, field_5152)
        self.se_date = (32, 43, field_5153)
        # RESERVED 80


class PlanningContinuationIndices(PrimaryIndices):
    def __init__(self):
        super().__init__()


class LimitationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        self.nlc = (23, 24, field_5205)
        self.cai = (24, 25, field_5206)
        self.seq_no = (25, 27, field_512)
        self.sector_1 = (27, 29, field_5207)
        self.dist_desc_1 = (29, 30, field_5187)
        self.dist_limit_1 = (30, 36, field_5208)
        self.alt_desc_1 = (36, 37, field_529)
        self.alt_limit_1 = (37, 43, field_5209)
        self.sector_2 = (43, 45, field_5207)
        self.dist_desc_2 = (45, 46, field_5187)
        self.dist_limit_2 = (46, 52, field_5208)
        self.alt_desc_2 = (52, 53, field_529)
        self.alt_limit_2 = (53, 59, field_5209)
        self.sector_3 = (59, 61, field_5207)
        self.dist_desc_3 = (61, 62, field_5187)
        self.dist_limit_3 = (62, 68, field_5208)
        self.alt_desc_3 = (68, 69, field_529)
        self.alt_limit_3 = (69, 75, field_5209)
        self.sector_4 = (75, 77, field_5207)
        self.dist_desc_4 = (77, 78, field_5187)
        self.dist_limit_4 = (78, 84, field_5208)
        self.alt_desc_4 = (84, 85, field_529)
        self.alt_limit_4 = (85, 91, field_5209)
        self.sector_5 = (91, 93, field_5207)
        self.dist_desc_5 = (93, 94, field_5187)
        self.dist_limit_5 = (94, 100, field_5208)
        self.alt_desc_5 = (100, 101, field_529)
        self.alt_limit_5 = (101, 107, field_5209)
        self.seq_ind = (107, 108, field_5210)
        # RESERVED 15


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_sim = SimulationIndices()
w_pla = PlanningIndices()
w_plc = PlanningContinuationIndices()
w_lim = LimitationIndices()
