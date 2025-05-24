from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .loc_gs.primary import Primary
from .loc_gs.continuation import Continuation
from .loc_gs.simulation import Simulation
from .loc_gs.widths import w_pri, w_con, w_sim

from sqlite3 import Cursor


class LOC_GS(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    simulation: list[Simulation]

    def __init__(self, loc_gs_partitioned: list[str]):
        self.primary = None
        self.continuation = []
        self.simulation = []

        for line in loc_gs_partitioned:
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
                application = extract_field(line, w_sim.application)
                if application == a_table.simulation:
                    simulation = Simulation()
                    self.simulation.append(simulation.from_line(line))
                    continue

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        con = ", continuation: [...]" if self.continuation else ""
        sim = ", simulation: [...]" if self.simulation else ""
        return f"\n{self.__class__.__name__}{pri}{con}{sim}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "continuation": [item.to_dict() for item in self.continuation],
            "simulation": [item.to_dict() for item in self.simulation],
        }


class LOC_GSs:
    records: list[LOC_GS]

    def __init__(self, loc_gs_lines: list[str]):
        self.records = []

        print("    Parsing LOC GS")
        loc_gs_partitioned = partition(loc_gs_lines, 0, 21)
        for loc_gs_partition in loc_gs_partitioned:
            loc_gs = LOC_GS(loc_gs_partition)
            self.records.append(loc_gs)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []
        simulation = []

        print("    Processing LOC GS")
        for loc_gs in self.records:
            if loc_gs.has_primary():
                primary.append(loc_gs.primary)
            if loc_gs.has_continuation():
                continuation.extend(loc_gs.continuation)
            if loc_gs.has_simulation():
                simulation.extend(loc_gs.simulation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        if simulation:
            process_table(db_cursor, simulation)
        return
