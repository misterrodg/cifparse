class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        self.sub_code = (12, 13)
        self.mls_id = (13, 17)
        self.cat = (17, 18)
        # PAD 3
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.channel = (22, 25)
        # PAD 2
        self.runway_id = (27, 32)
        self.mls_lat = (32, 41)
        self.mls_lon = (41, 51)
        self.mls_bearing = (51, 55)
        self.el_lat = (55, 64)
        self.el_lon = (64, 74)
        self.mls_dist = (74, 78)
        self.plus_minus = (78, 79)
        self.el_thr_dist = (79, 83)
        self.pro_right = (83, 86)
        self.pro_left = (86, 89)
        self.cov_right = (89, 92)
        self.cov_left = (92, 95)
        self.el_angle = (95, 98)
        self.mag_var = (98, 103)
        self.el_elevation = (103, 108)
        self.nom_el_angle = (108, 112)
        self.min_el_angle = (112, 115)
        self.support_fac = (115, 119)
        self.support_region = (119, 121)
        self.support_sec_code = (121, 122)
        self.support_sub_code = (122, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        # PAD 4
        self.fac_char = (27, 32)
        self.baz_lat = (32, 41)
        self.baz_lon = (41, 51)
        self.baz_mag_bearing = (51, 55)
        self.dp_lat = (55, 64)
        self.dp_lon = (64, 74)
        self.baz_dist = (74, 78)
        self.plus_minus = (78, 79)
        # PAD 4
        self.pro_right = (83, 86)
        self.pro_left = (86, 89)
        self.cov_right = (89, 92)
        self.cov_left = (92, 95)
        self.baz_true_bearing = (95, 100)
        self.baz_source = (100, 101)
        self.az_true_bearing = (101, 106)
        self.az_source = (106, 107)
        self.tch = (107, 109)
        # RESERVED 14


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
