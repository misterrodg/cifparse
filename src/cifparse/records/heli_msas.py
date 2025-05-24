from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .heli_msa.primary import Primary
from .heli_msa.continuation import Continuation
from .heli_msa.widths import w_pri, w_con

from sqlite3 import Cursor


class HeliMSA(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, heli_msa_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in heli_msa_partition:
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


class HeliMSAs:
    records: list[HeliMSA]

    def __init__(self, heli_msa_lines: list[str]):
        self.records = []

        print("    Parsing Heli MSAs")
        heli_msa_partitioned = partition(heli_msa_lines, 0, 38)
        for heli_msa_partition in heli_msa_partitioned:
            heli_msa = HeliMSA(heli_msa_partition)
            self.records.append(heli_msa)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing Heli MSAs")
        for heli_msa in self.records:
            if heli_msa.has_primary():
                primary.append(heli_msa.primary)
            if heli_msa.has_continuation():
                continuation.extend(heli_msa.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
