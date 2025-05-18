class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        # PAD 1
        self.vhf_id = (13, 17)
        # PAD 2
        self.vhf_region = (19, 21)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.frequency = (22, 27)
        self.nav_class = (27, 32)
        self.lat = (32, 41)
        self.lon = (41, 51)
        self.dme_id = (51, 55)
        self.dme_lat = (55, 64)
        self.dme_lon = (64, 74)
        self.mag_var = (74, 79)
        self.dme_elevation = (79, 84)
        self.figure_of_merit = (84, 85)
        self.dme_bias = (85, 87)
        self.frequency_protection = (87, 90)
        self.datum_code = (90, 93)
        self.vhf_name = (93, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.notes = (23, 92)
        # RESERVED 31


class SimulationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        # PAD 4
        self.fac_char = (27, 32)
        # PAD 42
        self.d_mag_var = (74, 79)
        self.fac_elev = (79, 84)
        # RESERVED 39


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.fir_ident = (23, 27)
        self.uir_ident = (27, 31)
        self.se_ind = (31, 32)
        self.se_date = (32, 43)
        # RESERVED 80


class PlanningContinuationIndices(PrimaryIndices):
    def __init__(self):
        super().__init__()


class LimitationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.nlc = (23, 24)
        self.cai = (24, 25)
        self.seq_no = (25, 27)
        self.sector_1 = (27, 29)
        self.dist_desc_1 = (29, 30)
        self.dist_limit_1 = (30, 36)
        self.alt_desc_1 = (36, 37)
        self.alt_limit_1 = (37, 43)
        self.sector_2 = (43, 45)
        self.dist_desc_2 = (45, 46)
        self.dist_limit_2 = (46, 52)
        self.alt_desc_2 = (52, 53)
        self.alt_limit_2 = (53, 59)
        self.sector_3 = (59, 61)
        self.dist_desc_3 = (61, 62)
        self.dist_limit_3 = (62, 68)
        self.alt_desc_3 = (68, 69)
        self.alt_limit_3 = (69, 75)
        self.sector_4 = (75, 77)
        self.dist_desc_4 = (77, 78)
        self.dist_limit_4 = (78, 84)
        self.alt_desc_4 = (84, 85)
        self.alt_limit_4 = (85, 91)
        self.sector_5 = (91, 93)
        self.dist_desc_5 = (93, 94)
        self.dist_limit_5 = (94, 100)
        self.alt_desc_5 = (100, 101)
        self.alt_limit_5 = (101, 107)
        self.seq_ind = (107, 108)
        # RESERVED 15


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_sim = SimulationIndices()
w_pla = PlanningIndices()
w_plc = PlanningContinuationIndices()
w_lim = LimitationIndices()
