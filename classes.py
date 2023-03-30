# A Class is like an object constructor, or a "blueprint" for creating objects.
class Cat:
    def __init__(self, name, age):  # a constructor
        self.name = name
        self.age = age

    def speak(self):  # Created a method
        print("meow!")


# mose = Cat()  # Creates an instance of a class which is an object
# print(type(mose))  # <class '__main__.Cat'>

mose = Cat("Mose", 1006)
print(mose.name)  # Mose
print(mose.age)  # 1006
mose.speak()  # meow! note-not wrapped in print because method uses print, doesn't return anything
