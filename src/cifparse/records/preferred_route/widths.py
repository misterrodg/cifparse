from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        # PAD 7
        self.route_id = (13, 23, field_58)
        self.use = (23, 25, field_5220)
        self.seq_no = (25, 29, field_512)
        # PAD 9
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
        self.fix_id = (39, 44, field_583)
        self.fix_region = (44, 46, field_514)
        self.fix_sec_code = (46, 47, field_54)
        self.fix_sub_code = (47, 48, field_55)
        self.via = (48, 51, field_577)
        self.path_id = (51, 57, field_578)
        self.path_area = (57, 60, field_53)
        self.level = (60, 61, field_519)
        self.route_type = (61, 62, field_57)
        self.int_point = (62, 67, field_5194)
        self.int_region = (67, 69, field_514)
        self.int_sec_code = (69, 70, field_54)
        self.int_sub_code = (70, 71, field_55)
        self.term_point = (71, 76, field_5194)
        self.term_region = (76, 78, field_514)
        self.term_sec_code = (78, 79, field_54)
        self.term_sub_code = (79, 80, field_55)
        self.min_alt = (80, 85, field_530)
        self.max_alt = (85, 90, field_5127)
        self.time_zone = (90, 91, field_5131)
        self.aircraft_use = (91, 93, field_5221)
        self.direction = (93, 94, field_5115)
        self.alt_desc = (94, 95, field_529)
        self.alt_1 = (95, 100, field_530)
        self.alt_2 = (100, 105, field_530)
        # RESERVED 18


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.notes = (40, 109, field_561)
        # RESERVED 14


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.time_zone = (40, 41, field_5131)
        self.daylight_ind = (41, 42, field_5138)
        self.op_time_1 = (42, 52, field_5195)
        self.op_time_2 = (52, 62, field_5195)
        self.op_time_3 = (62, 72, field_5195)
        self.op_time_4 = (72, 82, field_5195)
        self.op_time_5 = (82, 92, field_5195)
        self.op_time_6 = (92, 102, field_5195)
        self.op_time_7 = (102, 112, field_5195)
        # RESERVED 11


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_tim = TimeIndices()
