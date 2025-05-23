from cifparse.functions.sql import translate_sql_types

from abc import ABC, abstractmethod

from sqlite3 import Cursor
from typing import get_type_hints


class TableBase(ABC):
    table_name: str

    def __init__(self, table_name: str):
        self.table_name = table_name

    @abstractmethod
    def ordered_fields(self) -> list:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    def get_fields(self, include_types: bool = False) -> list:
        fields = self.ordered_fields()
        if "table_name" in fields:
            fields.remove("table_name")
        if not include_types:
            return fields
        result = []
        hints = get_type_hints(self.__class__)
        for field in fields:
            if field in hints:
                result.append(
                    f"{field} {translate_sql_types(str(hints[field]).replace("<class '", "").replace("'>", ""))}"
                )
        return result

    def to_drop_statement(self) -> str:
        return f"DROP TABLE IF EXISTS {self.table_name};"

    def to_create_statement(self) -> str:
        fields = self.get_fields(True)
        field_string = ", ".join(fields)
        return f"CREATE TABLE {self.table_name} ({field_string});"

    def to_insert_statement(self) -> str:
        fields = self.get_fields()
        field_string = ", ".join(fields)
        placeholders = ", ".join([f":{item}" for item in fields])
        return (
            f"INSERT INTO {self.table_name} ({field_string}) VALUES ({placeholders});"
        )


def process_table(db_cursor: Cursor, record_list: list[TableBase]) -> None:
    first = record_list[0]
    drop_statement = first.to_drop_statement()
    db_cursor.execute(drop_statement)

    create_statement = first.to_create_statement()
    db_cursor.execute(create_statement)

    insert_statement = first.to_insert_statement()

    records = []
    for record in record_list:
        records.append(record.to_dict())

    db_cursor.executemany(insert_statement, records)
