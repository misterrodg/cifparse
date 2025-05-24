from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .restrictive.primary import Primary
from .restrictive.continuation import Continuation
from .restrictive.time import Time
from .restrictive.widths import w_pri, w_con, w_tim

from sqlite3 import Cursor


class Restrictive(RecordBase):
    primary: Primary
    continuation: list[Continuation]
    time: list[Time]

    def __init__(self, record_partitioned: list[str]):
        self.primary = None
        self.continuation = []
        self.time = []

        for line in record_partitioned:
            cont_rec_no = extract_field(line, w_pri.cont_rec_no)
            if cont_rec_no in [0, 1]:
                primary = Primary()
                self.primary = primary.from_line(line)
                continue
            else:
                application = extract_field(line, w_con.application)
                if application == a_table.standard:
                    continuation = Continuation()
                    self.continuation.append(continuation.from_line(line))
                    continue
                application = extract_field(line, w_tim.application)
                if application == a_table.time:
                    time = Time()
                    self.time.append(time.from_line(line))
                    continue

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        con = ", continuation: [...]" if self.continuation else ""
        tim = ", time: [...]" if self.time else ""
        return f"\n{self.__class__.__name__}{pri}{con}{tim}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "continuation": [item.to_dict() for item in self.continuation],
            "time": [item.to_dict() for item in self.time],
        }


class Restrictives:
    records: list[Restrictive]

    def __init__(self, restrictive_lines: list[str]):
        self.records = []

        print("    Parsing Restrictive Airspace")
        restrictive_partitioned = partition(restrictive_lines, 0, 24)
        for restrictive_partition in restrictive_partitioned:
            restrictive = Restrictive(restrictive_partition)
            self.records.append(restrictive)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        continuation = []
        time = []

        print("    Processing Restrictive Airspace")
        for restrictive in self.records:
            if restrictive.has_primary():
                primary.append(restrictive.primary)
            if restrictive.has_continuation():
                continuation.extend(restrictive.continuation)
            if restrictive.has_time():
                time.extend(restrictive.time)

        if primary:
            process_table(db_cursor, primary)
            self._create_restrictive_segments_table(db_cursor)
        if continuation:
            process_table(db_cursor, continuation)
        if time:
            process_table(db_cursor, time)
        return

    def _create_restrictives_table(self, db_cursor: Cursor) -> None:
        table_name = "restrictives"
        drop_statement = f"DROP TABLE IF EXISTS {table_name};"
        db_cursor.execute(drop_statement)

        create_statement = f"CREATE TABLE {table_name} AS SELECT DISTINCT st, area, sec_code, sub_code, region, restrictive_type, restrictive_id, restrictive_name FROM restrictive_points WHERE restrictive_name IS NOT NULL;"
        db_cursor.execute(create_statement)
        return

    def _create_restrictive_segments_table(self, db_cursor: Cursor) -> None:
        table_name = "restrictive_segments"
        drop_statement = f"DROP TABLE IF EXISTS {table_name};"
        db_cursor.execute(drop_statement)

        create_statement = f"CREATE TABLE {table_name} AS SELECT st, area, sec_code, sub_code, restrictive_id, mult_code, lower_limit, lower_unit, upper_limit, upper_unit, restrictive_name FROM restrictive_points WHERE lower_limit IS NOT NULL OR upper_limit IS NOT NULL;"
        db_cursor.execute(create_statement)
        return
