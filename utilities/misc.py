import time

def typewrite(func):
    def wrap():
        time.sleep(0.005)
        func()
        print('next line')

    return wrap