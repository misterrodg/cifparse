from .record_base import RecordBase
from .table_base import process_table

from .company_route.primary import Primary

from sqlite3 import Cursor


class CompanyRoute(RecordBase):
    primary: Primary

    def __init__(self, company_route_line: str):
        self.primary = None

        primary = Primary()
        self.primary = primary.from_line(company_route_line)

    def to_dict(self) -> dict:
        return {
            "primary": self.primary.to_dict(),
        }


class CompanyRoutes:
    records: list[CompanyRoute]

    def __init__(self, company_route_lines: list[str]):
        self.records = []

        print("    Parsing Company Routes")
        for company_route_line in company_route_lines:
            company_route = CompanyRoute(company_route_line)
            self.records.append(company_route)

    def get_company_route_by_origin(self, origin_id: str) -> CompanyRoute:
        result = []
        for record in self.records:
            if record.has_primary() and record.primary.from_1 == origin_id:
                result.append(record)
        return

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        primary = []

        print("    Processing Company Routes")
        for company_route in self.records:
            if company_route.has_primary():
                primary.append(company_route.primary)

        if primary:
            process_table(db_cursor, primary)
        return
