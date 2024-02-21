from dataclasses import dataclass, field


@dataclass
class Teacher:
    id: int = 0
    name: str = None
    descipline: str = None
    shedule: list[list] = field(default_factory=list)
    hours: int = 0
    class_pool: list = field(default_factory=list)

    def __repr__(self) -> str:
        return f"{self.name} - {self.descipline}"

    def get_name(self):
        return self.name

    def get_shedule(self):
        return self.shedule

    def add_class_in_shedule(self, _class):
        self.shedule.append(_class)
