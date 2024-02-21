from dataclasses import dataclass, field
from random import shuffle

from lgc.cls.teacher import Teacher


@dataclass
class Group:
    id: int = None
    group: str = None
    shedule: list[list] = field(default_factory=list)
    hours: int = 0
    load: dict = field(default_factory=dict)
    lessons: list = field(default_factory=list)
    class_teacher: str = None

    def __repr__(self) -> str:
        return f"{self.group}"

    def get_group(self):
        return self.group

    def get_shedule(self):
        return self.shedule

    def prepare_lessons(self):
        self.lessons = [key for key, value in self.load.items()
                        for _ in range(value)]
        shuffle(self.lessons)

    def add_lesson_in_shedule(self, lesson):
        self.shedule.append(lesson)

    def remove_lesson(self, index):
        return self.lessons.pop(index)

    def find_index_by_lesson(self, discepline):
        return self.lessons.index(discepline)
