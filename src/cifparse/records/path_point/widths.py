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
        self.approach_id = (13, 19, field_510)
        self.surface_id = (19, 24, field_546)
        self.ops_type = (24, 26, field_5223)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (26, 27, field_516)
        self.route_ind = (27, 28, field_5224)
        self.sbas_spi = (28, 30, field_5255)
        self.ref_path_data_sel = (30, 32, field_5256)
        self.ref_path_data_id = (32, 36, field_5257)
        self.app_pd = (36, 37, field_5258)
        self.ltp_lat = (37, 48, field_5267)
        self.ltp_lon = (48, 60, field_5268)
        self.ltp_ellipsoid_height = (60, 66, field_5225)
        self.gpa = (66, 70, field_5226)
        self.fpap_lat = (70, 81, field_5267)
        self.fpap_lon = (81, 93, field_5268)
        self.course_width = (93, 98, field_5228)
        self.length_offset = (98, 102, field_5259)
        self.path_point_tch = (102, 108, field_5265)
        self.tch_ind = (108, 109, field_5266)
        self.hal = (109, 112, field_5263)
        self.val = (112, 115, field_5264)
        self.crc = (115, 123, field_5229)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (26, 27, field_516)
        self.application = (27, 28, field_591)
        self.fpap_ell_hgt = (28, 34, field_5225)
        self.fpap_ort_hgt = (34, 40, field_5227)
        self.ltp_ort_hgt = (40, 46, field_5227)
        self.app_type_id = (46, 56, field_5262)
        self.gnss_ch_no = (56, 61, field_5244)
        # PAD 10
        self.hpc = (71, 74, field_5269)
        # RESERVED 49


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
