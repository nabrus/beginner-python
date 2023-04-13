# Python is a dynamically-typed language which means that you don’t have to declare the data type of the variable beforehand.
# Annotations are Python features that hint developers about the data types of the variables or function parameters and return type.

# Specifying this func receives an integer and returns an integer
def increment(n: int) -> int:
    return n + 1


# Specify a variable is an integer
count: int = 0
