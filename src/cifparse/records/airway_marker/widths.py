class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        # PAD 7
        self.marker_id = (13, 17)
        # PAD 2
        self.marker_region = (19, 21)
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
        self.marker_code = (22, 26)
        # PAD 1
        self.shape = (27, 28)
        self.environment = (28, 29)
        # PAD 3
        self.lat = (32, 41)
        self.lon = (41, 51)
        self.true_bearing = (51, 55)
        # RESERVED 19
        self.mag_var = (74, 79)
        self.fac_elev = (79, 84)
        self.datum_code = (84, 87)
        # PAD 6
        self.marker_name = (93, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        # RESERVED 100


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
