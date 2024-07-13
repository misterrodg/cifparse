from .cifp_functions import convert_dms, convert_mag_var


class CIFP_NDB:
    def __init__(self) -> None:
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.airport_id = None
        self.airport_region = None
        self.ndb_id = None
        self.ndb_region = None
        self.frequency = None
        self.nav_class = None
        self.lat = None
        self.lon = None
        self.mag_var = None
        self.datum_code = None
        self.name = None
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
        self.airport_id = cifp_line[6:10].strip()
        self.airport_region = cifp_line[10:12].strip()
        # PAD 1
        self.ndb_id = cifp_line[13:17].strip()
        # PAD 2
        self.ndb_region = cifp_line[19:21].strip()
        # self.cont_rec_no = int(cifp_line[21:22].strip())
        freq = cifp_line[22:27].strip()
        self.nav_class = cifp_line[27:32].strip()
        lat_lon = cifp_line[32:51].strip()
        # PAD 23
        variation = cifp_line[74:79].strip()
        # PAD 6
        # RESERVED 5
        self.datum_code = cifp_line[90:93].strip()
        self.name = cifp_line[93:123].strip()
        self.record_number = int(cifp_line[123:128].strip())
        self.cycle_data = cifp_line[128:132].strip()

        if freq != "":
            self.frequency = int(freq) / 10

        if lat_lon != "":
            coordinates = convert_dms(lat_lon)
            self.lat = coordinates.lat
            self.lon = coordinates.lon

        if variation != "":
            mag_var = convert_mag_var(variation)
            self.mag_var = mag_var

    def _cont1(self, cifp_line: str) -> None:
        # PAD 22
        self.application = cifp_line[22:23].strip()
        self.notes = cifp_line[23:91].strip()
