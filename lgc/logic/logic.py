from random import randint
from lgc.cls.group import Group
from lgc.cls.teacher import Teacher
from lgc.source.data.constant import MAX_LESSONS


def distribution(classes: list[Group], teachers: list[Teacher]):
    for i in range(MAX_LESSONS):           
        for group in classes:
            print(group.lessons)
            lesson = group.lessons.pop(randint(0,len(group.lessons)))
            teachers_pool = list(filter(lambda x: group.group in x.class_pool and x.descipline == lesson, teachers))
            for teacher in teachers_pool:
                try:
                    teacher.shedule[i]
                    
                except IndexError:                    
                    try:                    
                        
                        group.shedule.append(lesson)
                        teacher.shedule.insert(i, group)
                        
                    except IndexError:
                        break
    return classes, teachers
                    
                    
        