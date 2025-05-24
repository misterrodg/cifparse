from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        # PAD 1
        self.heliport_id = (6, 10, field_541)
        self.heliport_region = (10, 12, field_514)
        self.heliport_sub_code = (12, 13, field_55)
        self.waypoint_id = (13, 18, field_513)
        # PAD 1
        self.waypoint_region = (19, 21, field_514)
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
        # PAD 4
        self.type = (26, 29, field_542)
        self.usage = (29, 31, field_582)
        # PAD 1
        self.lat = (32, 41, field_536)
        self.lon = (41, 51, field_537)
        # PAD 23
        self.mag_var = (74, 79, field_539)
        self.datum_code = (84, 87, field_5197)
        # PAD 8
        self.name_indicator = (95, 98, field_5196)
        self.name_description = (98, 123, field_543)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22, field_516)
        self.application = (22, 23, field_591)
        self.notes = (23, 92, field_561)
        # RESERVED 31


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


class PlanningContinuation(PrimaryIndices):
    def __init__(self):
        super().__init__()


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_pla = PlanningIndices()
