from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .heli_taa.primary import Primary
from .heli_taa.continuation import Continuation
from .heli_taa.widths import w_pri, w_con

from sqlite3 import Cursor


class HeliTAA(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, heli_taa_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in heli_taa_partition:
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


class HeliTAAs:
    records: list[HeliTAA]

    def __init__(self, heli_taa_lines: list[str]):
        self.records = []

        print("    Parsing Heli TAAs")
        heli_taa_partitioned = partition(heli_taa_lines, 0, 38)
        for heli_taa_partition in heli_taa_partitioned:
            heli_taa = HeliTAA(heli_taa_partition)
            self.records.append(heli_taa)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing Heli TAAs")
        for heli_taa in self.records:
            if heli_taa.has_primary():
                primary.append(heli_taa.primary)
            if heli_taa.has_continuation():
                continuation.extend(heli_taa.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
