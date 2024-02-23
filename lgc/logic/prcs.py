from lgc.logic.logic import distribution
from lgc.source.setup.setup_data import setup_settings


def process():
    classes, teachers = setup_settings()
    cl, te = distribution(classes, teachers)
    for i in cl:
        if i.group in ["5a", "5b", "5c"]:
            print(i.group)
            print(i.shedule)
            print(i.lessons)
            print(len(i.shedule))

    # for j in te:
    #     if j.descipline == "english":
    #         print(j.name)
    #         print(j.shedule)
