from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        # PAD 1
        self.airport_id = (6, 10, field_56)
        self.airport_region = (10, 12, field_514)
        self.sub_code = (12, 13, field_55)
        self.loc_id = (13, 17, field_544)
        self.cat = (17, 18, field_580)
        # PAD 3
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
        self.frequency = (22, 27, field_545)
        self.runway_id = (27, 32, field_546)
        self.loc_lat = (32, 41, field_536)
        self.loc_lon = (41, 51, field_537)
        self.loc_bearing = (51, 55, field_547)
        self.gs_lat = (55, 64, field_536)
        self.gs_lon = (64, 74, field_537)
        self.loc_dist = (74, 78, field_548)
        self.plus_minus = (78, 79, field_549)
        self.gs_thr_dist = (79, 83, field_550)
        self.loc_width = (83, 87, field_551)
        self.gs_angle = (87, 90, field_552)
        self.mag_var = (90, 95, field_566)
        self.tch = (95, 97, field_567)
        self.gs_elevation = (97, 102, field_574)
        self.support_fac = (102, 106, field_533)
        self.support_region = (106, 108, field_514)
        self.support_sec_code = (108, 109, field_54)
        self.support_sub_code = (109, 110, field_55)
        # RESERVED 13


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
        # PAD 19
        self.true_bearing = (51, 55, field_594)
        self.source = (55, 56, field_595)
        # PAD 31
        self.beam_width = (87, 90, field_596)
        self.app_ident_1 = (90, 96, field_510)
        self.app_ident_2 = (96, 102, field_510)
        self.app_ident_3 = (102, 108, field_510)
        self.app_ident_4 = (108, 114, field_510)
        self.app_ident_5 = (114, 120, field_510)
        # PAD 3


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_sim = SimulationIndices()
