from lgc.logic.logic import distribution
from lgc.source.setup.setup_data import setup_settings


def process():    
    classes, teachers = setup_settings()
    cl, te = distribution(classes=classes,teachers=teachers)
    for i in cl:
        print(i.group)
        print(i.shedule)
        print(len(i.shedule))
        
    for j in te:
        print(j.name)
        print(j.shedule)
        print(len(j.shedule))
        
    
