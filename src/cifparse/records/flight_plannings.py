from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .flight_planning.primary import Primary
from .flight_planning.continuation import Continuation
from .flight_planning.time import Time
from .flight_planning.widths import w_pri, w_con, w_tim

from sqlite3 import Cursor


class FlightPlanning(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    time: list[Time]

    def __init__(self, flight_planning_partition: list[str]):
        self.primary = None
        self.continuation = []
        self.time = []

        for line in flight_planning_partition:
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


class FlightPlannings:
    records: list[FlightPlanning]

    def __init__(self, flight_planning_lines: list[str]):
        self.records = []

        print("    Parsing Flight Plannings")
        flight_planning_partitioned = partition(flight_planning_lines, 0, 69)
        for flight_planning_partition in flight_planning_partitioned:
            flight_planning = FlightPlanning(flight_planning_partition)
            self.records.append(flight_planning)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []
        time = []

        print("    Processing Flight Plannings")
        for flight_planning in self.records:
            if flight_planning.has_primary():
                primary.append(flight_planning.primary)
            if flight_planning.has_continuation():
                continuation.extend(flight_planning.continuation)
            if flight_planning.has_time():
                time.extend(flight_planning.time)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        if time:
            process_table(db_cursor, time)
        return
