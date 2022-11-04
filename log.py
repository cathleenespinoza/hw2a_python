
import time
def timestamp(func):
    def inner():
        current_time = time.ctime()
        print(current_time)
        func()
    return inner
