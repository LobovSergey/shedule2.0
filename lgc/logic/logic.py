from random import randint, shuffle
from lgc.cls.group import Group
from lgc.cls.teacher import Teacher
from lgc.cls.window import Window
from lgc.source.data.constant import MAX_LESSONS


def check_conditions() -> bool:
    pass


def formatting_lessons(current_class: Group, teacher: Teacher, window: Window, special_teachers: list[Teacher]):
    descipline = teacher.descipline
    index = current_class.find_index_by_lesson(descipline)
    lesson = current_class.remove_lesson(index)
    if teacher in special_teachers and current_class.group in teacher.groups:
        group_teachers = list(filter(
            lambda t: current_class.group in t.groups, special_teachers))
        # skip = [group_teachers[i] for i in range(1, len(group_teachers))]
        list(map(lambda t: t.add_class_in_shedule(current_class), group_teachers))
    else:
        teacher.add_class_in_shedule(current_class)
    current_class.add_lesson_in_shedule(lesson)
    window.add_pool(current_class)
    # return skip


def distribution(classes: list[Group], teachers: list[Teacher]):
    special_teachers = list(filter(lambda teach: teach.special, teachers))
    for i in range(MAX_LESSONS):
        skipped_teachers = []
        window = Window(i)
        for teacher in teachers:
            if teacher in skipped_teachers:
                break
            shuffle(classes)
            flag = False
            index_group = 0
            while index_group < len(classes):
                current_class = classes[index_group]
                if teacher.descipline in current_class.lessons and current_class.group in teacher.class_pool and current_class not in window.pool:
                    formatting_lessons(
                        current_class=current_class, teacher=teacher, window=window, special_teachers=special_teachers, skip=skipped_teachers)
                    flag = True
                    break
                index_group += 1
            # if check_conditions():
            if not flag and index_group == len(classes):
                teacher.add_class_in_shedule("__")
    return classes, teachers
