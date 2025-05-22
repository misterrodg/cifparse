class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.table_id = (6, 8)
        self.seq_no = (8, 9)
        self.geo_entity = (9, 38)
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
        self.pref_route_id_1 = (40, 50)
        self.et_ind_1 = (50, 52)
        self.pref_route_id_2 = (52, 62)
        self.et_ind_2 = (62, 64)
        self.pref_route_id_3 = (64, 74)
        self.et_ind_3 = (74, 76)
        self.pref_route_id_4 = (76, 86)
        self.et_ind_4 = (86, 88)
        self.pref_route_id_5 = (88, 98)
        self.et_ind_5 = (98, 100)
        self.pref_route_id_6 = (100, 110)
        self.et_ind_6 = (100, 102)
        # PAD 11


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        # RESERVED 83


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
