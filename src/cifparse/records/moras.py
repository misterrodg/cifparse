from .record_base import RecordBase
from .table_base import process_table

from .mora.primary import Primary

from sqlite3 import Cursor


class MORA(RecordBase):
    primary: Primary

    def __init__(self, mora_line: str):
        self.primary = None

        primary = Primary()
        self.primary = primary.from_line(mora_line)

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        return f"\n{self.__class__.__name__}{pri}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
        }


class MORAs:
    records: list[MORA]

    def __init__(self, mora_lines: list[str]):
        self.records = []

        print("    Parsing MORAs")
        for mora_line in mora_lines:
            mora = MORA(mora_line)
            self.records.append(mora)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []

        print("    Processing MORAs")
        for mora in self.records:
            if mora.has_primary():
                primary.append(mora.primary)

        if primary:
            process_table(db_cursor, primary)
        return
