from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_pri


class Primary(Base):
    start_lat: float
    start_lon: float
    mora_1: int
    mora_2: int
    mora_3: int
    mora_4: int
    mora_5: int
    mora_6: int
    mora_7: int
    mora_8: int
    mora_9: int
    mora_10: int
    mora_11: int
    mora_12: int
    mora_13: int
    mora_14: int
    mora_15: int
    mora_16: int
    mora_17: int
    mora_18: int
    mora_19: int
    mora_20: int
    mora_21: int
    mora_22: int
    mora_23: int
    mora_24: int
    mora_25: int
    mora_26: int
    mora_27: int
    mora_28: int
    mora_29: int
    mora_30: int

    def __init__(self):
        super().__init__("moras")
        self.start_lat = None
        self.start_lon = None
        self.mora_1 = None
        self.mora_2 = None
        self.mora_3 = None
        self.mora_4 = None
        self.mora_5 = None
        self.mora_6 = None
        self.mora_7 = None
        self.mora_8 = None
        self.mora_9 = None
        self.mora_10 = None
        self.mora_11 = None
        self.mora_12 = None
        self.mora_13 = None
        self.mora_14 = None
        self.mora_15 = None
        self.mora_16 = None
        self.mora_17 = None
        self.mora_18 = None
        self.mora_19 = None
        self.mora_20 = None
        self.mora_21 = None
        self.mora_22 = None
        self.mora_23 = None
        self.mora_24 = None
        self.mora_25 = None
        self.mora_26 = None
        self.mora_27 = None
        self.mora_28 = None
        self.mora_29 = None
        self.mora_30 = None

    def from_line(self, line: str) -> "Primary":
        super().from_line(line)
        self.start_lat = extract_field(line, w_pri.start_lat)
        self.start_lon = extract_field(line, w_pri.start_lon)
        self.mora_1 = extract_field(line, w_pri.mora_1)
        self.mora_2 = extract_field(line, w_pri.mora_2)
        self.mora_3 = extract_field(line, w_pri.mora_3)
        self.mora_4 = extract_field(line, w_pri.mora_4)
        self.mora_5 = extract_field(line, w_pri.mora_5)
        self.mora_6 = extract_field(line, w_pri.mora_6)
        self.mora_7 = extract_field(line, w_pri.mora_7)
        self.mora_8 = extract_field(line, w_pri.mora_8)
        self.mora_9 = extract_field(line, w_pri.mora_9)
        self.mora_10 = extract_field(line, w_pri.mora_10)
        self.mora_11 = extract_field(line, w_pri.mora_11)
        self.mora_12 = extract_field(line, w_pri.mora_12)
        self.mora_13 = extract_field(line, w_pri.mora_13)
        self.mora_14 = extract_field(line, w_pri.mora_14)
        self.mora_15 = extract_field(line, w_pri.mora_15)
        self.mora_16 = extract_field(line, w_pri.mora_16)
        self.mora_17 = extract_field(line, w_pri.mora_17)
        self.mora_18 = extract_field(line, w_pri.mora_18)
        self.mora_19 = extract_field(line, w_pri.mora_19)
        self.mora_20 = extract_field(line, w_pri.mora_20)
        self.mora_21 = extract_field(line, w_pri.mora_21)
        self.mora_22 = extract_field(line, w_pri.mora_22)
        self.mora_23 = extract_field(line, w_pri.mora_23)
        self.mora_24 = extract_field(line, w_pri.mora_24)
        self.mora_25 = extract_field(line, w_pri.mora_25)
        self.mora_26 = extract_field(line, w_pri.mora_26)
        self.mora_27 = extract_field(line, w_pri.mora_27)
        self.mora_28 = extract_field(line, w_pri.mora_28)
        self.mora_29 = extract_field(line, w_pri.mora_29)
        self.mora_30 = extract_field(line, w_pri.mora_30)
        return self

    def ordered_fields(self) -> list:
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "start_lat",
                "start_lon",
                "mora_1",
                "mora_2",
                "mora_3",
                "mora_4",
                "mora_5",
                "mora_6",
                "mora_7",
                "mora_8",
                "mora_9",
                "mora_10",
                "mora_11",
                "mora_12",
                "mora_13",
                "mora_14",
                "mora_15",
                "mora_16",
                "mora_17",
                "mora_18",
                "mora_19",
                "mora_20",
                "mora_21",
                "mora_22",
                "mora_23",
                "mora_24",
                "mora_25",
                "mora_26",
                "mora_27",
                "mora_28",
                "mora_29",
                "mora_30",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "start_lat": self.start_lat,
            "start_lon": self.start_lon,
            "mora_1": self.mora_1,
            "mora_2": self.mora_2,
            "mora_3": self.mora_3,
            "mora_4": self.mora_4,
            "mora_5": self.mora_5,
            "mora_6": self.mora_6,
            "mora_7": self.mora_7,
            "mora_8": self.mora_8,
            "mora_9": self.mora_9,
            "mora_10": self.mora_10,
            "mora_11": self.mora_11,
            "mora_12": self.mora_12,
            "mora_13": self.mora_13,
            "mora_14": self.mora_14,
            "mora_15": self.mora_15,
            "mora_16": self.mora_16,
            "mora_17": self.mora_17,
            "mora_18": self.mora_18,
            "mora_19": self.mora_19,
            "mora_20": self.mora_20,
            "mora_21": self.mora_21,
            "mora_22": self.mora_22,
            "mora_23": self.mora_23,
            "mora_24": self.mora_24,
            "mora_25": self.mora_25,
            "mora_26": self.mora_26,
            "mora_27": self.mora_27,
            "mora_28": self.mora_28,
            "mora_29": self.mora_29,
            "mora_30": self.mora_30,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
