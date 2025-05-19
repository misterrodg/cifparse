class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        self.sub_code = (12, 13)
        self.loc_id = (13, 17)
        self.cat = (17, 18)
        # PAD 3
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
        self.runway_id = (27, 32)
        self.loc_lat = (32, 41)
        self.loc_lon = (41, 51)
        self.loc_bearing = (51, 55)
        self.gs_lat = (55, 64)
        self.gs_lon = (64, 74)
        self.loc_dist = (74, 78)
        self.plus_minus = (78, 79)
        self.gs_thr_dist = (79, 83)
        self.loc_width = (83, 87)
        self.gs_angle = (87, 90)
        self.mag_var = (90, 95)
        self.tch = (95, 97)
        self.gs_elevation = (97, 102)
        self.support_fac = (102, 106)
        self.support_region = (106, 108)
        self.support_sec_code = (108, 109)
        self.support_sub_code = (109, 110)
        # RESERVED 13


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
        # PAD 19
        self.true_bearing = (51, 55)
        self.source = (55, 56)
        # PAD 31
        self.beam_width = (87, 90)
        self.app_ident_1 = (90, 96)
        self.app_ident_2 = (96, 102)
        self.app_ident_3 = (102, 108)
        self.app_ident_4 = (108, 114)
        self.app_ident_5 = (114, 120)
        # PAD 3


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_sim = SimulationIndices()
