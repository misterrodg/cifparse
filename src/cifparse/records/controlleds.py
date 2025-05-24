from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .appl_table import a_table
from .record_base import RecordBase
from .table_base import process_table

from .controlled.primary import Primary
from .controlled.time import Time
from .controlled.widths import w_pri, w_tim

from sqlite3 import Cursor


class Controlled(RecordBase):
    primary: Primary
    time: list[Time]

    def __init__(self, record_partitioned: list[str]):
        self.primary = None
        self.time = []

        for line in record_partitioned:
            cont_rec_no = extract_field(line, w_pri.cont_rec_no)
            if cont_rec_no in [0, 1]:
                primary = Primary()
                self.primary = primary.from_line(line)
                continue
            else:
                application = extract_field(line, w_tim.application)
                if application == a_table.time:
                    time = Time()
                    self.time.append(time.from_line(line))
                    continue

    def __repr__(self):
        pri = ": primary: {{...}}" if self.primary else ""
        tim = ", time: [...]" if self.time else ""
        return f"\n{self.__class__.__name__}{pri}{tim}"

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
            "time": [item.to_dict() for item in self.time],
        }


class Controlleds:
    records: list[Controlled]

    def __init__(self, controlled_lines: list[str]):
        self.records = []

        print("    Parsing Controlled Airspace")
        controlled_partitioned = partition(controlled_lines, 0, 24)
        for controlled_partition in controlled_partitioned:
            controlled = Controlled(controlled_partition)
            self.records.append(controlled)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []
        time = []

        print("    Processing Controlled Airspace")
        for controlled in self.records:
            if controlled.has_primary():
                primary.append(controlled.primary)
            if controlled.has_time():
                time.extend(controlled.time)

        if primary:
            process_table(db_cursor, primary)
            self._create_controlled_segments(db_cursor)
        if time:
            process_table(db_cursor, time)
        return

    def _create_controlleds_table(self, db_cursor: Cursor) -> None:
        table_name = "controlleds"
        drop_statement = f"DROP TABLE IF EXISTS {table_name};"
        db_cursor.execute(drop_statement)

        create_statement = f"CREATE TABLE {table_name} AS SELECT DISTINCT st, area, sec_code, sub_code, center_region, airspace_type, center_id, center_sec_code, center_sub_code, airspace_class, airspace_name FROM controlled_points WHERE airspace_name IS NOT NULL;"
        db_cursor.execute(create_statement)
        return

    def _create_controlled_segments(self, db_cursor: Cursor) -> None:
        table_name = "controlled_airspace_segments"
        drop_statement = f"DROP TABLE IF EXISTS {table_name};"
        db_cursor.execute(drop_statement)

        create_statement = f"CREATE TABLE {table_name} AS SELECT st, area, sec_code, sub_code, center_region, airspace_type, center_id, center_sec_code, center_sub_code, airspace_class, mult_code, lower_limit, lower_unit, upper_limit, upper_unit, airspace_name FROM controlled_points WHERE lower_limit IS NOT NULL OR upper_limit IS NOT NULL;"
        db_cursor.execute(create_statement)
        return
