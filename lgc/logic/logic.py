from random import randint, shuffle
from lgc.cls.group import Group
from lgc.cls.teacher import Teacher
from lgc.cls.window import Window
from lgc.source.data.constant import MAX_LESSONS


def add_window(shedule: list, index):
    while len(shedule) != index:
        shedule.append(None)


def distribution(classes: list[Group], teachers: list[Teacher]):
    for i in range(MAX_LESSONS):
        window = Window(i)
        for teacher in teachers:
            shuffle(classes)
            flag = False
            index_group = 0
            while index_group < len(classes):
                current_class = classes[index_group]
                if teacher.descipline in current_class.lessons and current_class.group in teacher.class_pool and current_class not in window.pool:
                    index = current_class.find_index_by_lesson(
                        teacher.descipline)
                    lesson = current_class.remove_lesson(index)
                    ########
                    teacher.add_class_in_shedule(current_class)
                    window.add_pool(current_class)
                    current_class.add_lesson_in_shedule(lesson)
                    flag = True
                    break
                index_group += 1
            if not flag and index_group == len(classes):
                teacher.add_class_in_shedule("__")
    return classes, teachers
