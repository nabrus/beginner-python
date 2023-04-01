# Lambda Functions - small  anonymous functions
# A lambda function can take any number of arguments, but can only have one expression.
# Note-Can only be an expression, not a statement - an expression returns a value and a statement does not

# Syntax: lambda arguments : expression
# lambda num: num * 2
# `lambda` is the keyword
# `num:` is the argument
# `num * 2` is the expression

# Multiple args
lambda a, b: a * b

# Cannot be called directly, use in a variable or within functions
# double = lambda num: num * 2
# print(double(4)) # 8
# Note linter does not allow, changes to regular defined function
