class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        self.sub_code = (12, 13)
        self.gate_id = (13, 18)
        # PAD 3
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
        # PAD 10
        self.lat = (32, 41)
        self.lon = (41, 51)
        self.mag_hdg = (51, 55)
        # RESERVED 43
        self.gate_name = (98, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.notes = (23, 92)
        # RESERVED 31


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
