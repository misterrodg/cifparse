from cifparse.functions.field import extract_field
from cifparse.functions.records import partition

from .rest_type_table import rt_table
from .restriction_base import RestrictionBase
from .table_base import process_table

from .airway_restriction.alt_exc_primary import AltExcPrimary
from .airway_restriction.alt_exc_continuation import AltExcContinuation
from .airway_restriction.cruise_primary import CruisePrimary
from .airway_restriction.cruise_continuation import CruiseContinuation
from .airway_restriction.closure_primary import ClosurePrimary
from .airway_restriction.note_primary import NotePrimary
from .airway_restriction.note_continuation import NoteContinuation
from .airway_restriction.widths import w_aex, w_cru, w_clo, w_not

from sqlite3 import Cursor


class AirwayRestriction(RestrictionBase):
    alt_exc_primary: AltExcPrimary
    alt_exc_continuation: list[AltExcContinuation]
    cruise_primary: CruisePrimary
    cruise_continuation: list[CruiseContinuation]
    closure_primary: ClosurePrimary
    # No Closure Continuations
    note_primary: NotePrimary
    note_continuation: list[NoteContinuation]

    def __init__(self, airway_restriction_partition: list[str]):
        self.alt_exc_primary = None
        self.alt_exc_continuation = []
        self.cruise_primary = None
        self.cruise_continuation = []
        self.closure_primary = None
        self.note_primary = None
        self.note_continuation = []

        for line in airway_restriction_partition:
            rest_type = extract_field(line, w_aex.rest_type)
            if rest_type == rt_table.altitude_exclusion:
                cont_rec_no = extract_field(line, w_aex.cont_rec_no)
                if cont_rec_no in [0, 1]:
                    alt_exc_primary = AltExcPrimary()
                    self.alt_exc_primary = alt_exc_primary.from_line(line)
                    continue
                else:
                    alt_exc_continuation = AltExcContinuation()
                    self.alt_exc_continuation = alt_exc_continuation.from_line(line)
                    continue
            if rest_type == rt_table.cruising_table:
                cont_rec_no = extract_field(line, w_cru.cont_rec_no)
                if cont_rec_no in [0, 1]:
                    cruise_primary = CruisePrimary()
                    self.cruise_primary = cruise_primary.from_line(line)
                    continue
                else:
                    cruise_continuation = CruiseContinuation()
                    self.cruise_continuation = cruise_continuation.from_line(line)
                    continue
            if rest_type == rt_table.seasonal_restriction:
                cont_rec_no = extract_field(line, w_clo.cont_rec_no)
                if cont_rec_no in [0, 1]:
                    closure_primary = ClosurePrimary()
                    self.closure_primary = closure_primary.from_line(line)
                    continue
            if rest_type == rt_table.note_restriction:
                cont_rec_no = extract_field(line, w_not.cont_rec_no)
                if cont_rec_no in [0, 1]:
                    note_primary = NotePrimary()
                    self.note_primary = note_primary.from_line(line)
                    continue
                else:
                    note_continuation = NoteContinuation()
                    self.note_continuation = note_continuation.from_line(line)
                    continue

    def __repr__(self):
        alt_pri = ": alt_exc_primary: {{...}}" if self.alt_exc_primary else ""
        alt_con = ", alt_exc_continuation: [...]" if self.alt_exc_continuation else ""
        cru_pri = ": cruise_primary: {{...}}" if self.cruise_primary else ""
        cru_con = ", cruise_continuation: [...]" if self.cruise_continuation else ""
        clo_pri = ": closure_primary: {{...}}" if self.closure_primary else ""
        not_pri = ": note_primary: {{...}}" if self.note_primary else ""
        not_con = ", note_continuation: [...]" if self.note_continuation else ""
        return f"\n{self.__class__.__name__}{alt_pri}{alt_con}{cru_pri}{cru_con}{clo_pri}{not_pri}{not_con}"

    def to_dict(self) -> dict:
        return {
            "alt_exc_primary": self.alt_exc_primary.to_dict(),
            "alt_exc_continuation": [
                item.to_dict() for item in self.alt_exc_continuation
            ],
            "cruise_primary": self.cruise_primary.to_dict(),
            "cruise_continuation": [
                item.to_dict() for item in self.cruise_continuation
            ],
            "closure_primary": self.closure_primary.to_dict(),
            "note_primary": self.note_primary.to_dict(),
            "note_continuation": [item.to_dict() for item in self.note_continuation],
        }


class AirwayRestrictions:
    records: list[AirwayRestriction]

    def __init__(self, airway_restriction_lines: list[str]):
        self.records = []

        print("    Parsing Airway Restrictions")
        airway_restriction_partitioned = partition(airway_restriction_lines, 0, 17)
        for airway_restriction_partition in airway_restriction_partitioned:
            airway_restriction = AirwayRestriction(airway_restriction_partition)
            self.records.append(airway_restriction)

    def to_dict(self) -> list[dict]:
        result = []
        for record in self.records:
            result.append(record.to_dict())
        return result

    def to_db(self, db_cursor: Cursor) -> None:
        alt_exc_primary = []
        alt_exc_continuation = []
        cruise_primary = []
        cruise_continuation = []
        closure_primary = []
        note_primary = []
        note_continuation = []

        print("    Processing Airway Restrictions")
        for airway_restriction in self.records:
            if airway_restriction.has_alt_exc_primary():
                alt_exc_primary.append(airway_restriction.alt_exc_primary)
            if airway_restriction.has_alt_exc_continuation():
                alt_exc_continuation.extend(airway_restriction.alt_exc_continuation)
            if airway_restriction.has_cruise_primary():
                cruise_primary.append(airway_restriction.cruise_primary)
            if airway_restriction.has_cruise_continuation():
                cruise_continuation.extend(airway_restriction.cruise_continuation)
            if airway_restriction.has_closure_primary():
                closure_primary.append(airway_restriction.closure_primary)
            if airway_restriction.has_note_primary():
                note_primary.append(airway_restriction.note_primary)
            if airway_restriction.has_note_continuation():
                note_continuation.extend(airway_restriction.note_continuation)

        if alt_exc_primary:
            process_table(db_cursor, alt_exc_primary)
        if alt_exc_continuation:
            process_table(db_cursor, alt_exc_continuation)
        if cruise_primary:
            process_table(db_cursor, cruise_primary)
        if cruise_continuation:
            process_table(db_cursor, cruise_continuation)
        if closure_primary:
            process_table(db_cursor, closure_primary)
        if note_primary:
            process_table(db_cursor, note_primary)
        if note_continuation:
            process_table(db_cursor, note_continuation)
        return
