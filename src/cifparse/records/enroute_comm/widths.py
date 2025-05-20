class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.fir_rdo_id = (6, 10)
        self.fir_uir_addr = (10, 14)
        self.fir_uir_ind = (14, 15)
        # PAD 3
        self.remote_site_name = (18, 43)
        self.comm_type = (43, 46)
        self.comm_freq = (46, 53)
        self.gt = (53, 54)
        self.freq_unit = (54, 55)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (55, 56)
        self.serv_ind = (56, 59)
        self.radar = (59, 60)
        self.modulation = (60, 61)
        self.sig_em = (61, 62)
        self.lat = (62, 71)
        self.lon = (71, 81)
        self.mag_var = (81, 86)
        self.fac_elev = (86, 91)
        self.h24_ind = (91, 92)
        self.alt_desc = (92, 93)
        self.alt_1 = (93, 98)
        self.alt_2 = (98, 103)
        self.remote_fac = (103, 107)
        self.remote_region = (107, 109)
        self.remote_sec_code = (109, 110)
        self.remote_sub_code = (119, 111)
        # RESERVED 12


class CombinedIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (55, 56)
        self.application = (56, 57)
        self.time_zone = (57, 58)
        self.notam = (58, 59)
        self.daylight_ind = (59, 60)
        self.op_time = (60, 70)
        # RESERVED 23
        self.callsign = (93, 123)


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (55, 56)
        self.application = (56, 57)
        # PAD 3
        self.op_time_1 = (60, 70)
        self.op_time_2 = (70, 80)
        self.op_time_3 = (80, 90)
        self.op_time_4 = (90, 100)
        self.op_time_5 = (100, 110)
        self.op_time_6 = (110, 120)
        # RESERVED 3


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_com = CombinedIndices()
w_tim = TimeIndices()
