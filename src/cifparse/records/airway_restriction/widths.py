class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.route_id = (6, 11)
        self.six_char = (11, 12)
        self.rest_id = (12, 15)
        self.rest_type = (15, 17)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class AltExcPrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18)
        self.start_point_id = (18, 23)
        self.start_point_region = (23, 25)
        self.start_point_sec_code = (25, 26)
        self.start_point_sub_code = (26, 27)
        self.end_point_id = (27, 32)
        self.end_point_region = (32, 34)
        self.end_point_sec_code = (34, 35)
        self.end_point_sub_code = (35, 36)
        # PAD 1
        self.start_date = (37, 44)
        self.end_date = (44, 51)
        self.time_zone = (51, 52)
        self.daylight_ind = (52, 53)
        self.op_time_1 = (53, 63)
        self.op_time_2 = (63, 73)
        self.op_time_3 = (73, 83)
        self.op_time_4 = (83, 93)
        self.exc_ind = (93, 94)
        self.alt_desc = (94, 95)
        self.rest_alt_1 = (95, 98)
        self.blk_id_1 = (98, 99)
        self.rest_alt_2 = (99, 102)
        self.blk_id_2 = (102, 103)
        self.rest_alt_3 = (103, 106)
        self.blk_id_3 = (106, 107)
        self.rest_alt_4 = (107, 110)
        self.blk_id_4 = (110, 111)
        self.rest_alt_5 = (111, 114)
        self.blk_id_5 = (114, 115)
        self.rest_alt_6 = (115, 118)
        self.blk_id_6 = (118, 119)
        self.rest_alt_7 = (119, 122)
        self.blk_id_7 = (122, 123)


class AltExcContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18)
        self.application = (18, 19)
        # RESERVED 32
        self.time_zone = (51, 52)
        self.daylight_ind = (52, 53)
        self.op_time_1 = (53, 63)
        self.op_time_2 = (63, 73)
        self.op_time_3 = (73, 83)
        self.op_time_4 = (83, 93)
        self.exc_ind = (93, 94)
        self.alt_desc = (94, 95)
        self.rest_alt_1 = (95, 98)
        self.blk_id_1 = (98, 99)
        self.rest_alt_2 = (99, 102)
        self.blk_id_2 = (102, 103)
        self.rest_alt_3 = (103, 106)
        self.blk_id_3 = (106, 107)
        self.rest_alt_4 = (107, 110)
        self.blk_id_4 = (110, 111)
        self.rest_alt_5 = (111, 114)
        self.blk_id_5 = (114, 115)
        self.rest_alt_6 = (115, 118)
        self.blk_id_6 = (118, 119)
        self.rest_alt_7 = (119, 122)
        self.blk_id_7 = (122, 123)


class CruisePrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18)
        self.start_point_id = (18, 23)
        self.start_point_region = (23, 25)
        self.start_point_sec_code = (25, 26)
        self.start_point_sub_code = (26, 27)
        self.end_point_id = (27, 32)
        self.end_point_region = (32, 34)
        self.end_point_sec_code = (34, 35)
        self.end_point_sub_code = (35, 36)
        # PAD 1
        self.start_date = (37, 44)
        self.end_date = (44, 51)
        self.time_zone = (51, 52)
        self.daylight_ind = (52, 53)
        self.op_time_1 = (53, 63)
        self.op_time_2 = (63, 73)
        self.op_time_3 = (73, 83)
        self.op_time_4 = (83, 93)
        self.cruise_id = (93, 95)
        # PAD 28


class CruiseContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18)
        self.application = (18, 19)
        # RESERVED 32
        self.time_zone = (51, 52)
        self.daylight_ind = (52, 53)
        self.op_time_1 = (53, 63)
        self.op_time_2 = (63, 73)
        self.op_time_3 = (73, 83)
        self.op_time_4 = (83, 93)
        self.cruise_id = (93, 95)
        # PAD 28


class ClosurePrimaryIndices(CruisePrimaryIndices):
    def __init__(self):
        super().__init__()


class NotePrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18)
        self.start_point_id = (18, 23)
        self.start_point_region = (23, 25)
        self.start_point_sec_code = (25, 26)
        self.start_point_sub_code = (26, 27)
        self.end_point_id = (27, 32)
        self.end_point_region = (32, 34)
        self.end_point_sec_code = (34, 35)
        self.end_point_sub_code = (35, 36)
        # PAD 1
        self.start_date = (37, 44)
        self.end_date = (44, 51)
        self.notes = (51, 120)
        # PAD 3


class NoteContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (17, 18)
        self.application = (18, 19)
        # RESERVED 32
        self.notes = (37, 44)
        # PAD 3


w_bas = BaseIndices()
w_aex = AltExcPrimaryIndices()
w_aec = AltExcContinuationIndices()
w_cru = CruisePrimaryIndices()
w_crc = CruiseContinuationIndices()
w_clo = ClosurePrimaryIndices()
w_not = NotePrimaryIndices()
w_noc = NoteContinuationIndices()
