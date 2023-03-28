# Python has two primitive loop commands - `for` and `while`

# With the `while`` loop we can execute a set of statements as long as a condition is true.

condition = True

# Infinite Loop !!!! without `break`
while condition == True:
    print("This condition is True")
    break

# With the break statement we can stop the loop even if the while condition is true

count = 0
while count < 10:
    print("Jump!")  # will print 'jump' 9 times
    count += 1  # increment by 1 until condition is met

print("After the loop")

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

numbers = [1, 2, 3, 4]
for item in numbers:
    print(item)
# prints 1-4, each on a new line

# `range` Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for item in range(10):
    print(item)
# prints 0-9, each on a new line

# You can specify a starting value over the default starting value of 0, by adding a parameter.
for x in range(3, 15):
    print(x)  # prints 3-14, each on a new line

# You can change the default of incrementing by 1, using a third parameter
for x in range(5, 30, 4):
    print(x)  # prints 5-29 by 4's, each on a new line

# enumerate() Function - gives the index and item
names = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
for index, name in enumerate(names):
    print(index, name)
# 0 Homer
# 1 Marge
# 2 Bart
# 3 Lisa
# 4 Maggie

# Break and Continue
# A review from earlier,, with the `break` statement we can stop the loop before it has looped through all the items
# With the `continue` statement we can stop the current iteration of the loop, and continue with the next
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue
    print(item)
# 1
# 3
# 4

players = ["Nico", "Jack", "Timo", "Jesper"]
for player in players:
    if player == "Timo":
        break
    print(player)
# Nico
# Jack
