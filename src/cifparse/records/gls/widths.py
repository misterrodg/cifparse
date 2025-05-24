from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        # PAD 1
        self.fac_id = (6, 10, field_56)
        self.fac_region = (10, 12, field_514)
        self.sub_code = (12, 13, field_55)
        self.gls_ref_id = (13, 17, field_544)
        self.gls_cat = (17, 18, field_580)
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
        self.gls_channel = (22, 27, field_5244)
        self.runway_id = (27, 32, field_546)
        # PAD 19
        self.gls_bearing = (51, 55, field_547)
        self.station_lat = (55, 64, field_536)
        self.station_lon = (64, 74, field_537)
        self.gls_id = (74, 78, field_5243)
        # PAD 5
        self.svc_vol = (83, 85, field_5245)
        self.tdma_slots = (85, 87, field_5246)
        self.min_elev_angle = (87, 90, field_552)
        self.mag_var = (90, 95, field_539)
        # RESERVED 2
        self.station_elev = (97, 102, field_574)
        self.datum_code = (102, 105, field_5197)
        self.station_type = (105, 108, field_5247)
        # PAD 2
        self.wgs84_elev = (110, 115, field_5248)
        # PAD 8


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        # RESERVED 100


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
