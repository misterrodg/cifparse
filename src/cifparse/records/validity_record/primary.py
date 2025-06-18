from cifparse.records.table_base import TableBase


class Primary(TableBase):
    cycle_id: str
    valid_from: str
    valid_to: str

    def __init__(self, cycle_id: str, valid_from: str, valid_to: str):
        super().__init__("validity")
        self.cycle_id = cycle_id
        self.valid_from = valid_from
        self.valid_to = valid_to

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.cycle_id}, {self.valid_from}, {self.valid_to}"

    def ordered_fields(self) -> dict:
        return ["cycle_id", "valid_from", "valid_to"]

    def to_dict(self) -> dict:
        return {
            "cycle_id": self.cycle_id,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
        }
