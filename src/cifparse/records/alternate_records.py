from .record_base import RecordBase
from .table_base import process_table

from .alternate_record.primary import Primary

from sqlite3 import Cursor


class AlternateRecord(RecordBase):
    primary: Primary

    def __init__(self, alternate_record_line: str):
        self.primary = None

        primary = Primary()
        self.primary = primary.from_line(alternate_record_line)

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        return f"\n{self.__class__.__name__}{pri}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
        }


class AlternateRecords:
    records: list[AlternateRecord]

    def __init__(self, alternate_record_lines: list[str]):
        self.records = []

        print("    Parsing Alternate Records")
        for alternate_record_line in alternate_record_lines:
            alternate_record = AlternateRecord(alternate_record_line)
            self.records.append(alternate_record)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []

        print("    Processing Alternate Records")
        for alternate_record in self.records:
            if alternate_record.has_primary():
                primary.append(alternate_record.primary)

        if primary:
            process_table(db_cursor, primary)
        return
