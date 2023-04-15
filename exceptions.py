# Exception error. This type of error occurs whenever syntactically correct Python code results in an error.

# Exception handling using `try` and `except`
# try:
#     #  Some lines of code
# except <ERROR1>:
#     # handler <ERROR1>
# except <ERROR2>:
#     # handler <ERROR2>
#     # except: # Except without an error type will handle all other errors
# else:
#     # No exceptions were raised, the code ran successfully
# finally:
#     # Do something in any case, this code will always run

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    result = 1

print(result)
# Cannot divide by zero!
# 1

# Raise exceptions
# Throw an error when a certain condition occurs using `raise`
try:
    raise Exception("An Error!!")
except Exception as error:
    print(error)


class dogNotFoundException(Exception):
    print("inside")
    pass  # this statement doesn't do anything, used for no code


try:
    raise dogNotFoundException()
except dogNotFoundException:
    print("Dog not found!")

# `with` statement
filename = "/Users/sju/code/pythonWith.txt"

try:
    file = open(filename, "r")
    content = file.read()
    print(content)
finally:
    file.close()

# Same result but using `with`, so no need to close since it is automatically done. Implicit exception handling
with open(filename, "r") as file:
    content = file.read()
    print(content)
