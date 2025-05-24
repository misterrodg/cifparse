from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        # PAD 7
        self.airway_id = (13, 18, field_58)
        self.six_char = (18, 19, field_58)
        # PAD 6
        self.seq_no = (25, 29, field_512)
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
        self.desc_code = (39, 43, field_517)
        self.bound_code = (43, 44, field_518)
        self.route_type = (44, 45, field_57)
        self.level = (45, 46, field_519)
        self.direct = (46, 47, field_5115)
        self.cruise_id = (47, 49, field_5134)
        self.eu_ind = (49, 50, field_5164)
        self.rec_vhf = (50, 54, field_523)
        self.rec_vhf_region = (54, 56, field_514)
        self.rnp = (56, 59, field_5211)
        # PAD 3
        self.theta = (62, 66, field_524)
        self.rho = (66, 70, field_525)
        self.out_mag_crs = (70, 74, field_526)
        self.from_dist = (74, 78, field_527)
        self.in_mag_crs = (78, 82, field_528)
        # PAD 1
        self.min_alt_1 = (83, 88, field_530)
        self.min_alt_2 = (88, 93, field_530)
        self.max_alt = (93, 98, field_5127)
        self.fix_radius = (98, 102, field_5254)
        # RESERVED 21


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.notes = (40, 109, field_561)
        # RESERVED 14


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.se_ind = (40, 41, field_5152)
        self.se_date = (41, 52, field_5153)
        # PAD 14
        self.rest_1_region = (66, 68, field_514)
        self.rest_1_type = (68, 69, field_5128)
        self.rest_1_designation = (69, 79, field_5129)
        self.rest_1_mult_code = (79, 80, field_5130)
        self.rest_2_region = (80, 82, field_514)
        self.rest_2_type = (82, 83, field_5128)
        self.rest_2_designation = (83, 93, field_5129)
        self.rest_2_mult_code = (93, 94, field_5130)
        self.rest_3_region = (94, 96, field_514)
        self.rest_3_type = (96, 97, field_5128)
        self.rest_3_designation = (97, 107, field_5129)
        self.rest_3_mult_code = (107, 108, field_5130)
        self.rest_4_region = (108, 110, field_514)
        self.rest_4_type = (110, 111, field_5128)
        self.rest_4_designation = (111, 121, field_5129)
        self.rest_4_mult_code = (121, 122, field_5130)
        self.linked_record = (122, 123, field_5174)


class PlanningContinuationIndices(PrimaryIndices):
    def __init__(self):
        super().__init__()


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_pla = PlanningIndices()
w_plc = PlanningContinuationIndices()
