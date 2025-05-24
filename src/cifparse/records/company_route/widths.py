from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        self.area = (1, 4, field_53)
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        self.from_1 = (6, 11, field_575)
        # PAD 1
        self.from_region_1 = (12, 14, field_514)
        self.from_sec_code_1 = (14, 15, field_54)
        self.from_sub_code_1 = (15, 16, field_55)
        self.from_2 = (16, 21, field_575)
        # PAD 1
        self.from_region_2 = (22, 24, field_514)
        self.from_sec_code_2 = (24, 25, field_54)
        self.from_sub_code_2 = (25, 26, field_55)
        self.company_route_id = (26, 36, field_576)
        self.seq_no = (36, 39, field_512)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.via = (39, 42, field_577)
        self.path_id = (42, 48, field_578)
        self.path_area = (48, 51, field_53)
        self.to_1 = (51, 57, field_583)
        self.to_region_1 = (57, 59, field_514)
        self.to_sec_code_1 = (59, 60, field_54)
        self.to_sub_code_1 = (60, 61, field_55)
        self.runway_transition = (61, 66, field_584)
        self.enroute_transition = (66, 71, field_585)
        # PAD 1
        self.cruise_altitude = (72, 77, field_586)
        self.term_alt_ref = (77, 81, field_587)
        self.term_alt_region = (81, 83, field_514)
        self.alt_dist = (83, 87, field_588)
        self.cost_index = (87, 90, field_589)
        self.enrt_alt_ref = (90, 94, field_5148)
        # RESERVED 29


w_bas = BaseIndices()
w_pri = PrimaryIndices()
