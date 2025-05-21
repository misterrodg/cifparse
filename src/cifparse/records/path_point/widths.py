class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        self.sub_code = (12, 13)
        self.approach_id = (13, 19)
        self.surface_id = (19, 24)
        self.ops_type = (24, 26)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (26, 27)
        self.route_ind = (27, 28)
        self.sbas_spi = (28, 30)
        self.ref_path_data_sel = (30, 32)
        self.ref_path_data_id = (32, 36)
        self.app_pd = (36, 37)
        self.ltp_lat = (37, 48)
        self.ltp_lon = (48, 60)
        self.ltp_ellipsoid_height = (60, 66)
        self.gpa = (66, 70)
        self.fpap_lat = (70, 81)
        self.fpap_lon = (81, 93)
        self.course_width = (93, 98)
        self.length_offset = (98, 102)
        self.path_point_tch = (102, 108)
        self.tch_ind = (108, 109)
        self.hal = (109, 112)
        self.val = (112, 115)
        self.crc = (115, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (26, 27)
        self.application = (27, 28)
        self.fpap_ell_hgt = (28, 34)
        self.fpap_ort_hgt = (34, 40)
        self.ltp_ort_hgt = (40, 46)
        self.app_type_id = (46, 56)
        self.gnss_ch_no = (56, 61)
        # PAD 10
        self.hpc = (71, 74)
        # RESERVED 49


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
