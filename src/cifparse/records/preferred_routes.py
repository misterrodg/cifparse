from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .preferred_route.primary import Primary
from .preferred_route.continuation import Continuation
from .preferred_route.time import Time
from .preferred_route.widths import w_pri, w_con, w_tim

from sqlite3 import Cursor


class PreferredRoute(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    time: list[Time]

    def __init__(self, preferred_route_partition: list[str]):
        self.primary = None
        self.continuation = []
        self.time = []

        for line in preferred_route_partition:
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


class PreferredRoutes:
    records: list[PreferredRoute]

    def __init__(self, preferred_route_lines: list[str]):
        self.records = []

        print("    Parsing Preferred Routes")
        preferred_route_partitioned = partition(preferred_route_lines, 0, 38)
        for preferred_route_partition in preferred_route_partitioned:
            preferred_route = PreferredRoute(preferred_route_partition)
            self.records.append(preferred_route)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []
        time = []

        print("    Processing Preferred Routes")
        for preferred_route in self.records:
            if preferred_route.has_primary():
                primary.append(preferred_route.primary)
            if preferred_route.has_continuation():
                continuation.extend(preferred_route.continuation)
            if preferred_route.has_time():
                time.extend(preferred_route.time)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        if time:
            process_table(db_cursor, time)
        return
