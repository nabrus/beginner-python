# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.

# An int being an object, has access to all attributes and methods using `.` (dot) syntax.
age = 6

print(age.real)  # 6
print(age.imag)  # 0
print(age.bit_length())  # 3
# Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:

# Examples of attributes and methods for lists
items = [1, "DW", 500]

items.append("lion")  # Adds 'lion' to the end of the list
items.pop()  # Removes and returns last item: 'lion'

print(id(items))  # 4443300736
# `id()` gives the address of the object in memory`
