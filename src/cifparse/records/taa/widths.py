class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        self.sub_code = (12, 13)
        self.iap_id = (13, 19)
        self.taa_si = (19, 20)
        self.procedure_turn = (20, 24)
        # PAD 5
        self.iaf_point_id = (29, 34)
        self.iaf_point_region = (34, 36)
        self.iaf_point_sec_code = (36, 37)
        self.iaf_point_sub_code = (37, 38)
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
        # PAD 1
        self.mag_true = (40, 41)
        self.radius_1 = (41, 45)
        self.bearing_1 = (45, 51)
        self.min_alt_1 = (51, 54)
        self.radius_2 = (54, 58)
        self.bearing_2 = (58, 64)
        self.min_alt_2 = (64, 67)
        self.radius_3 = (67, 71)
        self.bearing_3 = (71, 77)
        self.min_alt_3 = (77, 80)
        self.radius_4 = (80, 84)
        self.bearing_4 = (84, 90)
        self.min_alt_4 = (90, 93)
        self.radius_5 = (93, 97)
        self.bearing_5 = (97, 103)
        self.min_alt_5 = (103, 106)
        self.radius_6 = (106, 110)
        self.bearing_6 = (110, 116)
        self.min_alt_6 = (116, 119)
        # PAD 3


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.notes = (40, 109)
        # RESERVED 14


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
