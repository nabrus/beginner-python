# A function that calls itself is said to be recursive, and the
# technique of employing a recursive function is called recursion.

# Factorials - multiply all  whole numbers from the chosen number  down to 1
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Use recursion to create a function to calculate factorials
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120
