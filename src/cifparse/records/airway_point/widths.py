class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        # PAD 7
        self.airway_id = (13, 18)
        self.six_char = (18, 19)
        # PAD 6
        self.seq_no = (25, 29)
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
        self.desc_code = (39, 43)
        self.bound_code = (43, 44)
        self.route_type = (44, 45)
        self.level = (45, 46)
        self.direct = (46, 47)
        self.tc_ind = (47, 49)
        self.eu_ind = (49, 50)
        self.rec_vhf = (50, 54)
        self.rec_vhf_region = (54, 56)
        self.rnp = (56, 59)
        # PAD 3
        self.theta = (62, 66)
        self.rho = (66, 70)
        self.out_mag_crs = (70, 74)
        self.from_dist = (74, 78)
        self.in_mag_crs = (78, 82)
        # PAD 1
        self.min_alt_1 = (83, 88)
        self.min_alt_2 = (88, 93)
        self.max_alt = (93, 98)
        self.fix_radius = (98, 102)
        # RESERVED 21


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.notes = (40, 109)
        # RESERVED 14


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.se_ind = (40, 41)
        self.se_date = (41, 52)
        # PAD 14
        self.rest_1_region = (66, 68)
        self.rest_1_type = (68, 69)
        self.rest_1_designation = (69, 79)
        self.rest_1_mult_code = (79, 80)
        self.rest_2_region = (80, 82)
        self.rest_2_type = (82, 83)
        self.rest_2_designation = (83, 93)
        self.rest_2_mult_code = (93, 94)
        self.rest_3_region = (94, 96)
        self.rest_3_type = (96, 97)
        self.rest_3_designation = (97, 107)
        self.rest_3_mult_code = (107, 108)
        self.rest_4_region = (108, 110)
        self.rest_4_type = (110, 111)
        self.rest_4_designation = (111, 121)
        self.rest_4_mult_code = (121, 122)
        self.linked_record = (122, 123)


class PlanningContinuationIndices(PrimaryIndices):
    def __init__(self):
        super().__init__()


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_pla = PlanningIndices()
w_plc = PlanningContinuationIndices()
