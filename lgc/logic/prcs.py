from itertools import zip_longest
from lgc.logic.logic import distribution
from lgc.source.setup.setup_data import setup_settings


def search_answer():
    classes, teachers = setup_settings()
    cl, te = distribution(classes, teachers)
    return cl, te


def process():
    cl, te = search_answer()
    for i in cl:
        if i.group in ["5a", "5b", "5c"]:
            print(i.group)
            print(i.lessons)
            print(len(i.shedule))

    # for j in te:
    #     if j.descipline == "english":
    #         print(j.name)
    #         print(j.shedule)
