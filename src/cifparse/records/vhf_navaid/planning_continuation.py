from .primary import Primary


class PlanningContinuation(Primary):
    def __init__(self):
        super().__init__("vhf_planning_continuations")

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.vhf_id}"

    def from_line(self, line: str) -> "PlanningContinuation":
        super().from_line(line)
        return self

    def ordered_fields(self) -> list:
        return super().ordered_fields()

    def to_dict(self) -> dict:
        return super().to_dict()
