class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        self.from_1 = (6, 11)
        # PAD 1
        self.from_region_1 = (12, 14)
        self.from_sec_code_1 = (14, 15)
        self.from_sub_code_1 = (15, 16)
        self.from_2 = (16, 21)
        # PAD 1
        self.from_region_2 = (22, 24)
        self.from_sec_code_2 = (24, 25)
        self.from_sub_code_2 = (25, 26)
        self.company_route_id = (26, 36)
        self.seq_no = (36, 39)
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.via = (39, 42)
        self.path_id = (42, 48)
        self.path_area = (48, 51)
        self.to_1 = (51, 57)
        self.to_region_1 = (57, 59)
        self.to_sec_code_1 = (59, 60)
        self.to_sub_code_1 = (60, 61)
        self.runway_transition = (61, 66)
        self.enroute_transition = (66, 71)
        # PAD 1
        self.cruise_altitude = (72, 77)
        self.term_alt_ref = (77, 81)
        self.term_alt_region = (81, 83)
        self.alt_dist = (83, 87)
        self.cost_index = (87, 90)
        self.enrt_alt_ref = (90, 94)
        # RESERVED 29


w_bas = BaseIndices()
w_pri = PrimaryIndices()
