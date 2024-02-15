

from lgc.cls.group import Group
from lgc.cls.setup.setup import SetSetting
from lgc.cls.teacher import Teacher


def prepare_data():
    setting = SetSetting()
    classes = setting.data_read(file_name="lgc/source/data/classes.json")
    teachers = setting.data_read(file_name="lgc/source/data/teachers.json")
    return classes, teachers


def class_data(classes, teachers):
    classes_class = [Group(id=group["id"], group=group["group"],
                           shedule=group["shedule"],
                           hours=group["hours"],
                           rules=group["rules"],
                           ) for group in classes]
    teachers_class = [Teacher(
        id=teacher["id"],
        name=teacher["id"],
        descipline=teacher["id"],
        shedule=teacher["id"],
        hours=teacher["id"],
    ) for teacher in teachers]
    return classes_class, teachers_class


def setup_settings():
    classes, teachers = prepare_data()
