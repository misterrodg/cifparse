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
        self.msa_center = (13, 18, field_5144)
        self.msa_center_region = (18, 20, field_514)
        self.msa_center_sec_code = (20, 21, field_54)
        self.msa_center_sub_code = (21, 22, field_55)
        self.mult_code = (22, 23, field_5130)
        # RESERVED 15
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
        # PAD 3
        self.bearing_1 = (42, 48, field_5146)
        self.min_alt_1 = (48, 51, field_5147)
        self.radius_1 = (51, 53, field_5145)
        self.bearing_2 = (53, 59, field_5146)
        self.min_alt_2 = (59, 62, field_5147)
        self.radius_2 = (62, 64, field_5145)
        self.bearing_3 = (64, 70, field_5146)
        self.min_alt_3 = (70, 73, field_5147)
        self.radius_3 = (73, 75, field_5145)
        self.bearing_4 = (75, 81, field_5146)
        self.min_alt_4 = (81, 84, field_5147)
        self.radius_4 = (84, 86, field_5145)
        self.bearing_5 = (86, 92, field_5146)
        self.min_alt_5 = (92, 95, field_5147)
        self.radius_5 = (95, 97, field_5145)
        self.bearing_6 = (97, 103, field_5146)
        self.min_alt_6 = (103, 106, field_5147)
        self.radius_6 = (106, 108, field_5145)
        self.bearing_7 = (108, 114, field_5146)
        self.min_alt_7 = (114, 117, field_5147)
        self.radius_7 = (117, 119, field_5145)
        self.mag_true = (119, 120, field_5165)
        # PAD 3


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.notes = (40, 109, field_561)
        # RESERVED 31


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
