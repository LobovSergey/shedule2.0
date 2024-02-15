import time


def check_time(func):
    def wrapper():
        now = time.time()
        func()
        end = time.time()
        result = (end - now) * 1000
        print(result)
    return wrapper
