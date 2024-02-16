from random import shuffle
from lgc.cls.group import Group
from lgc.cls.setup.setup import SetSetting
from lgc.cls.teacher import Teacher


def prepare_data():
    setting = SetSetting()
    classes = setting.data_read(file_name="lgc/source/data/classes.json")
    teachers = setting.data_read(file_name="lgc/source/data/teachers.json")
    return classes, teachers


def class_data(classes, teachers):
    classes_class = [Group(id=group["id"],
                           group=f'{group["setting"]["class_grade"]}{group["group"]}',
                           hours=group["setting"]["hours"],
                           load=group["setting"]["load"],
                           class_teacher=group["class_teacher"]
                           ) for group in classes]
    teachers_class = [Teacher(id=teacher["id"],
                              name=teacher["info"]["name"],
                              descipline=teacher["info"]["discipline"],
                              hours=teacher["info"]["hours"],
                              class_pool=teacher["info"]["class_pool"]
                              ) for teacher in teachers]
    return classes_class, teachers_class


def setup_settings():
    classes, teachers = prepare_data()
    classes_class, teachers_class = class_data(
        classes=classes, teachers=teachers)
    for i in classes_class:
        i.prepare_lessons()
    shuffle(classes_class)
    shuffle(teachers_class)
    return classes_class, teachers_class
