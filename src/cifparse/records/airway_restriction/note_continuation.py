from cifparse.functions.field import extract_field

from .base import Base
from .widths import w_noc


class NoteContinuation(Base):
    cont_rec_no: int
    application: str
    notes: str

    def __init__(self):
        super().__init__("restriction_note_continuations")
        self.cont_rec_no = None
        self.application = None
        self.notes = None

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.route_id}, {self.rest_id}"

    def from_line(self, line: str) -> "NoteContinuation":
        super().from_line(line)
        self.cont_rec_no = extract_field(line, w_noc.cont_rec_no)
        self.application = extract_field(line, w_noc.application)
        self.notes = extract_field(line, w_noc.notes)
        return self

    def ordered_fields(self):
        result = []
        result.extend(super().ordered_leading())
        result.extend(
            [
                "cont_rec_no",
                "application",
                "notes",
            ]
        )
        result.extend(super().ordered_trailing())
        return result

    def to_dict(self) -> dict:
        leading_dict = super().get_leading_dict()
        trailing_dict = super().get_trailing_dict()
        this_dict = {
            "cont_rec_no": self.cont_rec_no,
            "application": self.application,
            "notes": self.notes,
        }
        return {**leading_dict, **this_dict, **trailing_dict}
