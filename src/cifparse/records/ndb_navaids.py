from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .ndb_navaid.primary import Primary
from .ndb_navaid.continuation import Continuation
from .ndb_navaid.simulation import Simulation
from .ndb_navaid.planning import Planning
from .ndb_navaid.planning_continuation import PlanningContinuation
from .ndb_navaid.widths import w_pri, w_con, w_sim, w_pla

from sqlite3 import Cursor


class NDBNavaid(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    simulation: list[Simulation]
    planning: list[Planning]
    planning_continuation: list[PlanningContinuation]

    def __init__(self, ndb_partition: list[str]):
        self.primary = None
        self.continuation = []
        self.simulation = []
        self.planning = []
        self.planning_continuation = []

        was_last_planning = False
        for line in ndb_partition:
            cont_rec_no = extract_field(line, w_pri.cont_rec_no)
            if cont_rec_no in [0, 1]:
                primary = Primary()
                self.primary = primary.from_line(line)
                was_last_planning = False
                continue
            else:
                application = extract_field(line, w_con.application)
                if application == a_table.standard:
                    continuation = Continuation()
                    self.continuation.append(continuation.from_line(line))
                    was_last_planning = False
                    continue
                application = extract_field(line, w_sim.application)
                if application == a_table.simulation:
                    simulation = Simulation()
                    self.simulation.append(simulation.from_line(line))
                    was_last_planning = False
                    continue
                application = extract_field(line, w_pla.application)
                if application == a_table.planning:
                    planning = Planning()
                    self.planning.append(planning.from_line(line))
                    was_last_planning = True
                    continue
                if was_last_planning:
                    planning_continuation = PlanningContinuation()
                    self.planning_continuation.append(
                        planning_continuation.from_line(line)
                    )
                    was_last_planning = False
                    continue

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        con = ", continuation: [...]" if self.continuation else ""
        sim = ", simulation: [...]" if self.simulation else ""
        pla = ", planning: [...]" if self.planning else ""
        plc = ", planning_continuation: [...]" if self.planning_continuation else ""
        return f"\n{self.__class__.__name__}{pri}{con}{sim}{pla}{plc}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "continuation": [item.to_dict() for item in self.continuation],
            "simulation": [item.to_dict() for item in self.simulation],
            "planning": [item.to_dict() for item in self.planning],
            "planning_continuation": [
                item.to_dict() for item in self.planning_continuation
            ],
        }


class NDBNavaids:
    records: list[NDBNavaid]

    def __init__(self, ndb_navaid_lines: list[str]):
        self.records = []

        print("    Parsing NDB Navaids")
        ndb_navaid_partitioned = partition(ndb_navaid_lines, 0, 21)
        for ndb_navaid_partition in ndb_navaid_partitioned:
            ndb_navaid = NDBNavaid(ndb_navaid_partition)
            self.records.append(ndb_navaid)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []
        simulation = []
        planning = []
        planning_continuation = []

        print("    Processing NDB Navaids")
        for navaid in self.records:
            if navaid.has_primary():
                primary.append(navaid.primary)
            if navaid.has_continuation():
                continuation.extend(navaid.continuation)
            if navaid.has_simulation():
                simulation.extend(navaid.simulation)
            if navaid.has_planning():
                planning.extend(navaid.planning)
            if navaid.has_planning_continuation():
                planning_continuation.extend(navaid.planning_continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        if simulation:
            process_table(db_cursor, simulation)
        if planning:
            process_table(db_cursor, planning)
        if planning_continuation:
            process_table(db_cursor, planning_continuation)
        return
