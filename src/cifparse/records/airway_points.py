from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .airway_point.primary import Primary
from .airway_point.continuation import Continuation
from .airway_point.planning import Planning
from .airway_point.planning_continuation import PlanningContinuation
from .airway_point.widths import w_pri, w_con, w_pla

from sqlite3 import Cursor


class AirwayPoint(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    planning: list[Planning]
    planning_continuation: list[PlanningContinuation]

    def __init__(self, airway_partitioned: list[str]):
        self.primary = None
        self.continuation = []
        self.planning = []
        self.planning_continuation = []

        was_last_planning = False
        for line in airway_partitioned:
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
                application = extract_field(line, w_pla.application)
                if application == a_table.planning:
                    planning = Planning()
                    self.planning.append(planning.from_line(line))
                    was_last_planning = True
                    continue
                if was_last_planning:
                    planning_continuation = PlanningContinuation()
                    self.planning_continuation = planning_continuation.from_line(line)
                    was_last_planning = False
                    continue

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        con = ", continuation: [...]" if self.continuation else ""
        pla = ", planning: [...]" if self.planning else ""
        plc = ", planning_continuation: [...]" if self.planning_continuation else ""
        return f"\n{self.__class__.__name__}{pri}{con}{pla}{plc}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "continuation": [item.to_dict() for item in self.continuation],
            "planning": [item.to_dict() for item in self.planning],
            "planning_continuation": [
                item.to_dict() for item in self.planning_continuation
            ],
        }


class AirwayPoints:
    records: list[AirwayPoint]

    def __init__(self, airway_lines: list[str]):
        self.records = []

        print("    Parsing Airway Points")
        airway_partitioned = partition(airway_lines, 0, 38)
        for airway_partition in airway_partitioned:
            airway = AirwayPoint(airway_partition)
            self.records.append(airway)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []
        planning = []
        planning_continuation = []

        print("    Processing Airway Points")
        for airway in self.records:
            if airway.has_primary():
                primary.append(airway.primary)
            if airway.has_continuation():
                continuation.extend(airway.continuation)
            if airway.has_planning():
                planning.extend(airway.planning)
            if airway.has_planning_continuation():
                planning_continuation.extend(airway.planning_continuation)

        if primary:
            process_table(db_cursor, primary)
            self._create_airways_table(db_cursor)
        if continuation:
            process_table(db_cursor, continuation)
        if planning:
            process_table(db_cursor, planning)
        if planning_continuation:
            process_table(db_cursor, planning_continuation)
        return

    def _create_airways_table(self, db_cursor: Cursor) -> None:
        table_name = "airways"
        drop_statement = f"DROP TABLE IF EXISTS {table_name};"
        db_cursor.execute(drop_statement)

        create_statement = f"CREATE TABLE {table_name} AS SELECT DISTINCT st, area, sec_code, sub_code, airway_id, six_char FROM airway_points;"
        db_cursor.execute(create_statement)
        return
