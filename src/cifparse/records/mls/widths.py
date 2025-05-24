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
        self.mls_id = (13, 17, field_544)
        self.cat = (17, 18, field_580)
        # PAD 3
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.channel = (22, 25, field_5166)
        # PAD 2
        self.runway_id = (27, 32, field_546)
        self.mls_lat = (32, 41, field_536)
        self.mls_lon = (41, 51, field_537)
        self.mls_bearing = (51, 55, field_5167)
        self.el_lat = (55, 64, field_536)
        self.el_lon = (64, 74, field_537)
        self.mls_dist = (74, 78, field_548)
        # Doc shows 5167, but that is bearing. LOC uses 548 for similar.
        self.plus_minus = (78, 79, field_549)
        self.el_thr_dist = (79, 83, field_550)
        self.pro_right = (83, 86, field_5168)
        self.pro_left = (86, 89, field_5168)
        self.cov_right = (89, 92, field_5172)
        self.cov_left = (92, 95, field_5172)
        self.el_angle = (95, 98, field_5169)
        self.mag_var = (98, 103, field_539)
        self.el_elevation = (103, 108, field_574)
        self.nom_el_angle = (108, 112, field_5173)
        self.min_el_angle = (112, 115, field_552)
        self.support_fac = (115, 119, field_533)
        self.support_region = (119, 121, field_514)
        self.support_sec_code = (121, 122, field_54)
        self.support_sub_code = (122, 123, field_55)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        # PAD 4
        self.fac_char = (27, 32, field_593)
        self.baz_lat = (32, 41, field_536)
        self.baz_lon = (41, 51, field_537)
        self.baz_mag_bearing = (51, 55, field_5167)
        self.dp_lat = (55, 64, field_536)
        self.dp_lon = (64, 74, field_537)
        self.baz_dist = (74, 78, field_548)
        # Doc shows 5167, but that is bearing. LOC uses 548 for similar.
        self.plus_minus = (78, 79, field_549)
        # PAD 4
        self.pro_right = (83, 86, field_5168)
        self.pro_left = (86, 89, field_5168)
        self.cov_right = (89, 92, field_5172)
        self.cov_left = (92, 95, field_5172)
        self.baz_true_bearing = (95, 100, field_594)
        self.baz_source = (100, 101, field_595)
        self.az_true_bearing = (101, 106, field_594)
        self.az_source = (106, 107, field_595)
        self.tch = (107, 109, field_567)
        # RESERVED 14


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
