from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        # PAD 1
        self.facility_id = (6, 10, field_56)
        self.facility_region = (10, 12, field_514)
        self.sub_code = (12, 13, field_55)
        self.loc_id = (13, 17, field_544)
        self.marker_type = (17, 20, field_599)
        # PAD 1
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
        self.runway_id = (27, 32, field_546)
        self.marker_lat = (32, 41, field_536)
        self.marker_lon = (41, 51, field_537)
        self.true_bearing = (51, 55, field_5100)
        self.locator_lat = (55, 64, field_536)
        self.locator_lon = (64, 74, field_537)
        self.locator_class = (74, 79, field_535)
        self.locator_fac_char = (79, 84, field_593)
        self.locator_id = (84, 88, field_533)
        # PAD 2
        self.mag_var = (90, 95, field_539)
        # PAD 2
        self.fac_elev = (97, 102, field_592)
        # RESERVED 21


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        # RESERVED 100


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
