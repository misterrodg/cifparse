from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .terminal_marker.primary import Primary
from .terminal_marker.continuation import Continuation
from .terminal_marker.widths import w_pri, w_con

from sqlite3 import Cursor


class TerminalMarker(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, marker_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in marker_partition:
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


class TerminalMarkers:
    records: list[TerminalMarker]

    def __init__(self, marker_lines: list[str]):
        self.records = []

        print("    Parsing Terminal Markers")
        marker_partitioned = partition(marker_lines, 0, 21)
        for marker_partition in marker_partitioned:
            marker = TerminalMarker(marker_partition)
            self.records.append(marker)

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing Terminal Markers")
        for marker in self.records:
            if marker.has_primary():
                primary.append(marker.primary)
            if marker.has_continuation():
                continuation.extend(marker.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
