from .table_base import process_table

from .validity_record.primary import Primary

from sqlite3 import Cursor


class Validity:
    primary: Primary

    def __init__(self, cycle_id: str, valid_from: str, valid_to: str):
        primary = Primary(cycle_id, valid_from, valid_to)
        self.primary = primary

    def to_dict(self) -> dict:
        return {"primary": self.primary.to_dict()}

    def to_db(self, db_cursor: Cursor) -> None:
        process_table(db_cursor, [self.primary])
        return
