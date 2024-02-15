from dataclasses import dataclass, field


@dataclass
class Class:
    id: int = None
    group: str = None
    shedule: list[list] = field(default_factory=list)
    hours: int = 0
    rules: dict = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"{self.group}"

    def get_group(self):
        return self.group

    def get_shedule(self):
        return self.shedule
