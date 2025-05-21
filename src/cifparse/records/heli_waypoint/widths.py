class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        self.area = (1, 4)
        self.sec_code = (4, 5)
        # PAD 1
        self.heliport = (6, 10)
        self.heliport_region = (10, 12)
        self.heliport_sub_code = (12, 13)
        self.waypoint_id = (13, 18)
        # PAD 1
        self.waypoint_region = (19, 21)
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
        # PAD 4
        self.type = (26, 29)
        self.usage = (29, 31)
        # PAD 1
        self.lat = (32, 41)
        self.lon = (41, 51)
        # PAD 23
        self.mag_var = (74, 79)
        self.elevation = (79, 84)
        self.datum_code = (84, 87)
        # PAD 8
        self.name_indicator = (95, 98)
        self.name_description = (98, 123)


class ContinuationIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.cont_rec_no = (21, 22)
        self.application = (22, 23)
        self.notes = (23, 92)
        # RESERVED 31


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


class PlanningContinuation(PrimaryIndices):
    def __init__(self):
        super().__init__()


w_bas = BaseIndices()
w_pri = PrimaryIndices()
w_con = ContinuationIndices()
w_pla = PlanningIndices()
