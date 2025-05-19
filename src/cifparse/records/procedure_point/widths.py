class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.fac_id = (6, 10)
        self.fac_region = (10, 12)
        self.fac_sub_code = (12, 13)
        self.procedure_id = (13, 19)
        self.route_type = (19, 20)
        self.transition_id = (20, 25)
        # PAD 1
        self.seq_no = (26, 29)
        self.fix_id = (29, 34)
        self.fix_region = (34, 36)
        self.fix_sec_code = (36, 37)
        self.fix_sub_code = (37, 38)
        #
        # OTHER
        # FIELDS
        #
        # PAD 3
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.desc_code = (39, 43)
        self.turn_direction = (43, 44)
        self.rnp = (44, 47)
        self.path_term = (47, 49)
        self.tdv = (49, 50)
        self.rec_vhf = (50, 54)
        self.rec_vhf_region = (54, 56)
        self.arc_radius = (56, 62)
        self.theta = (62, 66)
        self.rho = (66, 70)
        self.course = (70, 74)
        self.dist_time = (74, 78)
        self.rec_vhf_sec_code = (78, 79)
        self.rec_vhf_sub_code = (79, 80)
        # RESERVED 2
        self.alt_desc = (82, 83)
        self.atc = (83, 84)
        self.alt_1 = (84, 89)
        self.alt_2 = (89, 94)
        self.trans_alt = (94, 99)
        self.speed_limit_1 = (99, 102)
        self.vert_angle = (102, 106)
        self.center_fix = (106, 111)
        self.mult_code = (111, 112)
        self.center_fix_region = (112, 114)
        self.center_fix_sec_code = (114, 115)
        self.center_fix_sub_code = (115, 116)
        self.gns_fms_id = (116, 117)
        self.speed_limit_2 = (117, 118)
        self.rte_qual_1 = (118, 119)
        self.rte_qual_2 = (119, 120)
        # PAD 3


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.dh_cat_a = (40, 44)
        self.dh_cat_b = (44, 48)
        self.dh_cat_c = (48, 52)
        self.dh_cat_d = (52, 56)
        self.mda_cat_a = (56, 60)
        self.mda_cat_b = (60, 64)
        self.mda_cat_c = (64, 68)
        self.mda_cat_d = (68, 72)
        self.tch = (72, 75)
        self.alt_desc = (75, 76)
        self.loc_alt = (76, 81)
        self.vert_angle = (81, 85)
        # PAD 4
        self.rnp = (89, 92)
        # RESERVED 26
        self.rte_qual_1 = (118, 119)
        self.rte_qual_2 = (119, 120)
        # PAD 3


class SimulationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.fas_block = (40, 41)
        self.fas_service = (41, 51)
        self.l_vnav_block = (51, 52)
        self.l_vnav_service = (52, 62)
        self.lnav_block = (62, 63)
        self.lnav_service = (63, 73)
        # RESERVED 45
        self.app_rte_type_1 = (118, 119)
        self.app_rte_type_2 = (119, 120)
        # PAD 3


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39)
        self.application = (39, 40)
        self.se_ind = (40, 41)
        self.se_date = (41, 52)
        # PAD 22
        self.leg_dist = (74, 78)
        # RESERVED 45


class PlanningContinuationIndices(PrimaryIndices):
    def __init__(self):
        super().__init__()


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_pla = PlanningIndices()
w_plc = PlanningContinuationIndices()
w_sim = SimulationIndices()
