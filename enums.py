# Some programming languages, like Java and C++, include syntax that supports a data type known as enumerations, or just enums. This data type allows you to create sets of semantically related constants that you can access through the enumeration itself. Python doesn’t have a dedicated syntax for enums. However, the Python standard library has an enum module that supports enumerations through the Enum class.

# So Enums are the only real way to create constants in Python.
from enum import Enum


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE.value)  # 1
print(State(1))  # State.ACTIVE

# Listing all values
print(list(State))  # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
