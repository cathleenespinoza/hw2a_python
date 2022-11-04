import time

def timeme(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        X = end - start
        print('Total time', X)
    return inner

#@timeme
#def test():
#    time.sleep(2)

#test()