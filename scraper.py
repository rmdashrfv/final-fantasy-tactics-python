from time import sleep

def greet(func):
    def wrap(n):
        print('Now you can decorate ... ')
        func(n)
        print('Anything in a decorator!')
    return wrap

@greet
def hola(n):
    print('yes' + n)

user = "Michael"

# hola(user)

# def typewrite(func):
#     def wrap(script):
        


script = '''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

'''

for line in list(script):
    print(line, end='')
    sleep(0.005)
