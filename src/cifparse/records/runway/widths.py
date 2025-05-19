class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        self.sub_code = (12, 13)
        self.runway_id = (13, 18)
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
        self.length = (22, 27)
        self.bearing = (27, 31)
        # PAD 1
        self.lat = (32, 41)
        self.lon = (41, 51)
        self.gradient = (51, 56)
        # PAD 4
        self.ellipsoidal_height = (60, 66)
        self.threshold_elevation = (66, 71)
        self.displaced_threshold = (71, 75)
        self.tch = (75, 77)
        self.width = (77, 80)
        self.tch_id = (80, 81)
        self.ls_ident_1 = (81, 85)
        self.cat_1 = (85, 86)
        self.stopway = (86, 90)
        self.ls_ident_2 = (90, 94)
        self.cat_2 = (94, 95)
        # RESERVED 6
        self.description = (101, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.notes = (23, 92)
        # RESERVED 31


class SimulationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        # PAD 28
        self.true_bearing = (51, 56)
        self.source = (56, 57)
        # PAD 8
        self.location = (65, 66)
        self.tdz_elev = (66, 71)
        # RESERVED 52


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_sim = SimulationIndices()
