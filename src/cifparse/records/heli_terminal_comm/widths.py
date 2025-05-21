class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.heliport_id = (6, 10)
        self.heliport_region = (10, 12)
        self.sub_code = (12, 13)
        self.comm_type = (13, 16)
        self.comm_freq = (16, 23)
        self.gt = (23, 24)
        self.freq_unit = (24, 25)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (25, 26)
        self.serv_ind = (26, 29)
        self.radar = (29, 30)
        self.modulation = (30, 31)
        self.sig_em = (31, 32)
        self.lat = (32, 41)
        self.lon = (41, 51)
        self.mag_var = (51, 56)
        self.fac_elev = (56, 61)
        self.h24_ind = (61, 62)
        self.sector = (62, 68)
        self.alt_desc = (68, 69)
        self.alt_1 = (69, 74)
        self.alt_2 = (74, 79)
        self.sector_fac = (79, 83)
        self.sector_region = (83, 85)
        self.sector_sec_code = (85, 86)
        self.sector_sub_code = (86, 87)
        self.dist_desc = (87, 88)
        self.comm_dist = (88, 90)
        self.remote_fac = (90, 94)
        self.remote_region = (94, 96)
        self.remote_sec_code = (96, 97)
        self.remote_sub_code = (97, 98)
        self.callsign = (98, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (25, 26)
        self.application = (26, 27)
        self.narrative = (27, 87)
        # RESERVED 36


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (25, 26)
        self.application = (26, 27)
        self.time_zone = (27, 28)
        self.notam = (28, 29)
        self.daylight_ind = (29, 30)
        self.op_time_1 = (30, 40)
        self.op_time_2 = (40, 50)
        self.op_time_3 = (50, 60)
        self.op_time_4 = (60, 70)
        self.op_time_5 = (70, 80)
        self.op_time_6 = (80, 90)
        self.op_time_7 = (90, 100)
        # RESERVED 23


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_tim = TimeIndices()
