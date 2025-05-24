from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .procedure.primary import Primary
from .procedure.continuation import Continuation
from .procedure.simulation import Simulation
from .procedure.planning import Planning
from .procedure.planning_continuation import PlanningContinuation
from .procedure.widths import w_pri, w_con, w_sim, w_pla

from sqlite3 import Cursor


class ProcedurePoint(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    simulation: list[Simulation]
    planning: list[Planning]
    planning_continuation: list[PlanningContinuation]

    def __init__(self, procedure_partition: list[str]):
        self.primary = None
        self.continuation = []
        self.simulation = []
        self.planning = []
        self.planning_continuation = []

        was_last_planning = False
        for line in procedure_partition:
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


class ProcedurePoints:
    records: list[ProcedurePoint]

    def __init__(self, planning_lines: list[str]):
        self.records = []

        print("    Parsing Procedure Points")
        procedure_partitioned = partition(planning_lines, 0, 38)
        for procedure_partition in procedure_partitioned:
            procedure = ProcedurePoint(procedure_partition)
            self.records.append(procedure)

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

        print("    Processing Procedure Points")
        for procedure in self.records:
            if procedure.has_primary():
                primary.append(procedure.primary)
            if procedure.has_continuation():
                continuation.extend(procedure.continuation)
            if procedure.has_simulation():
                simulation.extend(procedure.simulation)
            if procedure.has_planning():
                planning.extend(procedure.planning)
            if procedure.has_planning_continuation():
                planning_continuation.extend(procedure.planning_continuation)

        if primary:
            process_table(db_cursor, primary)
            self._create_procedures_table(db_cursor)
            self._create_procedure_segments_table(db_cursor)
        if continuation:
            process_table(db_cursor, continuation)
        if simulation:
            process_table(db_cursor, simulation)
        if planning:
            process_table(db_cursor, planning)
        if planning_continuation:
            process_table(db_cursor, planning_continuation)
        return

    def _create_procedures_table(self, db_cursor: Cursor) -> None:
        table_name = "procedures"
        drop_statement = f"DROP TABLE IF EXISTS {table_name};"
        db_cursor.execute(drop_statement)

        create_statement = f"CREATE TABLE {table_name} AS SELECT DISTINCT st, area, sec_code, fac_id, fac_region, fac_sub_code, procedure_id FROM procedure_points;"
        db_cursor.execute(create_statement)
        return

    def _create_procedure_segments_table(self, db_cursor: Cursor) -> None:
        table_name = "procedure_segments"
        drop_statement = f"DROP TABLE IF EXISTS {table_name};"
        db_cursor.execute(drop_statement)

        create_statement = f"CREATE TABLE {table_name} AS SELECT DISTINCT st, area, sec_code, fac_id, fac_region, fac_sub_code, procedure_id, procedure_type, transition_id FROM procedure_points;"
        db_cursor.execute(create_statement)
        return
