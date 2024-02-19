from random import randint
from lgc.cls.group import Group
from lgc.cls.teacher import Teacher
from lgc.source.data.constant import MAX_LESSONS


def check_window(index: int, group: Group):
    if index >= group.hours:
        return False
    return True


def add_window(shedule: list, index):
    while len(shedule) != index:
        shedule.append(None)


def distribution(classes: list[Group], teachers: list[Teacher]):
    for _ in range(MAX_LESSONS):
        pool = []
        for teacher in teachers:
            flag = False
            index_group = 0
            while index_group < len(classes):
                current_class = classes[index_group]
                if teacher.descipline in current_class.lessons and current_class.group in teacher.class_pool and current_class not in pool:
                    index = current_class.lessons.index(teacher.descipline)
                    lesson = current_class.lessons.pop(index)
                    teacher.shedule.append(current_class)
                    pool.append(current_class)
                    current_class.shedule.append(lesson)
                    flag = True
                    break
                index_group += 1
            if not flag and index_group == len(classes):
                teacher.shedule.append("__")
    return classes, teachers
