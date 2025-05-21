class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.center_region = (6, 8)
        self.airspace_type = (8, 9)
        self.center_id = (9, 14)
        self.center_sec_code = (14, 15)
        self.center_sub_code = (15, 16)
        self.airspace_class = (16, 17)
        # PAD 2
        self.mult_code = (19, 20)
        self.seq_no = (20, 24)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (24, 25)
        self.level = (25, 26)
        self.time_zone = (26, 27)
        self.notam = (27, 28)
        # PAD 2
        self.boundary_via = (30, 32)
        self.lat = (32, 51)
        self.lon = (32, 51)
        self.arc_lat = (51, 70)
        self.arc_lon = (51, 70)
        self.arc_dist = (70, 74)
        self.arc_bearing = (74, 78)
        self.rnp = (78, 81)
        self.lower_limit = (81, 86)
        self.lower_unit = (86, 87)
        self.upper_limit = (87, 92)
        self.upper_unit = (92, 93)
        self.airspace_name = (93, 123)


class TimeIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (24, 25)
        self.application = (25, 26)
        self.time_zone = (26, 27)
        self.notam = (27, 28)
        self.daylight_ind = (28, 29)
        self.op_time_1 = (29, 39)
        self.op_time_2 = (39, 49)
        self.op_time_3 = (49, 59)
        self.op_time_4 = (59, 69)
        self.op_time_5 = (69, 79)
        self.op_time_6 = (79, 89)
        self.op_time_7 = (89, 99)
        self.controlling_agency = (99, 123)


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_tim = TimeIndices()
