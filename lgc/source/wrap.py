import time


def check_time(func):
    def wrapper():
        now = time.time()
        func()
        end = time.time()
        result = (end - now) * 1000
        print(result)

    return wrapper


def chance_mistake(func):
    def wrapper():
        ind = 0
        fault = 0
        while ind != 100:
            clasess, teachers = func()
            for i in clasess:
                if len(i.lessons) != 0:
                    fault += 1
                    break
            ind += 1
        print(f"Chance fault - {fault/ind * 100}%")
        return clasess, teachers

    return wrapper
