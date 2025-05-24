from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.environment_id = (6, 10, field_541)
        self.environment_region = (10, 12, field_514)
        # PAD 15
        self.dup_ind = (27, 29, field_5114)
        self.point_id = (29, 34, field_513)
        self.point_region = (34, 36, field_514)
        self.point_sec_code = (36, 37, field_54)
        self.point_sub_code = (37, 38, field_55)
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
        self.in_course = (39, 43, field_562)
        self.turn_dir = (43, 44, field_563)
        self.leg_length = (44, 47, field_564)
        self.leg_time = (47, 49, field_565)
        self.min_alt = (49, 54, field_530)
        self.max_alt = (54, 59, field_5127)
        self.hold_speed = (59, 62, field_5175)
        self.rnp = (62, 65, field_5211)
        self.arc_radius = (65, 71, field_5204)
        # RESERVED 27
        self.hold_name = (98, 123, field_560)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.notes = (40, 109, field_561)
        # RESERVED 14


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
