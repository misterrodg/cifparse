from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .path_point.primary import Primary
from .path_point.continuation import Continuation
from .path_point.widths import w_pri, w_con

from sqlite3 import Cursor


class PathPoint(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, path_point_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in path_point_partition:
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


class PathPoints:
    records: list[PathPoint]

    def __init__(self, path_point_lines: list[str]):
        self.records = []

        print("    Parsing Path Points")
        path_point_partitioned = partition(path_point_lines, 0, 26)
        for path_point_partition in path_point_partitioned:
            path_point = PathPoint(path_point_partition)
            self.records.append(path_point)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing Path Points")
        for navaid in self.records:
            if navaid.has_primary():
                primary.append(navaid.primary)
            if navaid.has_continuation():
                continuation.extend(navaid.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
