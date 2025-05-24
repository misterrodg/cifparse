from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        # PAD 7
        self.marker_id = (13, 17, field_5110)
        # PAD 2
        self.marker_region = (19, 21, field_514)
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
        self.marker_code = (22, 26, field_5111)
        # PAD 1
        self.shape = (27, 28, field_5112)
        self.environment_id = (28, 29, field_5113)
        # PAD 3
        self.lat = (32, 41, field_536)
        self.lon = (41, 51, field_537)
        self.true_bearing = (51, 55, field_5100)
        # RESERVED 19
        self.mag_var = (74, 79, field_539)
        self.fac_elev = (79, 84, field_592)
        self.datum_code = (84, 87, field_5197)
        # PAD 6
        self.marker_name = (93, 123, field_571)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        # RESERVED 100


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
