from .cifp_functions import clean_value, convert_dms, convert_mag_var


class CIFPWaypoint:
    def __init__(self) -> None:
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.environment = None
        self.environment_region = None
        self.waypoint_id = None
        self.region = None
        self.type = None
        self.usage = None
        self.lat = None
        self.lon = None
        self.mag_var = None
        self.elevation = None
        self.datum_code = None
        self.name = None
        self.name_description = None
        self.application = None
        self.notes = None
        self.record_number = None
        self.cycle_data = None

    def from_lines(self, cifp_lines: list) -> None:
        for cifp_line in cifp_lines:
            cont_rec_no = int(cifp_line[21:22])
            if cont_rec_no == 0:
                self._cont0(cifp_line)
            if cont_rec_no == 1:
                self._cont1(cifp_line)

    def _cont0(self, cifp_line: str) -> None:
        # PAD 1
        self.area = cifp_line[1:4].strip()
        self.sec_code = cifp_line[4:5].strip()
        self.sub_code = cifp_line[5:6].strip()
        self.environment = cifp_line[6:10].strip()
        self.environment_region = cifp_line[10:12].strip()
        # PAD 1
        self.waypoint_id = cifp_line[13:18].strip()
        # PAD 1
        self.region = cifp_line[19:21].strip()
        # self.cont_rec_no = int(cifp_line[21:22].strip())
        # PAD 4
        self.type = cifp_line[26:29].strip()
        self.usage = cifp_line[29:31].strip()
        # PAD 1
        lat_lon = cifp_line[32:51].strip()
        # PAD 23
        variation = cifp_line[74:79].strip()
        elevation = cifp_line[79:84].strip()
        self.datum_code = cifp_line[84:87].strip()
        # PAD 8
        self.name = cifp_line[95:98].strip()
        self.name_description = cifp_line[98:123].strip()
        self.record_number = int(cifp_line[123:128].strip())
        self.cycle_data = cifp_line[128:132].strip()

        if lat_lon != "":
            coordinates = convert_dms(lat_lon)
            self.lat = coordinates.lat
            self.lon = coordinates.lon

        if variation != "":
            mag_var = convert_mag_var(variation)
            self.mag_var = mag_var

        if elevation != "":
            self.elevation = int(elevation)

    def _cont1(self, cifp_line: str) -> None:
        # PAD 22
        self.application = cifp_line[22:23].strip()
        self.notes = cifp_line[23:91].strip()

    def to_dict(self) -> dict:
        return {
            "area": clean_value(self.area),
            "sec_code": clean_value(self.sec_code),
            "sub_code": clean_value(self.sub_code),
            "environment": clean_value(self.environment),
            "environment_region": clean_value(self.environment_region),
            "waypoint_id": clean_value(self.waypoint_id),
            "region": clean_value(self.region),
            "type": clean_value(self.type),
            "usage": clean_value(self.usage),
            "lat": clean_value(self.lat),
            "lon": clean_value(self.lon),
            "mag_var": clean_value(self.mag_var),
            "elevation": clean_value(self.elevation),
            "datum_code": clean_value(self.datum_code),
            "name": clean_value(self.name),
            "name_description": clean_value(self.name_description),
            "application": clean_value(self.application),
            "notes": clean_value(self.notes),
            "record_number": clean_value(self.record_number),
            "cycle_data": clean_value(self.cycle_data),
        }
