# Operator Overloading
# In Python, operator overloading allows you to define how operators such as +, -, *, /, ==, !=, <, >, and others behave for instances of your custom classes.
# When you overload an operator, you define what should happen when that operator is used with instances of your class. This
# can be useful if you want to make your class behave like a built-in data type, or if you want to define a custom behavior for a particular operator.
class Dog:
    # the dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # operator overloading - use `__gt__` greater than
    def __gt__(self, other):
        return True if self.age > other.age else False


baxter = Dog("Baxter", 5)
scooby = Dog("Scooby", 10)

print(baxter > scooby)  # False
