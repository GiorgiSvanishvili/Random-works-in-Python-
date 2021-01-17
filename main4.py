#Using Decorators
'''def null_decorator(func):
    return func


def greet():
    return 'Hello!'


greet = null_decorator(greet)'''


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'hello little gio!'

greet()


def mathematician(func):
    def calc():
        original_result = func()
        modified_result = original_result * 5 
        return modified_result
    return calc

@mathematician 
def multiply():
    return '50'

multiply()
