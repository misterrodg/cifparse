from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        # PAD 1
        self.airport_id = (6, 10, field_56)
        self.airport_region = (10, 12, field_514)
        self.sub_code = (12, 13, field_55)
        self.procedure_id = (13, 19, field_59)
        self.procedure_type = (19, 20, field_57)
        self.runway_transition_id = (20, 25, field_511)
        self.runway_transition_point = (25, 30, field_513)
        self.runway_transition_region = (30, 32, field_514)
        self.runway_transition_sec_code = (32, 33, field_54)
        self.runway_transition_sub_code = (33, 34, field_55)
        self.runway_transition_atd = (34, 37, field_5231)
        self.common_point = (37, 42, field_513)
        self.common_point_region = (42, 44, field_514)
        self.common_point_sec_code = (44, 45, field_54)
        self.common_point_sub_code = (45, 46, field_55)
        self.common_point_atd = (46, 49, field_5231)
        self.enroute_transition_id = (49, 54, field_511)
        self.enroute_transition_point = (54, 59, field_513)
        self.enroute_transition_region = (59, 61, field_514)
        self.enroute_transition_sec_code = (61, 62, field_54)
        self.enroute_transition_sub_code = (62, 63, field_55)
        self.enroute_transition_atd = (63, 66, field_5231)
        self.seq_no = (66, 69, field_512)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (69, 70, field_516)
        self.noe = (70, 74, field_5232)
        self.turbo = (74, 75, field_5233)
        self.rnav = (75, 76, field_5234)
        self.atc_wc = (76, 77, field_5235)
        self.atc_id = (77, 84, field_5236)
        self.time_zone = (84, 85, field_5131)
        self.description = (85, 100, field_5237)
        self.ltc = (100, 102, field_5238)
        self.rpt = (102, 103, field_5239)
        self.out_mag_crs = (103, 107, field_526)
        self.alt_desc = (107, 108, field_529)
        self.alt_1 = (108, 111, field_5240)
        self.alt_2 = (111, 114, field_5240)
        self.speed_limit = (114, 117, field_572)
        self.cruise_id = (117, 119, field_5134)
        self.speed_desc = (119, 120, field_5261)
        # PAD 3


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (69, 70, field_516)
        self.application = (70, 71, field_591)
        self.intermediate_id_1 = (71, 76, field_513)
        self.intermediate_region_1 = (76, 78, field_514)
        self.intermediate_sec_code_1 = (78, 79, field_54)
        self.intermediate_sub_code_1 = (79, 80, field_55)
        self.intermediate_atd_1 = (80, 83, field_5231)
        self.frt_code_1 = (83, 84, field_5241)
        self.intermediate_id_2 = (84, 89, field_513)
        self.intermediate_region_2 = (89, 91, field_514)
        self.intermediate_sec_code_2 = (91, 92, field_54)
        self.intermediate_sub_code_2 = (92, 93, field_55)
        self.intermediate_atd_2 = (93, 96, field_5231)
        self.frt_code_2 = (96, 97, field_5241)
        self.intermediate_id_3 = (97, 102, field_513)
        self.intermediate_region_3 = (102, 104, field_514)
        self.intermediate_sec_code_3 = (104, 105, field_54)
        self.intermediate_sub_code_3 = (105, 106, field_55)
        self.intermediate_atd_3 = (106, 109, field_5231)
        self.frt_code_3 = (109, 110, field_5241)
        self.intermediate_id_4 = (110, 115, field_513)
        self.intermediate_region_4 = (115, 117, field_514)
        self.intermediate_sec_code_4 = (117, 118, field_54)
        self.intermediate_sub_code_4 = (118, 119, field_55)
        self.intermediate_atd_4 = (119, 122, field_5231)
        self.frt_code_4 = (122, 123, field_5241)


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (69, 70, field_516)
        self.application = (70, 71, field_591)
        self.time_zone = (71, 72, field_5131)
        self.daylight_ind = (72, 73, field_5138)
        self.op_time_1 = (73, 83, field_5195)
        self.op_time_2 = (83, 93, field_5195)
        self.op_time_3 = (93, 103, field_5195)
        self.op_time_4 = (103, 113, field_5195)
        self.op_time_5 = (113, 123, field_5195)


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_tim = TimeIndices()
