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
        self.runway_id = (13, 18, field_546)
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
        self.length = (22, 27, field_557)
        self.bearing = (27, 31, field_558)
        # PAD 1
        self.lat = (32, 41, field_536)
        self.lon = (41, 51, field_537)
        self.gradient = (51, 56, field_5212)
        # PAD 4
        self.ellipsoidal_height = (60, 66, field_5225)
        self.threshold_elevation = (66, 71, field_568)
        self.displaced_threshold = (71, 75, field_569)
        self.tch = (75, 77, field_567)
        self.width = (77, 80, field_5109)
        self.tch_id = (80, 81, field_5270)
        self.ls_ident_1 = (81, 85, field_544)
        self.cat_1 = (85, 86, field_580)
        self.stopway = (86, 90, field_579)
        self.ls_ident_2 = (90, 94, field_544)
        self.cat_2 = (94, 95, field_580)
        # RESERVED 6
        self.description = (101, 123, field_559)


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
        # PAD 28
        self.true_bearing = (51, 56, field_594)
        self.source = (56, 57, field_595)
        # PAD 8
        self.location = (65, 66, field_598)
        self.tdz_elev = (66, 71, field_597)
        # RESERVED 52


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_sim = SimulationIndices()
