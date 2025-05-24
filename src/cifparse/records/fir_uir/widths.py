from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.fir_uir_id = (6, 10, field_5116)
        self.fir_uir_addr = (10, 14, field_5151)
        self.fir_uir_ind = (14, 15, field_5117)
        self.seq_no = (15, 19, field_512)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (19, 20, field_516)
        self.adj_fir_id = (20, 24, field_5116)
        self.adj_uir_id = (24, 28, field_5116)
        self.rus = (28, 29, field_5122)
        self.rua = (29, 30, field_5123)
        self.entry = (30, 31, field_5124)
        # PAD 1
        self.boundary_via = (32, 34, field_5118)
        self.fir_uir_lat = (34, 43, field_536)
        self.fir_uir_lon = (43, 53, field_537)
        self.arc_lat = (53, 62, field_536)
        self.arc_lon = (62, 72, field_537)
        self.arc_dist = (72, 76, field_5119)
        self.arc_bearing = (76, 80, field_5120)
        self.fir_upper_limit = (80, 85, field_5121)
        self.uir_lower_limit = (85, 90, field_5121)
        self.uir_upper_limit = (90, 95, field_5121)
        self.cruise_id = (95, 97, field_5134)
        # PAD 1
        self.fir_uir_name = (98, 123, field_5125)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (19, 20, field_516)
        self.application = (20, 21, field_591)
        # RESERVED 102


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
