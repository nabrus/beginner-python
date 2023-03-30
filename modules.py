# What is a Module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Every Python file is a module.

# Use `import` and the name of the python file, `cat.py` leaving off the extension
# Or you can use `from` `import`, to specify a specific function.
import cat
from dog import growl

# then you can access the code from that file
cat.speak()  # Meeeeeooooooww!

growl()  # Grrrrrrr
