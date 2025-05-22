class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.point_id = (6, 11)
        self.point_region = (11, 13)
        self.point_sec_code = (13, 14)
        self.point_sub_code = (14, 15)
        self.art = (15, 17)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        # PAD 2
        self.dta_1 = (19, 22)
        self.alt_type_1 = (22, 23)
        self.alt_id_1 = (23, 33)
        # PAD 2
        self.dta_2 = (35, 38)
        self.alt_type_2 = (38, 39)
        self.alt_id_2 = (39, 49)
        # PAD 2
        self.dta_3 = (51, 54)
        self.alt_type_3 = (54, 55)
        self.alt_id_3 = (55, 65)
        # PAD 2
        self.dta_4 = (67, 70)
        self.alt_type_4 = (70, 71)
        self.alt_id_4 = (71, 81)
        # PAD 2
        self.dta_5 = (83, 86)
        self.alt_type_5 = (86, 87)
        self.alt_id_5 = (87, 97)
        # PAD 2
        self.dta_6 = (99, 102)
        self.alt_type_6 = (102, 103)
        self.alt_id_6 = (103, 113)
        # RESERVED 10


w_bas = BaseIndices()
w_pri = PrimaryIndices()
