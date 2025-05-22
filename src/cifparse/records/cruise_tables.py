from .record_base import RecordBase
from .table_base import process_table

from .cruise_table.primary import Primary

from sqlite3 import Cursor


class CruiseTable(RecordBase):
    primary: Primary

    def __init__(self, cruise_table_line: str):
        self.primary = None

        primary = Primary()
        self.primary = primary.from_line(cruise_table_line)

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        return f"\n{self.__class__.__name__}{pri}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
        }


class CruiseTables:
    records: list[CruiseTable]

    def __init__(self, cruise_table_lines: list[str]):
        self.records = []

        print("    Parsing Cruise Tables")
        for cruise_table_line in cruise_table_lines:
            cruise_table = CruiseTable(cruise_table_line)
            self.records.append(cruise_table)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []

        print("    Processing Cruise Tables")
        for cruise_table in self.records:
            if cruise_table.has_primary():
                primary.append(cruise_table.primary)

        if primary:
            process_table(db_cursor, primary)
        return
