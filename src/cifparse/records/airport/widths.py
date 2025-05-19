class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        self.sub_code = (12, 13)
        self.iata = (13, 16)
        # RESERVED 2
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
        self.limit_alt = (22, 27)
        self.longest = (27, 30)
        self.is_ifr = (30, 31)
        self.longest_surface = (31, 32)
        self.lat = (32, 41)
        self.lon = (41, 51)
        self.mag_var = (51, 56)
        self.elevation = (56, 61)
        self.limit_speed = (61, 64)
        self.rec_vhf = (64, 68)
        self.rec_vhf_region = (68, 70)
        self.transition_alt = (70, 75)
        self.transition_level = (75, 80)
        self.usage = (80, 81)
        self.time_zone = (81, 84)
        self.daylight_ind = (84, 85)
        self.mag_true = (85, 86)
        self.datum_code = (86, 89)
        # RESERVED 4
        self.airport_name = (93, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.notes = (23, 93)
        # RESERVED 30


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.fir_ident = (23, 27)
        self.uir_ident = (27, 31)
        self.se_ind = (31, 32)
        self.se_date = (32, 43)
        # RESERVED 23
        self.as_ind = (66, 67)
        self.as_airport_id = (67, 71)
        self.as_code = (71, 73)
        # RESERVED 50


class PlanningContinuationIndices(PrimaryIndices):
    def __init__(self):
        super().__init__()


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_pla = PlanningIndices()
w_plc = PlanningContinuationIndices()
