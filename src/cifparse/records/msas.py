from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .msa.primary import Primary
from .msa.continuation import Continuation
from .msa.widths import w_pri, w_con

from sqlite3 import Cursor


class MSA(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, msa_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in msa_partition:
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


class MSAs:
    records: list[MSA]

    def __init__(self, msa_lines: list[str]):
        self.records = []

        print("    Parsing MSAs")
        msa_partitioned = partition(msa_lines, 6, 23)
        for msa_partition in msa_partitioned:
            msa = MSA(msa_partition)
            self.records.append(msa)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing MSAs")
        for msa in self.records:
            if msa.has_primary():
                primary.append(msa.primary)
            if msa.has_continuation():
                continuation.extend(msa.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
