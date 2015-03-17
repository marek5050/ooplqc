#!/usr/bin/env python3

# ---------------
# FunctionDict.py
# ---------------

print("FunctionDict.py")

def f (x, y, **z) :
    assert type(z) is dict
    return [x, y, z]

assert f(2, 3)               == [2, 3, {}]
assert f(2, 3, a = 4)        == [2, 3, {'a' : 4}]
assert f(2, 3, a = 4, b = 5) == [2, 3, {'a' : 4, 'b' : 5}]
assert f(2, 3, a = 4, b = 5) == [2, 3, {'b' : 5, 'a' : 4}]

#f(2, 3, {'b' : 5, 'a' : 4})   # TypeError: f() takes exactly 2 arguments (3 given)
#f(2, 3, [('b', 5), ('a', 4)]) # TypeError: f() takes exactly 2 arguments (3 given)

d = {"b" : 4, "a" : 3}
u = (2,)
assert d                 == {'b' : 4, 'a' : 3}
assert d                 == {'a' : 3, 'b' : 4}
assert f(2, 5,     **d)  == [2, 5, {'a' : 3, 'b' : 4}]
assert f(2, y = 5, **d)  == [2, 5, {'a' : 3, 'b' : 4}]
assert f(y = 5, *u, **d) == [2, 5, {'a' : 3, 'b' : 4}]
assert f(*u, y = 5, **d) == [2, 5, {'a' : 3, 'b' : 4}]
#f(2, **d, y = 5)                                      # SyntaxError: invalid syntax

d = {"y" : 3, "x" : 2}
#f(2, **d)                   # TypeError: f() got multiple values for keyword argument 'x'
assert f(**d) == [2, 3, {}]

d = {"y" : 3}
assert f(2,     **d) == [2, 3, {}]
assert f(x = 2, **d) == [2, 3, {}]
#f(**d)                            # TypeError: f() takes exactly 2 arguments (1 given)

d = {"y" : 3, "a" : 2}
assert f(2,     **d) == [2, 3, {'a' : 2}]
assert f(x = 2, **d) == [2, 3, {'a' : 2}]
#f(**d)                                   # TypeError: f() takes exactly 2 arguments (1 given)

print("Done.")
