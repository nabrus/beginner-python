# Global functions - map(), filter(), reduce()

# The `map()` function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# Syntax: map(function, iterables)
numbers = [1, 2, 3]


def double(a):
    return a * 2


result = map(double, numbers)

print(list(result))  # [2, 4, 6]

# Convert to a `lambda` function
`
