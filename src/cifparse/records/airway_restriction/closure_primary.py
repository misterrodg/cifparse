from .cruise_primary import CruisePrimary


class ClosurePrimary(CruisePrimary):
    def __init__(self):
        super().__init__("restriction_seasonals")

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.route_id}, {self.rest_id}"

    def from_line(self, line: str) -> "ClosurePrimary":
        super().from_line(line)
        return self

    def ordered_fields(self) -> list:
        return super().ordered_fields()

    def to_dict(self) -> dict:
        return super().to_dict()
