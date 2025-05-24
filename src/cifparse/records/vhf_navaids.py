from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .vhf_navaid.primary import Primary
from .vhf_navaid.continuation import Continuation
from .vhf_navaid.simulation import Simulation
from .vhf_navaid.planning import Planning
from .vhf_navaid.planning_continuation import PlanningContinuation
from .vhf_navaid.limitation import Limitation
from .vhf_navaid.widths import w_pri, w_con, w_sim, w_pla, w_lim

from sqlite3 import Cursor


class VHFNavaid(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    simulation: list[Simulation]
    planning: list[Planning]
    planning_continuation: list[PlanningContinuation]
    limitation: list[Limitation]

    def __init__(self, vhf_navaid_partition: list[str]):
        self.primary = None
        self.continuation = []
        self.simulation = []
        self.planning = []
        self.planning_continuation = []
        self.limitation = []

        was_last_planning = False
        for line in vhf_navaid_partition:
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
                application = extract_field(line, w_lim.application)
                if application == a_table.limitation:
                    limitation = Limitation()
                    self.limitation.append(limitation.from_line(line))
                    was_last_planning = False
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
        lim = ", limitation: [...]" if self.limitation else ""
        return f"\n{self.__class__.__name__}{pri}{con}{sim}{pla}{plc}{lim}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "continuation": [item.to_dict() for item in self.continuation],
            "simulation": [item.to_dict() for item in self.simulation],
            "planning": [item.to_dict() for item in self.planning],
            "planning_continuation": [
                item.to_dict() for item in self.planning_continuation
            ],
            "limitation": [item.to_dict() for item in self.limitation],
        }


class VHFNavaids:
    records: list[VHFNavaid]

    def __init__(self, vhf_navaid_lines: list[str]):
        self.records = []

        print("    Parsing VHF Navaids")
        vhf_navaid_partitioned = partition(vhf_navaid_lines, 0, 21)
        for vhf_navaid_partition in vhf_navaid_partitioned:
            vhf_navaid = VHFNavaid(vhf_navaid_partition)
            self.records.append(vhf_navaid)

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
        limitation = []

        print("    Processing VHF Navaids")
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
            if navaid.has_limitation():
                limitation.extend(navaid.limitation)

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
        if limitation:
            process_table(db_cursor, limitation)
        return
