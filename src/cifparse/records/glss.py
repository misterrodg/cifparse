from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .gls.primary import Primary
from .gls.continuation import Continuation
from .gls.widths import w_pri, w_con

from sqlite3 import Cursor


class GLS(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, gls_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in gls_partition:
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


class GLSs:
    records: list[GLS]

    def __init__(self, gls_lines: list[str]):
        self.records = []

        print("    Parsing GLSs")
        gls_partitioned = partition(gls_lines, 0, 21)
        for gls_partition in gls_partitioned:
            gls = GLS(gls_partition)
            self.records.append(gls)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing GLSs")
        for gls in self.records:
            if gls.has_primary():
                primary.append(gls.primary)
            if gls.has_continuation():
                continuation.extend(gls.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
