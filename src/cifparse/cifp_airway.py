from cifp_airway_point import CIFPAirwayPoint
from cifp_functions import clean_value


class CIFPAirway:
    def __init__(self) -> None:
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.id = None
        self.six_char = None
        self.application = None
        self.notes = None
        self.points: list[CIFPAirwayPoint] = []
        self._is_start_set = False

    def from_lines(self, cifp_lines: list) -> None:
        for cifp_line in cifp_lines:
            cont_rec_no = int(cifp_line[38:39])
            if cont_rec_no == 0:
                self._cont0(cifp_line)
            if cont_rec_no == 1:
                self._cont1(cifp_line)

    def _cont0(self, cifp_line: str) -> None:
        if self.id == None:
            # PAD 1
            self.area = cifp_line[1:4].strip()
            self.sec_code = cifp_line[4:5].strip()
            self.sub_code = cifp_line[5:6].strip()
            # PAD 7
            self.id = cifp_line[13:18].strip()
            self.six_char = cifp_line[18:19].strip()

        point = CIFPAirwayPoint()
        point.from_line(cifp_line)

        is_start = False
        if self._is_start_set == False:
            self._is_start_set = True
            is_start = True

        desc_code = cifp_line[39:43]
        is_end = False
        if desc_code[1:2] == "E":
            self._is_start_set = False
            is_end = True

        if is_start == True:
            sig_point = "S"
            point.set_sig_point(sig_point)
        if is_end == True:
            sig_point = "E"
            point.set_sig_point(sig_point)

        self.points.append(point)

    def _cont1(self, cifp_line: str) -> None:
        # PAD 38
        self.application = cifp_line[39:40]
        self.notes = cifp_line[40:109]

    def to_dict(self) -> dict:
        points = []
        for item in self.points:
            points.append(item.to_dict())

        return {
            "area": clean_value(self.area),
            "sec_code": clean_value(self.sec_code),
            "sub_code": clean_value(self.sub_code),
            "id": clean_value(self.id),
            "six_char": clean_value(self.six_char),
            "application": clean_value(self.application),
            "notes": clean_value(self.notes),
            "points": points,
        }
