from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .runway.primary import Primary
from .runway.continuation import Continuation
from .runway.simulation import Simulation
from .runway.widths import w_pri, w_con, w_sim

from sqlite3 import Cursor


class Runway(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    simulation: list[Simulation]

    def __init__(self, runway_partitioned: list[str]):
        self.primary = None
        self.continuation = []
        self.simulation = []

        for line in runway_partitioned:
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


class Runways:
    records: list[Runway]

    def __init__(self, runway_lines: list[str]):
        self.records = []

        print("    Parsing Runways")
        runway_partitioned = partition(runway_lines, 0, 21)
        for runway_partition in runway_partitioned:
            runway = Runway(runway_partition)
            self.records.append(runway)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []
        simulation = []

        print("    Processing Runways")
        for runway in self.records:
            if runway.has_primary():
                primary.append(runway.primary)
            if runway.has_continuation():
                continuation.extend(runway.continuation)
            if runway.has_simulation():
                simulation.extend(runway.simulation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        if simulation:
            process_table(db_cursor, simulation)
        return
