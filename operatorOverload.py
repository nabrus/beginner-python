# Operator Overloading
# In Python, operator overloading allows you to define how operators such as +, -, *, /, ==, !=, <, >, and others behave for instances of your custom classes.
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
