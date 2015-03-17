#!/usr/bin/env python3

# -------------------
# FunctionKeywords.py
# -------------------

print("FunctionKeywords.py")

def f (x, y, z) :
    return [x, y, z]

assert f(2, 3, 4) == [2, 3, 4]
#f(2, 3)                        # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 3, 4, 5)                  # TypeError: f() takes exactly 3 arguments (4 given)

assert f(2, z = 4, y = 3) == [2, 3, 4]
#f(z = 4, 3, x = 2)                     # SyntaxError: non-keyword arg after keyword arg
#f(2, z = 4, x = 2)                     # TypeError: f() got multiple values for keyword argument 'x'
#f(2, z = 4, a = 5)                     # TypeError: f() got an unexpected keyword argument 'a'

print("Done.")
