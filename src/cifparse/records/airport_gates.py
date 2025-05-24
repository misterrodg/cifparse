from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .airport_gate.primary import Primary
from .airport_gate.continuation import Continuation
from .airport_gate.widths import w_pri, w_con

from sqlite3 import Cursor


class Gate(RecordBase):
    primary: Primary
    continuation: list[Continuation]

    def __init__(self, gate_partition: list[str]):
        self.primary = None
        self.continuation = []

        for line in gate_partition:
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


class Gates:
    records: list[Gate]

    def __init__(self, gate_lines: list[str]):
        self.records = []

        print("    Parsing Gates")
        gate_partitioned = partition(gate_lines, 0, 21)
        for gate_partition in gate_partitioned:
            gate = Gate(gate_partition)
            self.records.append(gate)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []

        print("    Processing Gates")
        for gate in self.records:
            if gate.has_primary():
                primary.append(gate.primary)
            if gate.has_continuation():
                continuation.extend(gate.continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        return
