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
    for i in range(MAX_LESSONS):
        for group in classes:
            if not check_window(i, group):
                continue
            try:
                lesson = group.lessons.pop(0)

            except IndexError:
                lesson = None

            teachers_pool = list(filter(
                lambda x: group.group in x.class_pool and x.descipline == lesson, teachers))
            for teacher in teachers_pool:
                if lesson == teacher.descipline:
                    try:
                        teacher.shedule[i]

                    except IndexError:
                        if i - len(teacher.shedule) > 0:
                            add_window(shedule=teacher.shedule, index=i)
                        group.shedule.append(lesson)
                        teacher.shedule.insert(i, group)
                        break

                    #

                    #     finally:
                    #         break
    return classes, teachers
