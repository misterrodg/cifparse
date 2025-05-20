class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.fir_uir_id = (6, 10)
        self.fir_uir_addr = (10, 14)
        self.fir_uir_ind = (14, 15)
        self.seq_no = (15, 19)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (19, 20)
        self.adj_fir_id = (20, 24)
        self.adj_uir_id = (24, 28)
        self.rus = (28, 29)
        self.rua = (29, 30)
        self.entry = (30, 31)
        # PAD 1
        self.boundary_via = (32, 34)
        self.fir_uir_lat = (34, 43)
        self.fir_uir_lon = (43, 53)
        self.arc_lat = (53, 62)
        self.arc_lon = (62, 72)
        self.arc_dist = (72, 76)
        self.arc_bearing = (76, 80)
        self.fir_upper_limit = (80, 85)
        self.uir_lower_limit = (85, 90)
        self.uir_upper_limit = (90, 95)
        self.tc_ind = (95, 97)
        # PAD 1
        self.fir_uir_name = (98, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (19, 20)
        self.application = (20, 21)
        # RESERVED 102


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
