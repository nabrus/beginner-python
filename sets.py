# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and un-indexed.
# * Note: Set items are unchangeable, but you can remove items and add new items
# Sets are written with curly brackets.
# No duplicates - Sets cannot have two items with the same value.
# Sets can contain any data type and have different data types.

set1 = {'Plane', 'Truck', 'Boat', 'Motorcycle'}
set2 = {'Playstation', 5, 'Dog', False}

# Intersect-items in sets that they have in common
names1 = {'Wyatt', 'Mose'}
names2 = {'Wyatt'}

intersect = names1 & names2
print(intersect)  # {'Wyatt'}

# Union `|`
mod = set1 | set2
print(mod)
# {False, 'Boat', 5, 'Plane', 'Dog', 'Motorcycle', 'Truck', 'Playstation'}

# Difference between sets
diff = names1 - names2
print(diff)  # {'Mose'}

# CHecking for superset and subset
greaterThan = names1 > names2
print(greaterThan)  # True
lessThan = names1 < names2
print(lessThan)  # False

# Getting a list from a set
print(list(set2))  # [False, 'Playstation', 'Dog', 5]

# No duplicates
fruits = {'banana', 'apple', 'grapes', 'apple', 'banana', 'peach'}
print(fruits)  # {'peach', 'grapes', 'apple', 'banana'}
