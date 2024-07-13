from .cifp_functions import clean_value, convert_dms


class CIFPRunway:
    def __init__(self) -> None:
        self.area = None
        self.airport_id = None
        self.region = None
        self.runway_id = None
        self.length = None
        self.bearing = None
        self.lat = None
        self.lon = None
        self.gradient = None
        self.ellipsoidal_height = None
        self.threshold_elevation = None
        self.displaced_threshold = None
        self.tch = None
        self.width = None
        self.tch_id = None
        self.vhf_ident = None
        self.cat = None
        self.stopway = None
        self.vhf_ident_2 = None
        self.cat_2 = None
        self.description = None
        self.record_number = None
        self.cycle_data = None

    def from_line(self, cifp_line: str) -> None:
        # PAD 1
        self.area = cifp_line[1:4].strip()
        # self._sec_code = cifp_line[4:5].strip()
        # PAD 1
        self.airport_id = cifp_line[6:10].strip()
        self.region = cifp_line[10:12].strip()
        # sub_code = cifp_line[12:13].strip()
        self.runway_id = cifp_line[13:18].strip()
        # PAD 3
        # cont_rec_no = int(cifp_line[21:22].strip())
        runway_length = cifp_line[22:27].strip()
        runway_bearing = cifp_line[27:31].strip()
        # PAD 1
        lat_lon = cifp_line[32:51].strip()
        runway_gradient = cifp_line[51:56].strip()
        # PAD 4
        ell_height = cifp_line[60:66].strip()
        thr_elevation = cifp_line[66:71].strip()
        dis_threshold = cifp_line[71:75].strip()
        thr_cross_height = cifp_line[75:77].strip()
        runway_width = cifp_line[77:80].strip()
        self.tch_id = cifp_line[80:81].strip()
        self.vhf_ident = cifp_line[81:85].strip()
        self.cat = cifp_line[85:86].strip()
        runway_stopway = cifp_line[86:90].strip()
        self.vhf_ident_2 = cifp_line[90:94].strip()
        self.cat_2 = cifp_line[94:95].strip()
        # PAD 6
        self.description = cifp_line[101:123].strip()
        self.record_number = int(cifp_line[123:128].strip())
        self.cycle_data = cifp_line[128:132].strip()

        if runway_length != "":
            self.length = int(runway_length)

        if runway_bearing != "":
            self.bearing = int(runway_bearing) / 10

        if lat_lon != "":
            coordinates = convert_dms(lat_lon)
            self.lat = coordinates.lat
            self.lon = coordinates.lon

        if runway_gradient != "":
            self.gradient = int(runway_gradient)

        if ell_height != "":
            self.ellipsoidal_height = int(ell_height)

        if thr_elevation != "":
            self.threshold_elevation = int(thr_elevation)

        if dis_threshold != "":
            self.displaced_threshold = int(dis_threshold)

        if thr_cross_height != "":
            self.tch = int(thr_cross_height)

        if runway_width != "":
            self.width = int(runway_width)

        if runway_stopway != "":
            self.stopway = int(runway_stopway)

    def to_dict(self) -> dict:
        return {
            "area": clean_value(self.area),
            "airport_id": clean_value(self.airport_id),
            "region": clean_value(self.region),
            "runway_id": clean_value(self.runway_id),
            "length": clean_value(self.length),
            "bearing": clean_value(self.bearing),
            "lat": clean_value(self.lat),
            "lon": clean_value(self.lon),
            "gradient": clean_value(self.gradient),
            "ellipsoidal_height": clean_value(self.ellipsoidal_height),
            "threshold_elevation": clean_value(self.threshold_elevation),
            "displaced_threshold": clean_value(self.displaced_threshold),
            "tch": clean_value(self.tch),
            "width": clean_value(self.width),
            "tch_id": clean_value(self.tch_id),
            "vhf_ident": clean_value(self.vhf_ident),
            "cat": clean_value(self.cat),
            "stopway": clean_value(self.stopway),
            "vhf_ident_2": clean_value(self.vhf_ident_2),
            "cat_2": clean_value(self.cat_2),
            "description": clean_value(self.description),
            "record_number": clean_value(self.record_number),
            "cycle_data": clean_value(self.cycle_data),
        }
