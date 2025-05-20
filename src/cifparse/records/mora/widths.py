class BaseIndices:
    def __init__(self):
        self.st = (0, 1)
        # PAD 3
        self.sec_code = (4, 5)
        self.sub_code = (5, 6)
        # PAD 7
        #
        # OTHER
        # FIELDS
        #
        self.record_number = (123, 128)
        self.cycle_data = (128, 132)


class PrimaryIndices(BaseIndices):
    def __init__(self):
        super().__init__()
        self.start_lat = (13, 16)
        self.start_lon = (16, 20)
        # PAD 10
        self.mora_1 = (30, 33)
        self.mora_2 = (33, 36)
        self.mora_3 = (36, 39)
        self.mora_4 = (39, 42)
        self.mora_5 = (42, 45)
        self.mora_6 = (45, 48)
        self.mora_7 = (48, 51)
        self.mora_8 = (51, 54)
        self.mora_9 = (54, 57)
        self.mora_10 = (57, 60)
        self.mora_11 = (60, 63)
        self.mora_12 = (63, 66)
        self.mora_13 = (66, 69)
        self.mora_14 = (69, 72)
        self.mora_15 = (72, 75)
        self.mora_16 = (75, 78)
        self.mora_17 = (78, 81)
        self.mora_18 = (81, 84)
        self.mora_19 = (84, 87)
        self.mora_20 = (87, 90)
        self.mora_21 = (90, 93)
        self.mora_22 = (93, 96)
        self.mora_23 = (96, 99)
        self.mora_24 = (99, 102)
        self.mora_25 = (102, 105)
        self.mora_26 = (105, 108)
        self.mora_27 = (108, 111)
        self.mora_28 = (111, 114)
        self.mora_29 = (114, 117)
        self.mora_30 = (117, 120)
        # RESERVED 3


w_bas = BaseIndices()
w_pri = PrimaryIndices()
