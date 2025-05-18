from abc import ABC


class RecordBase(ABC):
    def has_primary(self) -> bool:
        return True if self.primary is not None else False

    def has_continuation(self) -> bool:
        return True if self.continuation is not None else False

    def has_combined(self) -> bool:
        return True if self.combined is not None else False

    def has_callsign(self) -> bool:
        return True if self.callsign is not None else False

    def has_extension(self) -> bool:
        return True if self.extension is not None else False

    def has_limitation(self) -> bool:
        return True if self.limitation is not None else False

    def has_narrative(self) -> bool:
        return True if self.narrative is not None else False

    def has_time(self) -> bool:
        return True if self.time is not None else False

    def has_nar_time(self) -> bool:
        return True if self.nar_time is not None else False

    def has_se_time(self) -> bool:
        return True if self.se_time is not None else False

    def has_planning(self) -> bool:
        return True if self.planning is not None else False

    def has_planning_continuation(self) -> bool:
        return True if self.planning_continuation is not None else False

    def has_simulation(self) -> bool:
        return True if self.simulation is not None else False

    def has_procedure(self) -> bool:
        return True if self.procedure is not None else False
