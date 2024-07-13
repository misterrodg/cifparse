from .cifp_functions import chunk, clean_value
from .cifp_restrictive_airspace_segment import CIFPRestrictiveAirspaceSegment


class CIFPRestrictiveAirspace:
    def __init__(self) -> None:
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.region = None
        self.restrictive_id = None
        self.restrictive_type = None
        self.restrictive_designation = None
        self.restrictive_name = None
        self.application_type = None
        self.time_ind = None
        self.op_time_1 = None
        self.op_time_2 = None
        self.op_time_3 = None
        self.op_time_4 = None
        self.op_time_5 = None
        self.op_time_6 = None
        self.op_time_7 = None
        self.controlling_agency = None
        self.segments: list[CIFPRestrictiveAirspaceSegment] = []

    def from_lines(self, cifp_lines: list) -> None:
        point_lines = []
        for cifp_line in cifp_lines:
            cont_rec_no = int(cifp_line[24:25])
            if cont_rec_no == 0 or cont_rec_no == 1:
                point_lines.append(cifp_line)
            if cont_rec_no == 1:
                self._cont1(cifp_line)
            if cont_rec_no == 2:
                self._cont2(cifp_line)

        segment_chunked = chunk(point_lines, 19, 20)
        self._segment_to_object(segment_chunked)

    def _segment_to_object(self, chunked_list: list) -> None:
        for segment_chunk in chunked_list:
            segment = CIFPRestrictiveAirspaceSegment()
            segment.from_lines(segment_chunk)
            self.segments.append(segment)

    def _cont1(self, cifp_line: str) -> None:
        if self.restrictive_name == None:
            # PAD 1
            self.area = cifp_line[1:4].strip()
            self.sec_code = cifp_line[4:5].strip()
            self.sub_code = cifp_line[5:6].strip()
            self.region = cifp_line[6:8].strip()
            self.restrictive_type = cifp_line[8:9].strip()
            self.restrictive_designation = cifp_line[9:19].strip()
            self.restrictive_name = cifp_line[93:123].strip()

            if self.restrictive_type != "M":
                self.restrictive_id = (
                    f"{self.restrictive_type}{self.restrictive_designation}"
                )
            else:
                self.restrictive_id = self.restrictive_designation

    def _cont2(self, cifp_line: str) -> None:
        # PAD 25
        # cont_rec_no = int(cifp_line[24:25].strip())
        self.application_type = cifp_line[25:26].strip()
        self.time_code = cifp_line[26:27].strip()
        self.notam = cifp_line[27:28].strip()
        self.time_ind = cifp_line[28:29].strip()
        self.op_time_1 = cifp_line[29:39].strip()
        self.op_time_2 = cifp_line[39:49].strip()
        self.op_time_3 = cifp_line[49:59].strip()
        self.op_time_4 = cifp_line[59:69].strip()
        self.op_time_5 = cifp_line[69:79].strip()
        self.op_time_6 = cifp_line[79:89].strip()
        self.op_time_7 = cifp_line[89:99].strip()
        self.controlling_agency = cifp_line[99:123].strip()
        # self.record_number = cifp_line[123:128].strip()
        # self.cycle_data = cifp_line[128:132].strip()

    def to_dict(self) -> dict:
        segments = []
        for item in self.segments:
            segments.append(item.to_dict())

        return {
            "area": clean_value(self.area),
            "sec_code": clean_value(self.sec_code),
            "sub_code": clean_value(self.sub_code),
            "region": clean_value(self.region),
            "restrictive_type": clean_value(self.restrictive_type),
            "restrictive_designation": clean_value(self.restrictive_designation),
            "restrictive_name": clean_value(self.restrictive_name),
            "application_type": clean_value(self.application_type),
            "time_ind": clean_value(self.time_ind),
            "op_time_1": clean_value(self.op_time_1),
            "op_time_2": clean_value(self.op_time_2),
            "op_time_3": clean_value(self.op_time_3),
            "op_time_4": clean_value(self.op_time_4),
            "op_time_5": clean_value(self.op_time_5),
            "op_time_6": clean_value(self.op_time_6),
            "op_time_7": clean_value(self.op_time_7),
            "controlling_agency": clean_value(self.controlling_agency),
            "segments": segments,
        }