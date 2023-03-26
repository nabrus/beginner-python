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
