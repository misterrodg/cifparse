class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.airport_id = (6, 10)
        self.airport_region = (10, 12)
        # PAD 1
        self.ndb_id = (13, 17)
        # PAD 2
        self.ndb_region = (19, 21)
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
        self.frequency = (22, 27)
        self.nav_class = (27, 32)
        self.lat = (32, 41)
        self.lon = (41, 51)
        # PAD 23
        self.mag_var = (74, 79)
        # PAD 6
        # RESERVED 5
        self.datum_code = (90, 93)
        self.ndb_name = (93, 123)


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
        # PAD 4
        self.fac_char = (27, 32)
        # PAD 47
        self.fac_elev = (79, 84)
        # RESERVED 39


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.fir_ident = (23, 27)
        self.uir_ident = (27, 31)
        self.se_ind = (31, 32)
        self.se_date = (32, 43)
        # RESERVED 80


class PlanningContinuationIndices(PrimaryIndices):
    def __init__(self):
        super().__init__()


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_sim = SimulationIndices()
w_pla = PlanningIndices()
w_plc = PlanningContinuationIndices()
