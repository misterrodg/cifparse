from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        # PAD 1
        self.heliport_id = (6, 10, field_56)
        self.heliport_region = (10, 12, field_514)
        self.sub_code = (12, 13, field_55)
        self.iata = (13, 16, field_5107)
        self.pad_id = (16, 21, field_5180)
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
        self.limit_alt = (22, 27, field_573)
        self.datum_code = (27, 30, field_5197)
        self.is_ifr = (30, 31, field_5108)
        # PAD 1
        self.lat = (32, 41, field_536)
        self.lon = (41, 51, field_537)
        self.mag_var = (51, 56, field_539)
        self.elevation = (56, 61, field_555)
        self.speed_limit = (61, 64, field_572)
        self.rec_vhf = (64, 68, field_523)
        self.rec_vhf_region = (68, 70, field_514)
        self.transition_alt = (70, 75, field_553)
        self.transition_level = (75, 80, field_553)
        self.usage = (80, 81, field_5177)
        self.time_zone = (81, 84, field_5178)
        self.daylight_ind = (84, 85, field_5179)
        self.pad_dimensions = (85, 91, field_5176)
        self.mag_true = (91, 92, field_5165)
        # RESERVED 1
        self.heliport_name = (93, 123, field_571)


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
        # RESERVED 23
        self.as_ind = (66, 67, field_5217)
        self.as_heliport_id = (67, 71, field_56)
        self.as_region = (71, 73, field_514)
        # RESERVED 50


class PlanningContinuationIndices(PrimaryIndices):
    def __init__(self):
        super().__init__()


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_pla = PlanningIndices()
w_plc = PlanningContinuationIndices()
