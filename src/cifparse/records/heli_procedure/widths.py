from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        # PAD 1
        self.fac_id = (6, 10, field_56)
        self.fac_region = (10, 12, field_514)
        self.fac_sub_code = (12, 13, field_55)
        self.procedure_id = (13, 19, field_59)
        self.procedure_type = (19, 20, field_57)
        self.transition_id = (20, 25, field_511)
        # PAD 1
        self.seq_no = (26, 29, field_512)
        self.fix_id = (29, 34, field_513)
        self.fix_region = (34, 36, field_514)
        self.fix_sec_code = (36, 37, field_54)
        self.fix_sub_code = (37, 38, field_55)
        #
        # OTHER
        # FIELDS
        #
        # PAD 3
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.desc_code = (39, 43, field_517)
        self.turn_direction = (43, 44, field_520)
        self.rnp = (44, 47, field_5211)
        self.path_term = (47, 49, field_521)
        self.tdv = (49, 50, field_522)
        self.rec_vhf = (50, 54, field_523)
        self.rec_vhf_region = (54, 56, field_514)
        self.arc_radius = (56, 62, field_5204)
        self.theta = (62, 66, field_524)
        self.rho = (66, 70, field_525)
        self.course = (70, 74, field_526)
        self.dist_time = (74, 78, field_527)
        self.rec_vhf_sec_code = (78, 79, field_54)
        self.rec_vhf_sub_code = (79, 80, field_55)
        # RESERVED 2
        self.alt_desc = (82, 83, field_529)
        self.atc = (83, 84, field_581)
        self.alt_1 = (84, 89, field_530)
        self.alt_2 = (89, 94, field_530)
        self.trans_alt = (94, 99, field_553)
        self.speed_limit = (99, 102, field_572)
        self.vertical_angle = (102, 106, field_570)
        self.center_fix = (106, 111, field_5144)
        self.multiple_code = (111, 112, field_5130)
        self.center_fix_region = (112, 114, field_514)
        self.center_fix_sec_code = (114, 115, field_54)
        self.center_fix_sub_code = (115, 116, field_55)
        self.gns_fms_id = (116, 117, field_5222)
        self.speed_desc = (117, 118, field_5261)
        self.rte_qual_1 = (118, 119, field_57)
        self.rte_qual_2 = (119, 120, field_57)
        # PAD 3


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.dh_cat_a = (40, 44, field_5170)
        self.dh_cat_b = (44, 48, field_5170)
        self.dh_cat_c = (48, 52, field_5170)
        self.dh_cat_d = (52, 56, field_5170)
        self.mda_cat_a = (56, 60, field_5171)
        self.mda_cat_b = (60, 64, field_5171)
        self.mda_cat_c = (64, 68, field_5171)
        self.mda_cat_d = (68, 72, field_5171)
        self.tch = (72, 75, field_567)
        self.alt_desc = (75, 76, field_529)
        self.loc_alt = (76, 81, field_530)
        self.vert_angle = (81, 85, field_570)
        # PAD 4
        self.rnp = (89, 92, field_5211)
        # RESERVED 26
        self.rte_qual_1 = (118, 119, field_57)
        self.rte_qual_2 = (119, 120, field_57)
        # PAD 3


class SimulationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.fas_block = (40, 41, field_5276)
        self.fas_service = (41, 51, field_5275)
        self.l_vnav_block = (51, 52, field_5276)
        self.l_vnav_service = (52, 62, field_5275)
        self.lnav_block = (62, 63, field_5276)
        self.lnav_service = (63, 73, field_5275)
        # RESERVED 45
        self.app_rte_type_1 = (118, 119, field_57)
        self.app_rte_type_2 = (119, 120, field_57)
        # PAD 3


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (38, 39, field_516)
        self.application = (39, 40, field_591)
        self.se_ind = (40, 41, field_5152)
        self.se_date = (41, 52, field_5153)
        # PAD 22
        self.leg_dist = (74, 78, field_527)
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
