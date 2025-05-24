from cifparse.functions.record import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.table_id = (6, 8, field_5218)
        self.seq_no = (8, 9, field_512)
        self.geo_entity = (9, 38, field_5219)
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
        self.pref_route_id_1 = (40, 50, field_58)
        self.et_ind_1 = (50, 52, field_5220)
        self.pref_route_id_2 = (52, 62, field_58)
        self.et_ind_2 = (62, 64, field_5220)
        self.pref_route_id_3 = (64, 74, field_58)
        self.et_ind_3 = (74, 76, field_5220)
        self.pref_route_id_4 = (76, 86, field_58)
        self.et_ind_4 = (86, 88, field_5220)
        self.pref_route_id_5 = (88, 98, field_58)
        self.et_ind_5 = (98, 100, field_5220)
        self.pref_route_id_6 = (100, 110, field_58)
        self.et_ind_6 = (100, 102, field_5220)
        # PAD 11


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        # RESERVED 83


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
