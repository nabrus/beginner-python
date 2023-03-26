# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# * ordered in Python 3.7 and >, unordered in previous versions

comp = {
    "type": "laptop",
    "memory": 32,
    "size": 14,
    "brand": "Apple"
}

print(comp["brand"])  # Apple

# Change a value
comp["type"] = "desktop"
print(comp)  # {'type': 'desktop', 'memory': 32, 'size': 14, 'brand': 'Apple'}

# The 'get' method
print(comp.get("size"))  # 14

# Setting a default value. Used when value cannot be found
print(comp.get("color", "gold"))  # gold

# 'pop' method - returns and deletes the item
print(comp.pop("memory"))  # 32
print(comp)  # {'type': 'desktop', 'size': 14, 'brand': 'Apple'}

# 'popitem' method - retrieves and removes last key-value in dict
print(comp.popitem())  # ('brand', 'Apple')

# Find out if a key is contained using the 'in' operator
print("size" in comp)  # True

# 'keys' method for listing all keys in a dict
print(comp.keys())  # dict_keys(['type', 'size'])
# Use list to return a list
print(list(comp.keys()))  # ['type', 'size']

# `values` method for listing all values in a dict
print(comp.values())  # dict_values(['desktop', 14])
# Use `list` to return a list
print(list(comp.values()))  # ['desktop', 14]

# Use `items` to list the items in a dict
print(list(comp.items()))  # [('type', 'desktop'), ('size', 14)]

# `len` to find out how many items in dict
print(len(comp))  # 2

# Adding key-value pairs to a dict
comp["model"] = "macBook Pro"
print(comp)  # {'type': 'desktop', 'size': 14, 'model': 'macBook Pro'}

# Deleting a key-value pair from a dict
del comp['type']
print(comp)  # {'size': 14, 'model': 'macBook Pro'}

# Copying a dict
compCopy = comp.copy()
print(compCopy)  # {'size': 14, 'model': 'macBook Pro'}
