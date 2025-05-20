class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        # PAD 3
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.cruise_id = (6, 8)
        self.seq_no = (8, 9)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.course_from = (28, 32)
        self.course_to = (32, 36)
        self.mt_ind = (36, 37)
        # PAD 2
        self.level_from_1 = (39, 44)
        self.vert_sep_1 = (44, 49)
        self.level_to_1 = (49, 54)
        self.level_from_2 = (39, 44)
        self.vert_sep_2 = (44, 49)
        self.level_to_2 = (49, 54)
        self.level_from_3 = (39, 44)
        self.vert_sep_3 = (44, 49)
        self.level_to_3 = (49, 54)
        self.level_from_4 = (39, 44)
        self.vert_sep_4 = (44, 49)
        self.level_to_4 = (49, 54)
        # RESERVED 24


w_bas = BaseIndices()
w_pri = PrimaryIndices()
