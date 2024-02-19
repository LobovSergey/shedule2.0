from lgc.logic.logic import distribution
from lgc.source.setup.setup_data import setup_settings


def process():
    classes, teachers = setup_settings()
    cl, te = distribution(classes=classes, teachers=teachers)
    for i in cl:
        print(i.group)
        print(i.shedule)
        print(len(i.shedule))

    # jk = filter(lambda x: len(tuple(x.shedule)) >=
    #             1 and tuple(x.shedule)[0] is not None, te)

    for j in te:
        print(j.name)
        print(j.shedule[:len(classes[0].shedule)])
        print(len(j.shedule))
