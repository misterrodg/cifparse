from abc import ABC


class RestrictionBase(ABC):
    def has_alt_exc_primary(self) -> bool:
        return True if self.alt_exc_primary is not None else False

    def has_alt_exc_continuation(self) -> bool:
        return True if self.alt_exc_continuation is not None else False

    def has_note_primary(self) -> bool:
        return True if self.note_primary is not None else False

    def has_note_continuation(self) -> bool:
        return True if self.note_continuation is not None else False

    def has_closure_primary(self) -> bool:
        return True if self.closure_primary is not None else False

    def has_cruise_primary(self) -> bool:
        return True if self.cruise_primary is not None else False

    def has_cruise_continuation(self) -> bool:
        return True if self.cruise_continuation is not None else False
