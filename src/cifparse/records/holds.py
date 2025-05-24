from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .hold.primary import Primary
from .hold.continuation import Continuation
from .hold.widths import w_pri, w_con

from sqlite3 import Cursor


class Hold(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, hold_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in hold_partition:
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

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        con = ", continuation: [...]" if self.continuation else ""
        return f"\n{self.__class__.__name__}{pri}{con}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "continuation": [item.to_dict() for item in self.continuation],
        }


class Holds:
    records: list[Hold]

    def __init__(self, hold_lines: list[str]):
        self.records = []

        print("    Parsing Holds")
        hold_partitioned = partition(hold_lines, 0, 38)
        for hold_partition in hold_partitioned:
            hold = Hold(hold_partition)
            self.records.append(hold)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing Holds")
        for hold in self.records:
            if hold.has_primary():
                primary.append(hold.primary)
            if hold.has_continuation():
                continuation.extend(hold.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
