from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .fir_uir.primary import Primary
from .fir_uir.continuation import Continuation
from .fir_uir.widths import w_pri, w_con

from sqlite3 import Cursor


class FIRUIR(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, fir_uir_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in fir_uir_partition:
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


class FIRUIRs:
    records: list[FIRUIR]

    def __init__(self, fir_uir_lines: list[str]):
        self.records = []

        print("    Parsing FIR UIRs")
        fir_uir_partitioned = partition(fir_uir_lines, 0, 19)
        for fir_uir_partition in fir_uir_partitioned:
            fir_uir = FIRUIR(fir_uir_partition)
            self.records.append(fir_uir)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing FIR UIRs")
        for fir_uir in self.records:
            if fir_uir.has_primary():
                primary.append(fir_uir.primary)
            if fir_uir.has_continuation():
                continuation.extend(fir_uir.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
