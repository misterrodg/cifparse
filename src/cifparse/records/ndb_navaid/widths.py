from cifparse.functions.record import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.airport_id = (6, 10, field_56)
        self.airport_region = (10, 12, field_514)
        # PAD 1
        self.ndb_id = (13, 17, field_533)
        # PAD 2
        self.ndb_region = (19, 21, field_514)
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
        self.frequency = (22, 27, field_534)
        self.nav_class = (27, 32, field_535)
        self.lat = (32, 41, field_536)
        self.lon = (41, 51, field_537)
        # PAD 23
        self.mag_var = (74, 79, field_539)
        # PAD 6
        # RESERVED 5
        self.datum_code = (90, 93, field_5197)
        self.ndb_name = (93, 123, field_571)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        self.notes = (23, 92, field_561)
        # RESERVED 31


class SimulationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        # PAD 4
        self.fac_char = (27, 32, field_593)
        # PAD 47
        self.fac_elev = (79, 84, field_592)
        # RESERVED 39


class PlanningIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        self.fir_ident = (23, 27, field_5116)
        self.uir_ident = (27, 31, field_5116)
        self.se_ind = (31, 32, field_5152)
        self.se_date = (32, 43, field_5153)
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
