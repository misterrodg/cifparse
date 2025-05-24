from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.route_id = (6, 11, field_58)
        self.six_char = (11, 12, field_58)
        self.rest_id = (12, 15, field_5154)
        self.rest_type = (15, 17, field_5201)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class AltExcPrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18, field_516)
        self.start_point_id = (18, 23, field_513)
        self.start_point_region = (23, 25, field_514)
        self.start_point_sec_code = (25, 26, field_54)
        self.start_point_sub_code = (26, 27, field_55)
        self.end_point_id = (27, 32, field_513)
        self.end_point_region = (32, 34, field_514)
        self.end_point_sec_code = (34, 35, field_54)
        self.end_point_sub_code = (35, 36, field_55)
        # PAD 1
        self.start_date = (37, 44, field_5157)
        self.end_date = (44, 51, field_5157)
        self.time_zone = (51, 52, field_5131)
        self.daylight_ind = (52, 53, field_5138)
        self.op_time_1 = (53, 63, field_5195)
        self.op_time_2 = (63, 73, field_5195)
        self.op_time_3 = (73, 83, field_5195)
        self.op_time_4 = (83, 93, field_5195)
        self.exc_ind = (93, 94, field_5202)
        self.alt_desc = (94, 95, field_5160)
        self.rest_alt_1 = (95, 98, field_5161)
        self.blk_id_1 = (98, 99, field_5203)
        self.rest_alt_2 = (99, 102, field_5161)
        self.blk_id_2 = (102, 103, field_5203)
        self.rest_alt_3 = (103, 106, field_5161)
        self.blk_id_3 = (106, 107, field_5203)
        self.rest_alt_4 = (107, 110, field_5161)
        self.blk_id_4 = (110, 111, field_5203)
        self.rest_alt_5 = (111, 114, field_5161)
        self.blk_id_5 = (114, 115, field_5203)
        self.rest_alt_6 = (115, 118, field_5161)
        self.blk_id_6 = (118, 119, field_5203)
        self.rest_alt_7 = (119, 122, field_5161)
        self.blk_id_7 = (122, 123, field_5203)


class AltExcContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18, field_516)
        self.application = (18, 19, field_591)
        # RESERVED 32
        self.time_zone = (51, 52, field_5131)
        self.daylight_ind = (52, 53, field_5138)
        self.op_time_1 = (53, 63, field_5195)
        self.op_time_2 = (63, 73, field_5195)
        self.op_time_3 = (73, 83, field_5195)
        self.op_time_4 = (83, 93, field_5195)
        self.exc_ind = (93, 94, field_5202)
        self.alt_desc = (94, 95, field_5160)
        self.rest_alt_1 = (95, 98, field_5161)
        self.blk_id_1 = (98, 99, field_5203)
        self.rest_alt_2 = (99, 102, field_5161)
        self.blk_id_2 = (102, 103, field_5203)
        self.rest_alt_3 = (103, 106, field_5161)
        self.blk_id_3 = (106, 107, field_5203)
        self.rest_alt_4 = (107, 110, field_5161)
        self.blk_id_4 = (110, 111, field_5203)
        self.rest_alt_5 = (111, 114, field_5161)
        self.blk_id_5 = (114, 115, field_5203)
        self.rest_alt_6 = (115, 118, field_5161)
        self.blk_id_6 = (118, 119, field_5203)
        self.rest_alt_7 = (119, 122, field_5161)
        self.blk_id_7 = (122, 123, field_5203)


class CruisePrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18, field_516)
        self.start_point_id = (18, 23, field_513)
        self.start_point_region = (23, 25, field_514)
        self.start_point_sec_code = (25, 26, field_54)
        self.start_point_sub_code = (26, 27, field_55)
        self.end_point_id = (27, 32, field_513)
        self.end_point_region = (32, 34, field_514)
        self.end_point_sec_code = (34, 35, field_54)
        self.end_point_sub_code = (35, 36, field_55)
        # PAD 1
        self.start_date = (37, 44, field_5157)
        self.end_date = (44, 51, field_5157)
        self.time_zone = (51, 52, field_5131)
        self.daylight_ind = (52, 53, field_5138)
        self.op_time_1 = (53, 63, field_5195)
        self.op_time_2 = (63, 73, field_5195)
        self.op_time_3 = (73, 83, field_5195)
        self.op_time_4 = (83, 93, field_5195)
        self.cruise_id = (93, 95, field_5134)
        # PAD 28


class CruiseContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18, field_516)
        self.application = (18, 19, field_591)
        # RESERVED 32
        self.time_zone = (51, 52, field_5131)
        self.daylight_ind = (52, 53, field_5138)
        self.op_time_1 = (53, 63, field_5195)
        self.op_time_2 = (63, 73, field_5195)
        self.op_time_3 = (73, 83, field_5195)
        self.op_time_4 = (83, 93, field_5195)
        self.cruise_id = (93, 95, field_5134)
        # PAD 28


class ClosurePrimaryIndices(CruisePrimaryIndices):
    def __init__(self):
        super().__init__()


class NotePrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18, field_516)
        self.start_point_id = (18, 23, field_513)
        self.start_point_region = (23, 25, field_514)
        self.start_point_sec_code = (25, 26, field_54)
        self.start_point_sub_code = (26, 27, field_55)
        self.end_point_id = (27, 32, field_513)
        self.end_point_region = (32, 34, field_514)
        self.end_point_sec_code = (34, 35, field_54)
        self.end_point_sub_code = (35, 36, field_55)
        # PAD 1
        self.start_date = (37, 44, field_5157)
        self.end_date = (44, 51, field_5157)
        self.notes = (51, 120, field_5163)
        # PAD 3


class NoteContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18, field_516)
        self.application = (18, 19, field_591)
        # RESERVED 32
        self.notes = (37, 44, field_5163)
        # PAD 3


w_bas = BaseIndices()
w_aex = AltExcPrimaryIndices()
w_aec = AltExcContinuationIndices()
w_cru = CruisePrimaryIndices()
w_crc = CruiseContinuationIndices()
w_clo = ClosurePrimaryIndices()
w_not = NotePrimaryIndices()
w_noc = NoteContinuationIndices()
