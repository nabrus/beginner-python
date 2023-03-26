# LISTS
# Lists are one of 4 built-in data types in Python used to store collections of data.
# Lists are used to store multiple items in a single variable using square brackets.

# Different data types can be used in a list
items = ["lion", 693, False, "Tina"]

print("Tina" in items)  # True - using the `in` operator

# Referencing list items using it's index
print(items[0])  # lion
print(items[-1])  # Tina

# Updating items using index
items[2] = "R2D2"
print(items)  # ['lion', 693, R2D2, 'Tina'

# Slice
print(items[1:3])  # [693, 'R2D2']
print(items[1:])  # [693, 'R2D2', 'Tina']
print(items[:2])  # ['lion', 693]

# Adding  items to a list: Append method, Extend method, +=
items.append("DW")
print(items)  # ['lion', 693, 'R2D2', 'Tina', 'DW']

items.extend(["Homer", 77])
print(items)  # ['lion', 693, 'R2D2', 'Tina', 'DW', 'Homer', 77]

items += ["Richard"]
print(items)  # ['lion', 693, 'R2D2', 'Tina', 'DW', 'Homer', 77, 'Richard']

# Removing items from a list with remove-only takes one argument
items.remove("Homer")
print(items)  # ['lion', 693, 'R2D2', 'Tina', 'DW', 77, 'Richard']

# Return and remove the last item of a list with pop
print(items.pop())  # Richard
print(items)  # ['lion', 693, 'R2D2', 'Tina', 'DW', 77]


names = ["wyatt", "False", "Larry", "Michael Scott", "Santa"]

# Adding items - specifying the index
names.insert(1, "urban")
print(names)  # ['wyatt', 'urban', 'False', 'Larry', 'Michael Scott', 'Santa']

names[1:1] = ["Indiana", "Jones"]
# ['wyatt', 'Indiana', 'Jones', 'urban', 'False', 'Larry', 'Michael Scott', 'Santa']
print(names)

# Sorting Lists
print(sorted(names, key=str.lower))  # Does not modify list
#  ['False', 'Indiana', 'Jones', 'Larry', 'Michael Scott', 'Santa', 'urban', 'wyatt']
names_copy = names[:]  # Make a copy of a list before modifying
names.sort(key=str.lower)  # sort method modifies original list


print(names)
print(names_copy)
