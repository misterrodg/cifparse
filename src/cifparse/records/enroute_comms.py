from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .enroute_comm.primary import Primary
from .enroute_comm.combined import Combined
from .enroute_comm.time import Time
from .enroute_comm.widths import w_pri, w_com, w_tim

from sqlite3 import Cursor


class EnrouteComm(RecordBase):
    primary: Primary
    combined: list[Combined]
    time: list[Time]

    def __init__(self, enroute_comm_partition: list[str]):
        self.primary = None
        self.combined = []
        self.time = []

        for line in enroute_comm_partition:
            cont_rec_no = extract_field(line, w_pri.cont_rec_no)
            if cont_rec_no in [0, 1]:
                primary = Primary()
                self.primary = primary.from_line(line)
                continue
            else:
                application = extract_field(line, w_com.application)
                if application == a_table.combined:
                    combined = Combined()
                    self.combined.append(combined.from_line(line))
                    continue
                application = extract_field(line, w_tim.application)
                if application == a_table.time:
                    time = Time()
                    self.time.append(time.from_line(line))
                    continue

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        com = ", combined: [...]" if self.combined else ""
        tim = ", time: [...]" if self.time else ""
        return f"\n{self.__class__.__name__}{pri}{com}{tim}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "combined": [item.to_dict() for item in self.combined],
            "time": [item.to_dict() for item in self.time],
        }


class EnrouteComms:
    records: list[EnrouteComm]

    def __init__(self, enroute_comm_lines: list[str]):
        self.records = []

        print("    Parsing Enroute Comms")
        enroute_comm_partitioned = partition(enroute_comm_lines, 0, 55)
        for enroute_comm_partition in enroute_comm_partitioned:
            enroute_comm = EnrouteComm(enroute_comm_partition)
            self.records.append(enroute_comm)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        combined = []
        time = []

        print("    Processing Enroute Comms")
        for enroute_comm in self.records:
            if enroute_comm.has_primary():
                primary.append(enroute_comm.primary)
            if enroute_comm.has_combined():
                combined.extend(enroute_comm.combined)
            if enroute_comm.has_time():
                time.extend(enroute_comm.time)

        if primary:
            process_table(db_cursor, primary)
        if combined:
            process_table(db_cursor, combined)
        if time:
            process_table(db_cursor, time)
        return
