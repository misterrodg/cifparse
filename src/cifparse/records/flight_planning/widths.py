class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        self.sub_code = (12, 13)
        self.procedure_id = (13, 19)
        self.procedure_type = (19, 20)
        self.runway_transition_id = (20, 25)
        self.runway_transition_point = (25, 30)
        self.runway_transition_region = (30, 32)
        self.runway_transition_sec_code = (32, 33)
        self.runway_transition_sub_code = (33, 34)
        self.runway_transition_atd = (34, 37)
        self.common_point = (37, 42)
        self.common_point_region = (42, 44)
        self.common_point_sec_code = (44, 45)
        self.common_point_sub_code = (45, 46)
        self.common_point_atd = (46, 49)
        self.enroute_transition_id = (49, 54)
        self.enroute_transition_point = (54, 59)
        self.enroute_transition_region = (59, 61)
        self.enroute_transition_sec_code = (61, 62)
        self.enroute_transition_sub_code = (62, 63)
        self.enroute_transition_atd = (63, 66)
        self.seq_no = (66, 69)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (69, 70)
        self.noe = (70, 74)
        self.turbo = (74, 75)
        self.rnav = (75, 76)
        self.atc_wc = (76, 77)
        self.atc_id = (77, 84)
        self.time_zone = (84, 85)
        self.description = (85, 100)
        self.ltc = (100, 102)
        self.rpt = (102, 103)
        self.out_mag_crs = (103, 107)
        self.alt_desc = (107, 108)
        self.alt_1 = (108, 111)
        self.alt_2 = (111, 114)
        self.limit_speed = (114, 117)
        self.cruise_id = (117, 119)
        self.speed_desc = (119, 120)
        # PAD 3


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (69, 70)
        self.application = (70, 71)
        self.intermediate_id_1 = (71, 76)
        self.intermediate_region_1 = (76, 78)
        self.intermediate_sec_code_1 = (78, 79)
        self.intermediate_sub_code_1 = (79, 80)
        self.intermediate_atd_1 = (80, 83)
        self.frt_code_1 = (83, 84)
        self.intermediate_id_2 = (84, 89)
        self.intermediate_region_2 = (89, 91)
        self.intermediate_sec_code_2 = (91, 92)
        self.intermediate_sub_code_2 = (92, 93)
        self.intermediate_atd_2 = (93, 96)
        self.frt_code_2 = (96, 97)
        self.intermediate_id_3 = (97, 102)
        self.intermediate_region_3 = (102, 104)
        self.intermediate_sec_code_3 = (104, 105)
        self.intermediate_sub_code_3 = (105, 106)
        self.intermediate_atd_3 = (106, 109)
        self.frt_code_3 = (109, 110)
        self.intermediate_id_4 = (110, 115)
        self.intermediate_region_4 = (115, 117)
        self.intermediate_sec_code_4 = (117, 118)
        self.intermediate_sub_code_4 = (118, 119)
        self.intermediate_atd_4 = (119, 122)
        self.frt_code_4 = (122, 123)


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (69, 70)
        self.application = (70, 71)
        self.time_zone = (71, 72)
        self.daylight_ind = (72, 73)
        self.op_time_1 = (73, 83)
        self.op_time_2 = (83, 93)
        self.op_time_3 = (93, 103)
        self.op_time_4 = (103, 113)
        self.op_time_5 = (113, 123)


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_tim = TimeIndices()
