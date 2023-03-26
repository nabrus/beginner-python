# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Note-indentation is important. It creates the code blocks of functions. Number of spaces doesn't matter as long as it's consistent. 4 spaces is convention.

# Defining a function
def greeting():
    print("Hi, how are you today?")


# Calling the function
greeting()  # Hi, how are you today?

# Parameters


def personal_greeting(yourName):  # `yourName` is the parameter
    print(f"Hey {yourName}, what's up?")


personal_greeting('Wyatt')  # Hey Wyatt, what's up?
personal_greeting('Homer')  # Hey Homer, what's up?
# 'Wyatt' and 'Homer' are the arguments (args)

# Default parameters - Will be used if no args are given when running the function


def new_greeting(name="my friend"):  # 'my friend' is an optional arg
    print(f"Hey {name}, what's new?")


new_greeting("Marge")  # Hey Marge, what's new?
new_greeting()  # Hey my friend, what's new?

# Multiple parameters


def snake_maker(length, species="Python"):
    print(f"This snake is {length} ft. long, and is a {species}.")


snake_maker(4, "Cobra")  # This snake is 4 ft. long, and is a Cobra.
snake_maker(1, "Puff Adder")  # This snake is 1 ft. long, and is a Puff Adder.
snake_maker(5)  # This snake is 5 ft. long, and is a Python.

# Immutable objects in functions - ex ints


def change(value):
    value = 2


val = 1
change(val)

print(val)  # 1

# Mutable objects in functions - ex dicts


def changeVal(value):
    value["name"] = "Wyatt"


val_a = {"name": "Steve"}
changeVal(val_a)

print(val_a)  # {'name': 'Wyatt'}

# Returning values - function ends at `return` statements


def hello(name):
    if not name:
        return  # if arg provided is False, code ends
    print(f"Hello {name}, nice to see you!")


hello("Wyatt")  # Hello Wyatt, nice to see you!
hello(False)  # nothing is returned
hello("Jeffy!!!")  # Hello Jeffy!!!, nice to see you!

# Variable Scope

# Global variables
age = 1005  # Global scoped variable


def test():
    print(age)


print(age)  # 1005
test()  # 1005

# Local Variable


def test_2():
    dog = "husky"
    print(dog)


# print(dog)  # 'not defined' cannot be accessed outside the function
test_2()  # husky

# Nested Functions


def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)


talk("May the force be with you")
# Each word in this phrase will print on a new line

# Accessing variables in an outer funct from an inner funct


def count():
    count = 0

    def increment():
        nonlocal count  # declares `count`` non-local
        count = count + 1
        print(count)

    increment()


count()  # 1

# Closures
# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.


def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment  # returning the nested function `increment`


increment = counter()

print(increment())  # 1
print(increment())  # 2
print(increment())  # 3
print(increment())  # 4
# We return the inner increment function which still has access to `count` that is inside the counter function. even after it has ended.
