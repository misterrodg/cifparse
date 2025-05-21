class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.heliport_id = (6, 10)
        self.heliport_region = (10, 12)
        self.sub_code = (12, 13)
        self.msa_center = (13, 18)
        self.msa_center_region = (18, 20)
        self.msa_center_sec_code = (20, 21)
        self.msa_center_sub_code = (21, 22)
        self.mult_code = (22, 23)
        # RESERVED 15
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        # PAD 3
        self.bearing_1 = (42, 48)
        self.min_alt_1 = (48, 51)
        self.radius_1 = (51, 53)
        self.bearing_2 = (53, 59)
        self.min_alt_2 = (59, 62)
        self.radius_2 = (62, 64)
        self.bearing_3 = (64, 70)
        self.min_alt_3 = (70, 73)
        self.radius_3 = (73, 75)
        self.bearing_4 = (75, 81)
        self.min_alt_4 = (81, 84)
        self.radius_4 = (84, 86)
        self.bearing_5 = (86, 92)
        self.min_alt_5 = (92, 95)
        self.radius_5 = (95, 97)
        self.bearing_6 = (97, 103)
        self.min_alt_6 = (103, 106)
        self.radius_6 = (106, 108)
        self.bearing_7 = (108, 114)
        self.min_alt_7 = (114, 117)
        self.radius_7 = (117, 119)
        self.mag_true = (119, 120)
        # PAD 3


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.notes = (40, 109)
        # RESERVED 31


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
