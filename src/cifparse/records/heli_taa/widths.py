from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        # PAD 1
        self.heliport_id = (6, 10, field_56)
        self.heliport_region = (10, 12, field_514)
        self.sub_code = (12, 13, field_55)
        self.iap_id = (13, 19, field_510)
        self.taa_si = (19, 20, field_5272)
        self.procedure_turn = (20, 24, field_5271)
        # PAD 5
        self.iaf_point_id = (29, 34, field_5273)
        self.iaf_point_region = (34, 36, field_514)
        self.iaf_point_sec_code = (36, 37, field_54)
        self.iaf_point_sub_code = (37, 38, field_55)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        # PAD 1
        self.mag_true = (40, 41, field_5165)
        self.radius_1 = (41, 45, field_5274)
        self.bearing_1 = (45, 51, field_5146)
        self.min_alt_1 = (51, 54, field_5147)
        self.radius_2 = (54, 58, field_5274)
        self.bearing_2 = (58, 64, field_5146)
        self.min_alt_2 = (64, 67, field_5147)
        self.radius_3 = (67, 71, field_5274)
        self.bearing_3 = (71, 77, field_5146)
        self.min_alt_3 = (77, 80, field_5147)
        self.radius_4 = (80, 84, field_5274)
        self.bearing_4 = (84, 90, field_5146)
        self.min_alt_4 = (90, 93, field_5147)
        self.radius_5 = (93, 97, field_5274)
        self.bearing_5 = (97, 103, field_5146)
        self.min_alt_5 = (103, 106, field_5147)
        self.radius_6 = (106, 110, field_5274)
        self.bearing_6 = (110, 116, field_5146)
        self.min_alt_6 = (116, 119, field_5147)
        # PAD 3


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.notes = (40, 109, field_561)
        # RESERVED 14


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
