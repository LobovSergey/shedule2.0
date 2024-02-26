from itertools import zip_longest
from lgc.logic.logic import distribution
from lgc.source.setup.setup_data import setup_settings
from lgc.source.wrap import chance_mistake


@chance_mistake
def search_answer():
    classes, teachers = setup_settings()
    cl, te = distribution(classes, teachers)
    return cl, te


def process():
    cl, te = search_answer()
    for i in cl:
        print(f"{i.group} остаток {i.lessons}")

    # for j in te:
    #     if j.descipline == "english":
    #         print(j.name)
    #         print(j.shedule)
