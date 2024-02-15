from dataclasses import dataclass, field


@dataclass
class Teacher:
    name: str = None
    descipline: str = None
    shedule: list[list] = field(default_factory=list)
    hours: int = 0

    def __repr__(self) -> str:
        return f"{self.name} - {self.descipline}"

    def get_name(self):
        return self.name

    def get_shedule(self):
        return self.shedule
