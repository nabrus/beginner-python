# Variables - declared with equal sign.
name = "Mose"
age = 1006

# Expressions (returns a value) and Statements (operations on a value)
1 + 1  # expression
print(name)  # statement

# Indentation is important with Python. Statements use this as code blocks

# Data types -

print(type(age))  # <class 'int'>  type function used to check type

age_a = 6
print(isinstance(age_a, float))  # false

# class constructors
age_b = "20"
age_c = int(age_b)
print(isinstance(age_c, int))  # true

# Operators
1 + 1  # 2
2 - 1  # 1
2 * 2  # 4
4 / 2  # 2
4 % 3  # 1 (remainder)
4 ** 2  # 16 (exponents: power of 2)
5 // 2  # 2 (floor division, divides rounding down)

# String replication operator
# the multiplication operator when used on a string performs replication.

print("Wyatt" * 3)  # WyattWyattWyatt
print("Hello World! " * 8)
# Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World! Hello World!

age_d = 9
age_d += 8  # age_d = age_d + 8
print(age_d)  # 17

# Comparison Operators
a = 1
b = 2

a == b  # False (equal)
a != b  # True (not equal `! =`)
a > b  # False
a <= b  # True

# Boolean (True/False)
condition1 = True
condition2 = False

# Boolean operators
not condition1  # False
condition1 and condition2  # False
condition1 or condition2  # True

# is & in Operators
# is  # Identity operator-compares objects
# in  # membership operator-lists and sequences

# Ternary Operator


def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# Using ternary for more concise code


def is_adult2(age):
    return True if age > 18 else False


print("What is your age?")
# Or put "What is your age?" in the parenthesis, eliminating the first print statement
answer = input()
print(f"You are {answer}.")

condition = False

if condition == True:
    print("This condition")
    print("is true")
else:
    print("This condition is not true")
