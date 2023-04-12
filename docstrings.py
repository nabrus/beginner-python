# Python uses docstrings to document code. A docstring is a string that is the first statement in a package, module, class or function. These strings can be extracted automatically through the __doc__ member of the object and are used by pydoc.

# Docstring used in function
def increment(n):
    """Increment a number"""
    return n + 1

# Docstring used in a Class


"""Dog Module

This module does...

-Dog

...
"""


class Dog:
    """A class representing a dog"""

    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age

    def bark():
        """Let the dog bark"""
        print("Woof! woof!")


# Using the `help` global function to get the documentation to get the documentation for a class, function, method, module.
print(help(Dog))
