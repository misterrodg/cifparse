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
        self.comm_type = (13, 16, field_5101)
        self.comm_freq = (16, 23, field_5103)
        self.gt = (23, 24, field_5182)
        self.freq_unit = (24, 25, field_5104)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (25, 26, field_516)
        self.serv_ind = (26, 29, field_5106)
        self.radar = (29, 30, field_5102)
        self.modulation = (30, 31, field_5198)
        self.sig_em = (31, 32, field_5199)
        self.lat = (32, 41, field_536)
        self.lon = (41, 51, field_537)
        self.mag_var = (51, 56, field_539)
        self.fac_elev = (56, 61, field_592)
        self.h24_ind = (61, 62, field_5181)
        self.sector = (62, 68, field_5183)
        self.alt_desc = (68, 69, field_529)
        self.alt_1 = (69, 74, field_5184)
        self.alt_2 = (74, 79, field_5184)
        self.sector_fac = (79, 83, field_5185)
        self.sector_region = (83, 85, field_514)
        self.sector_sec_code = (85, 86, field_54)
        self.sector_sub_code = (86, 87, field_55)
        self.dist_desc = (87, 88, field_5187)
        self.comm_dist = (88, 90, field_5188)
        self.remote_fac = (90, 94, field_5200)
        self.remote_region = (94, 96, field_514)
        self.remote_sec_code = (96, 97, field_54)
        self.remote_sub_code = (97, 98, field_55)
        self.callsign = (98, 123, field_5105)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (25, 26, field_516)
        self.application = (26, 27, field_591)
        self.narrative = (27, 87, field_5186)
        # RESERVED 36


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (25, 26, field_516)
        self.application = (26, 27, field_591)
        self.time_zone = (27, 28, field_5131)
        self.notam = (28, 29, field_5132)
        self.daylight_ind = (29, 30, field_5138)
        self.op_time_1 = (30, 40, field_5195)
        self.op_time_2 = (40, 50, field_5195)
        self.op_time_3 = (50, 60, field_5195)
        self.op_time_4 = (60, 70, field_5195)
        self.op_time_5 = (70, 80, field_5195)
        self.op_time_6 = (80, 90, field_5195)
        self.op_time_7 = (90, 100, field_5195)
        # RESERVED 23


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_tim = TimeIndices()
