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

hola(user)


'''

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