class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        # PAD 7
        self.route_id = (13, 23)
        self.use = (23, 25)
        self.seq_no = (25, 29)
        # PAD 9
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
        self.fix_id = (39, 44)
        self.fix_region = (44, 46)
        self.fix_sec_code = (46, 47)
        self.fix_sub_code = (47, 48)
        self.via = (48, 51)
        self.path_id = (51, 57)
        self.path_area = (57, 60)
        self.level = (60, 61)
        self.route_type = (61, 62)
        self.int_point = (62, 67)
        self.int_region = (67, 69)
        self.int_sec_code = (69, 70)
        self.int_sub_code = (70, 71)
        self.term_point = (71, 76)
        self.term_region = (76, 78)
        self.term_sec_code = (78, 79)
        self.term_sub_code = (79, 80)
        self.min_alt = (80, 85)
        self.max_alt = (85, 90)
        self.time_zone = (90, 91)
        self.aircraft_use = (91, 93)
        self.direction = (93, 94)
        self.alt_desc = (94, 95)
        self.alt_1 = (95, 100)
        self.alt_2 = (100, 105)
        # RESERVED 18


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.notes = (40, 109)
        # RESERVED 14


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.time_zone = (40, 41)
        self.daylight_ind = (41, 42)
        self.op_time_1 = (42, 52)
        self.op_time_2 = (52, 62)
        self.op_time_3 = (62, 72)
        self.op_time_4 = (72, 82)
        self.op_time_5 = (82, 92)
        self.op_time_6 = (92, 102)
        self.op_time_7 = (102, 112)
        # RESERVED 11


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_tim = TimeIndices()
