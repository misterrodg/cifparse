from .cifp_functions import clean_value, convert_dms


class CIFPRestrictiveAirspacePoint:
    def __init__(self) -> None:
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.region = None
        self.restrictive_type = None
        self.restrictive_designation = None
        self.multiple_code = None
        self.sequence_number = None
        self.level = None
        self.time_zone = None
        self.notam = None
        self.boundary_via = None
        self.lat = None
        self.lon = None
        self.arc_lat = None
        self.arc_lon = None
        self.arc_dist = None
        self.arc_bearing = None
        self.lower_limit = None
        self.lower_unit = None
        self.upper_limit = None
        self.upper_unit = None
        self.restrictive_name = None
        self.record_number = None
        self.cycle_data = None

    def from_line(self, cifp_line: str) -> None:
        self.area = cifp_line[1:4].strip()
        self.sec_code = cifp_line[4:5].strip()
        self.sub_code = cifp_line[5:6].strip()
        self.region = cifp_line[6:8].strip()
        self.restrictive_type = cifp_line[8:9].strip()
        self.restrictive_designation = cifp_line[9:19].strip()
        self.multiple_code = cifp_line[19:20].strip()
        self.sequence_number = int(cifp_line[20:24].strip())
        # cont_rec_no = int(cifp_line[24:25].strip())
        self.level = cifp_line[25:26].strip()
        self.time_zone = cifp_line[26:27].strip()
        self.notam = cifp_line[27:28].strip()
        # PAD 2
        self.boundary_via = cifp_line[30:32].strip()
        lat_lon = cifp_line[32:51].strip()
        arc_lat_lon = cifp_line[51:70].strip()
        arc_dist = cifp_line[70:74].strip()
        arc_bearing = cifp_line[74:78].strip()
        # PAD 3
        self.lower_limit = cifp_line[81:86].strip()
        self.lower_unit = cifp_line[86:87].strip()
        self.upper_limit = cifp_line[87:92].strip()
        self.upper_unit = cifp_line[92:93].strip()
        self.restrictive_name = cifp_line[93:123].strip()
        self.record_number = int(cifp_line[123:128].strip())
        self.cycle_data = cifp_line[128:132].strip()

        if lat_lon != "":
            coordinates = convert_dms(lat_lon)
            self.lat = coordinates.lat
            self.lon = coordinates.lon

        if arc_lat_lon != "":
            arc_coordinates = convert_dms(arc_lat_lon)
            self.arc_lat = arc_coordinates.lat
            self.arc_lon = arc_coordinates.lon

        if arc_dist != "":
            self.arc_dist = int(arc_dist) / 10

        if arc_bearing != "":
            self.arc_bearing = int(arc_bearing) / 10

    def to_dict(self) -> dict:
        return {
            "area": clean_value(self.area),
            "sec_code": clean_value(self.sec_code),
            "sub_code": clean_value(self.sub_code),
            "region": clean_value(self.region),
            "restrictive_type": clean_value(self.restrictive_type),
            "restrictive_designation": clean_value(self.restrictive_designation),
            "multiple_code": clean_value(self.multiple_code),
            "sequence_number": clean_value(self.sequence_number),
            "level": clean_value(self.level),
            "time_zone": clean_value(self.time_zone),
            "notam": clean_value(self.notam),
            "boundary_via": clean_value(self.boundary_via),
            "lat": clean_value(self.lat),
            "lon": clean_value(self.lon),
            "arc_lat": clean_value(self.arc_lat),
            "arc_lon": clean_value(self.arc_lon),
            "arc_dist": clean_value(self.arc_dist),
            "arc_bearing": clean_value(self.arc_bearing),
            "lower_limit": clean_value(self.lower_limit),
            "lower_unit": clean_value(self.lower_unit),
            "upper_limit": clean_value(self.upper_limit),
            "upper_unit": clean_value(self.upper_unit),
            "restrictive_name": clean_value(self.restrictive_name),
            "record_number": clean_value(self.record_number),
            "cycle_data": clean_value(self.cycle_data),
        }