from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .heli_terminal_comm.primary import Primary
from .heli_terminal_comm.continuation import Continuation
from .heli_terminal_comm.time import Time
from .heli_terminal_comm.widths import w_pri, w_con, w_tim

from sqlite3 import Cursor


class HeliTerminalComm(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    time: list[Time]

    def __init__(self, heli_terminal_comm_partition: list[str]):
        self.primary = None
        self.continuation = []
        self.time = []

        for line in heli_terminal_comm_partition:
            cont_rec_no = extract_field(line, w_pri.cont_rec_no)
            if cont_rec_no in [0, 1]:
                primary = Primary()
                self.primary = primary.from_line(line)
                continue
            else:
                application = extract_field(line, w_con.application)
                if application == a_table.standard:
                    continuation = Continuation()
                    self.continuation.append(continuation.from_line(line))
                    continue
                application = extract_field(line, w_tim.application)
                if application == a_table.time:
                    time = Time()
                    self.time.append(time.from_line(line))
                    continue

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        con = ", continuation: [...]" if self.continuation else ""
        tim = ", time: [...]" if self.time else ""
        return f"\n{self.__class__.__name__}{pri}{con}{tim}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "continuation": [item.to_dict() for item in self.continuation],
            "time": [item.to_dict() for item in self.time],
        }


class HeliTerminalComms:
    records: list[HeliTerminalComm]

    def __init__(self, heli_terminal_comm_lines: list[str]):
        self.records = []

        print("    Parsing Heli Terminal Comms")
        heli_terminal_comm_partitioned = partition(heli_terminal_comm_lines, 0, 25)
        for heli_terminal_comm_partition in heli_terminal_comm_partitioned:
            heli_terminal_comm = HeliTerminalComm(heli_terminal_comm_partition)
            self.records.append(heli_terminal_comm)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []
        time = []

        print("    Processing Heli Terminal Comms")
        for heli_terminal_comm in self.records:
            if heli_terminal_comm.has_primary():
                primary.append(heli_terminal_comm.primary)
            if heli_terminal_comm.has_continuation():
                continuation.extend(heli_terminal_comm.continuation)
            if heli_terminal_comm.has_time():
                time.extend(heli_terminal_comm.time)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        if time:
            process_table(db_cursor, time)
        return
