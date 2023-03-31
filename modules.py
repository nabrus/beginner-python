# What is a Module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Every Python file is a module.

# Use `import` and the name of the python file, `cat.py` leaving off the extension. This imports the entire file.
# Or you can use `from` `import`, to specify a specific function.

import cat
from lib import dog
# or `from lib.dog import growl` to just access` a specific function

# then you can access the code from that file
cat.speak()  # Meeeeeooooooww!

dog.growl()  # Grrrrrrr

# Python Standard Library
# A huge collection of utilities

# math for math utilities
# re for regular expressions
# json to work with JSON
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System utilities
# random for random number generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to manage URLs
