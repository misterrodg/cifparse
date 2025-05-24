from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .waypoint.primary import Primary
from .waypoint.continuation import Continuation
from .waypoint.planning import Planning
from .waypoint.planning_continuation import PlanningContinuation
from .waypoint.widths import w_pri, w_con, w_pla

from sqlite3 import Cursor


class Waypoint(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    planning: list[Planning]
    planning_continuation: list[PlanningContinuation]
    is_terminal: bool

    def __init__(self, waypoint_partition: list[str], is_terminal: bool = False):
        self.primary = None
        self.continuation = []
        self.planning = []
        self.planning_continuation = []
        self.is_terminal = is_terminal

        was_last_planning = False
        for line in waypoint_partition:
            cont_rec_no = extract_field(line, w_pri.cont_rec_no)
            if cont_rec_no in [0, 1]:
                primary = Primary(self.is_terminal)
                self.primary = primary.from_line(line)
                was_last_planning = False
                continue
            else:
                application = extract_field(line, w_con.application)
                if application == a_table.standard:
                    continuation = Continuation(self.is_terminal)
                    self.continuation.append(continuation.from_line(line))
                    was_last_planning = False
                    continue
                application = extract_field(line, w_pla.application)
                if application == a_table.planning:
                    planning = Planning(self.is_terminal)
                    self.planning.append(planning.from_line(line))
                    was_last_planning = True
                    continue
                if was_last_planning:
                    planning_continuation = PlanningContinuation(self.is_terminal)
                    self.planning_continuation.append(
                        planning_continuation.from_line(line)
                    )
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


class Waypoints:
    records: list[Waypoint]
    is_terminal: bool

    def __init__(self, waypoint_lines: list[str], is_terminal: bool = False):
        self.records = []
        self.is_terminal = is_terminal

        print(f"    Parsing {"Terminal " if self.is_terminal else ""}Waypoints")
        waypoint_partitioned = partition(waypoint_lines, 0, 21)
        for waypoint_partition in waypoint_partitioned:
            waypoint = Waypoint(waypoint_partition, self.is_terminal)
            self.records.append(waypoint)

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

        print(f"    Processing {"Terminal " if self.is_terminal else ""}Waypoints")
        for waypoint in self.records:
            if waypoint.has_primary():
                primary.append(waypoint.primary)
            if waypoint.has_continuation():
                continuation.extend(waypoint.continuation)
            if waypoint.has_planning():
                planning.extend(waypoint.planning)
            if waypoint.has_planning_continuation():
                planning_continuation.extend(waypoint.planning_continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        if planning:
            process_table(db_cursor, planning)
        if planning_continuation:
            process_table(db_cursor, planning_continuation)
        return
