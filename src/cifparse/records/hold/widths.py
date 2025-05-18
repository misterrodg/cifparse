class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.environment = (6, 10)
        self.environment_region = (10, 12)
        # PAD 15
        self.dup_ind = (27, 29)
        self.point_id = (29, 34)
        self.point_region = (34, 36)
        self.point_sec_code = (36, 37)
        self.point_sub_code = (37, 38)
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
        self.in_course = (39, 43)
        self.turn_dir = (43, 44)
        self.leg_length = (44, 47)
        self.leg_time = (47, 49)
        self.min_alt = (49, 54)
        self.max_alt = (54, 59)
        self.hold_speed = (59, 62)
        self.rnp = (62, 65)
        self.arc_radius = (65, 71)
        # RESERVED 27
        self.hold_name = (98, 123)


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
