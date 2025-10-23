from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.center_region = (6, 8, field_514)
        self.airspace_type = (8, 9, field_5213)
        self.center_id = (9, 14, field_5214)
        self.center_sec_code = (14, 15, field_54)
        self.center_sub_code = (15, 16, field_55)
        self.airspace_class = (16, 17, field_5215)
        # PAD 2
        self.mult_code = (19, 20, field_5130)
        self.seq_no = (20, 24, field_512)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (24, 25, field_516)
        self.level = (25, 26, field_519)
        self.time_zone = (26, 27, field_5131)
        self.notam = (27, 28, field_5132)
        # PAD 2
        self.boundary_via = (30, 32, field_5118)
        self.lat = (32, 41, field_536)
        self.lon = (41, 51, field_537)
        self.arc_lat = (51, 60, field_536)
        self.arc_lon = (60, 70, field_537)
        self.arc_dist = (70, 74, field_5119)
        self.arc_bearing = (74, 78, field_5120)
        self.rnp = (78, 81, field_5211)
        self.lower_limit = (81, 86, field_5121)
        self.lower_unit = (86, 87, field_5133)
        self.upper_limit = (87, 92, field_5121)
        self.upper_unit = (92, 93, field_5133)
        self.airspace_name = (93, 123, field_5216)


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (24, 25, field_516)
        self.application = (25, 26, field_591)
        self.time_zone = (26, 27, field_5131)
        self.notam = (27, 28, field_5132)
        self.daylight_ind = (28, 29, field_5138)
        self.op_time_1 = (29, 39, field_5195)
        self.op_time_2 = (39, 49, field_5195)
        self.op_time_3 = (49, 59, field_5195)
        self.op_time_4 = (59, 69, field_5195)
        self.op_time_5 = (69, 79, field_5195)
        self.op_time_6 = (79, 89, field_5195)
        self.op_time_7 = (89, 99, field_5195)
        self.controlling_agency = (99, 123, field_5140)


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_tim = TimeIndices()
