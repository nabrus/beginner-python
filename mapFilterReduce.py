# Global functions - map(), filter(), reduce()

# The `map()` function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# Syntax: map(function, iterables)
from functools import reduce
# See reduce() examples below
numbers = [1, 2, 3]


def double(a):
    return a * 2


result = map(double, numbers)

print(list(result))  # [2, 4, 6]

# Use `lambda` function

numbers_2 = [4, 5, 6]
# Note: Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier. per PEP8 style guide

# double_2 = lambda a: a * 2
# result_2 = map(double_2, numbers_2)
# print(list(result_2))  # [8, 10, 12]

# Acceptable way of using lambda
numbers_3 = [7, 8, 9]
result_3 = map(lambda a: a * 2, numbers_3)
print(list(result_3))  # [14, 16, 18]


# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
numbers_4 = [1, 2, 3, 4, 5, 6]

is_even = filter(lambda n: n % 2 == 0, numbers_4)
print(list(is_even))  # [2, 4, 6]

# reduce()
expenses = [
    ("Dinner", 80),
    ("Car repair", 120)
]

# The 'long' way of coding this, more python like and preferred
# sum = 0
# for expense in expenses:
#     sum += expense[1]

sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)
