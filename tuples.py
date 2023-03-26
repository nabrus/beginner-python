# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable (immutable).

# Parentheses are used, not square brackets
cars = ("RDX", "TLX", "Highlander")
print(cars[0])  # RDX
len(cars)  # 3

print(sorted(cars))  # ['Highlander', 'RDX', 'TLX']

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
thisTuple = ("apple", "banana", "cherry", "apple", "cherry")
