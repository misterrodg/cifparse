class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.fac_id = (6, 10)
        self.fac_region = (10, 12)
        self.sub_code = (12, 13)
        self.gls_ref_id = (13, 17)
        self.gls_cat = (17, 18)
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
        self.gls_channel = (22, 27)
        self.runway_id = (27, 32)
        # PAD 19
        self.gls_bearing = (51, 55)
        self.station_lat = (55, 64)
        self.station_lon = (64, 74)
        self.gls_id = (74, 78)
        # PAD 5
        self.svc_vol = (83, 85)
        self.tdma_slots = (85, 87)
        self.min_elev_angle = (87, 90)
        self.mag_var = (90, 95)
        # RESERVED 2
        self.station_elev = (97, 102)
        self.datum_code = (102, 105)
        self.station_type = (105, 108)
        # PAD 2
        self.wgs84_elev = (110, 115)
        # PAD 8


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        # RESERVED 100


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
