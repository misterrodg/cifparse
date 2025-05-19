class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.facility_id = (6, 10)
        self.facility_region = (10, 12)
        self.sub_code = (12, 13)
        self.loc_id = (13, 17)
        self.marker_type = (17, 20)
        # PAD 1
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
        self.frequency = (22, 27)
        self.runway_id = (27, 32)
        self.marker_lat = (32, 41)
        self.marker_lon = (41, 51)
        self.true_bearing = (51, 55)
        self.locator_lat = (55, 64)
        self.locator_lon = (64, 74)
        self.locator_class = (74, 79)
        self.locator_fac_char = (79, 84)
        self.locator_id = (84, 88)
        # PAD 2
        self.mag_var = (90, 95)
        # PAD 2
        self.fac_elev = (97, 102)
        # RESERVED 21


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        # RESERVED 100


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
