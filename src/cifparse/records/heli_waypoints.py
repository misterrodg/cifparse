from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .heli_waypoint.primary import Primary
from .heli_waypoint.continuation import Continuation
from .heli_waypoint.planning import Planning
from .heli_waypoint.planning_continuation import PlanningContinuation
from .heli_waypoint.widths import w_pri, w_con, w_pla

from sqlite3 import Cursor


class HeliWaypoint(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    planning: list[Planning]
    planning_continuation: list[PlanningContinuation]
    is_terminal: bool

    def __init__(self, heli_waypoint_partition: list[str]):
        self.primary = None
        self.continuation = []
        self.planning = []
        self.planning_continuation = []

        was_last_planning = False
        for line in heli_waypoint_partition:
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


class HeliWaypoints:
    records: list[HeliWaypoint]
    is_terminal: bool

    def __init__(self, heli_waypoint_lines: list[str]):
        self.records = []

        print(f"    Parsing Heli Terminal Waypoints")
        heli_waypoint_partitioned = partition(heli_waypoint_lines, 0, 21)
        for heli_waypoint_partition in heli_waypoint_partitioned:
            heli_waypoint = HeliWaypoint(
                heli_waypoint_partition,
            )
            self.records.append(heli_waypoint)

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

        print(f"    Processing Heli Terminal Waypoints")
        for heli_waypoint in self.records:
            if heli_waypoint.has_primary():
                primary.append(heli_waypoint.primary)
            if heli_waypoint.has_continuation():
                continuation.extend(heli_waypoint.continuation)
            if heli_waypoint.has_planning():
                planning.extend(heli_waypoint.planning)
            if heli_waypoint.has_planning_continuation():
                planning_continuation.extend(heli_waypoint.planning_continuation)

        if primary:
            process_table(db_cursor, primary)
        if continuation:
            process_table(db_cursor, continuation)
        if planning:
            process_table(db_cursor, planning)
        if planning_continuation:
            process_table(db_cursor, planning_continuation)
        return
