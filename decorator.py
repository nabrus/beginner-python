# Decorators - change, enhance, or alter how a function works.
# In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on).
# A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

# Put simply: decorators wrap a function, modifying its behavior

# Python syntax: you to use decorators with the @ symbol, sometimes called the “pie” syntax.

def log_time(func):
    def wrapper():
        print("do something before")
        val = func()
        print("do something after")
        return val
    return wrapper


@log_time
def hello():
    print("Hello!")


hello()
# do something before
# Hello!
# do something after
