from cifparse.functions import *


class BaseIndices:
    def __init__(self):
        self.st = (0, 1, field_52)
        # PAD 3
        self.sec_code = (4, 5, field_54)
        self.sub_code = (5, 6, field_55)
        # PAD 7
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128, field_531)
        self.cycle_data = (128, 132, field_532)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.start_lat = (13, 16, field_5141)
        self.start_lon = (16, 20, field_5142)
        # PAD 10
        self.mora_1 = (30, 33, field_5143)
        self.mora_2 = (33, 36, field_5143)
        self.mora_3 = (36, 39, field_5143)
        self.mora_4 = (39, 42, field_5143)
        self.mora_5 = (42, 45, field_5143)
        self.mora_6 = (45, 48, field_5143)
        self.mora_7 = (48, 51, field_5143)
        self.mora_8 = (51, 54, field_5143)
        self.mora_9 = (54, 57, field_5143)
        self.mora_10 = (57, 60, field_5143)
        self.mora_11 = (60, 63, field_5143)
        self.mora_12 = (63, 66, field_5143)
        self.mora_13 = (66, 69, field_5143)
        self.mora_14 = (69, 72, field_5143)
        self.mora_15 = (72, 75, field_5143)
        self.mora_16 = (75, 78, field_5143)
        self.mora_17 = (78, 81, field_5143)
        self.mora_18 = (81, 84, field_5143)
        self.mora_19 = (84, 87, field_5143)
        self.mora_20 = (87, 90, field_5143)
        self.mora_21 = (90, 93, field_5143)
        self.mora_22 = (93, 96, field_5143)
        self.mora_23 = (96, 99, field_5143)
        self.mora_24 = (99, 102, field_5143)
        self.mora_25 = (102, 105, field_5143)
        self.mora_26 = (105, 108, field_5143)
        self.mora_27 = (108, 111, field_5143)
        self.mora_28 = (111, 114, field_5143)
        self.mora_29 = (114, 117, field_5143)
        self.mora_30 = (117, 120, field_5143)
        # RESERVED 3


w_bas = BaseIndices()
w_pri = PrimaryIndices()
