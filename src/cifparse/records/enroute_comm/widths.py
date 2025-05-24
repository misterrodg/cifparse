from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.fir_rdo_id = (6, 10, field_5190)
        self.fir_uir_addr = (10, 14, field_5151)
        self.fir_uir_ind = (14, 15, field_5117)
        # PAD 3
        self.remote_site_name = (18, 43, field_5189)
        self.comm_type = (43, 46, field_5101)
        self.comm_freq = (46, 53, field_5103)
        self.gt = (53, 54, field_5182)
        self.freq_unit = (54, 55, field_5104)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (55, 56, field_516)
        self.serv_ind = (56, 59, field_5106)
        self.radar = (59, 60, field_5102)
        self.modulation = (60, 61, field_5198)
        self.sig_em = (61, 62, field_5199)
        self.lat = (62, 71, field_536)
        self.lon = (71, 81, field_537)
        self.mag_var = (81, 86, field_539)
        self.fac_elev = (86, 91, field_592)
        self.h24_ind = (91, 92, field_5181)
        self.alt_desc = (92, 93, field_529)
        self.alt_1 = (93, 98, field_5184)
        self.alt_2 = (98, 103, field_5184)
        self.remote_fac = (103, 107, field_5200)
        self.remote_region = (107, 109, field_514)
        self.remote_sec_code = (109, 110, field_54)
        self.remote_sub_code = (119, 111, field_55)
        # RESERVED 12


class CombinedIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (55, 56, field_516)
        self.application = (56, 57, field_591)
        self.time_zone = (57, 58, field_5131)
        self.notam = (58, 59, field_5132)
        self.daylight_ind = (59, 60, field_5138)
        self.op_time = (60, 70, field_5195)
        # RESERVED 23
        self.callsign = (93, 123, field_5105)


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (55, 56, field_516)
        self.application = (56, 57, field_591)
        # PAD 3
        self.op_time_1 = (60, 70, field_5195)
        self.op_time_2 = (70, 80, field_5195)
        self.op_time_3 = (80, 90, field_5195)
        self.op_time_4 = (90, 100, field_5195)
        self.op_time_5 = (100, 110, field_5195)
        self.op_time_6 = (110, 120, field_5195)
        # RESERVED 3


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_com = CombinedIndices()
w_tim = TimeIndices()
