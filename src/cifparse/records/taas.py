from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .taa.primary import Primary
from .taa.continuation import Continuation
from .taa.widths import w_pri, w_con

from sqlite3 import Cursor


class TAA(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, taa_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in taa_partition:
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


class TAAs:
    records: list[TAA]

    def __init__(self, taa_lines: list[str]):
        self.records = []

        print("    Parsing TAAs")
        taa_partitioned = partition(taa_lines, 0, 38)
        for taa_partition in taa_partitioned:
            taa = TAA(taa_partition)
            self.records.append(taa)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing TAAs")
        for taa in self.records:
            if taa.has_primary():
                primary.append(taa.primary)
            if taa.has_continuation():
                continuation.extend(taa.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
