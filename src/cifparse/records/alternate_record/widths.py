from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.point_id = (6, 11, field_575)
        self.point_region = (11, 13, field_514)
        self.point_sec_code = (13, 14, field_54)
        self.point_sub_code = (14, 15, field_55)
        self.art = (15, 17, field_5250)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        # PAD 2
        self.dta_1 = (19, 22, field_5251)
        self.alt_type_1 = (22, 23, field_5252)
        self.alt_id_1 = (23, 33, field_5253)
        # PAD 2
        self.dta_2 = (35, 38, field_5251)
        self.alt_type_2 = (38, 39, field_5252)
        self.alt_id_2 = (39, 49, field_5253)
        # PAD 2
        self.dta_3 = (51, 54, field_5251)
        self.alt_type_3 = (54, 55, field_5252)
        self.alt_id_3 = (55, 65, field_5253)
        # PAD 2
        self.dta_4 = (67, 70, field_5251)
        self.alt_type_4 = (70, 71, field_5252)
        self.alt_id_4 = (71, 81, field_5253)
        # PAD 2
        self.dta_5 = (83, 86, field_5251)
        self.alt_type_5 = (86, 87, field_5252)
        self.alt_id_5 = (87, 97, field_5253)
        # PAD 2
        self.dta_6 = (99, 102, field_5251)
        self.alt_type_6 = (102, 103, field_5252)
        self.alt_id_6 = (103, 113, field_5253)
        # RESERVED 10


w_bas = BaseIndices()
w_pri = PrimaryIndices()
