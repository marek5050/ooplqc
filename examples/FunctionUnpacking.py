#!/usr/bin/env python3

# --------------------
# FunctionUnpacking.py
# --------------------

import collections

print("FunctionUnpacking.py")

def f (x, y, z) :
    return [x, y, z]

t = (3, 4)
assert t            == (3, 4)
assert t            != (4, 3)
assert f(2, t, 5)   == [2, (3, 4), 5]
assert f(2, 5, t)   == [2, 5, (3, 4)]
assert f(2, *t)     == [2, 3, 4]
assert f(z = 2, *t) == [3, 4, 2]
assert f(*t, z = 2) == [3, 4, 2]
#f(*t, 2)                              # SyntaxError: invalid syntax
#f(x = 2, *t)                          # f() got multiple values for argument 'x'
#f(*t)                                 # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, *t)                           # TypeError: f() takes exactly 3 arguments (4 given)

l = [3, 4]
assert l            == [3, 4]
assert l            != [4, 3]
assert f(2, l, 5)   == [2, [3, 4], 5]
assert f(2, 5, l)   == [2, 5, [3, 4]]
assert f(2, *l)     == [2, 3, 4]
assert f(z = 2, *l) == [3, 4, 2]
assert f(*l, z = 2) == [3, 4, 2]
#f(*l, 2)                              # SyntaxError: only named arguments may follow *expression
#f(x = 2, *l)                          # f() got multiple values for argument 'x'
#f(*l)                                 # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, *l)                           # TypeError: f() takes exactly 3 arguments (4 given)

s = {3, 4}
assert s                 == {3, 4}
assert s                 == {4, 3}
assert f(2, s, 5)        == [2, {3, 4}, 5]
assert f(2, 5, s)        == [2, 5, {3, 4}]
assert set(f(2, *s))     == {2, 3, 4}
assert set(f(z = 2, *s)) == {2, 3, 4}
assert set(f(*s, z = 2)) == {2, 3, 4}
#f(*s, 2)                                   # SyntaxError: only named arguments may follow *expression
#f(x = 2, *s)                               # f() got multiple values for argument 'x'
#f(*s)                                      # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, *s)                                # TypeError: f() takes exactly 3 arguments (4 given)

d = {"b" : 4, "a" : 3}
assert type(d.keys()) is not collections.KeysView
assert isinstance(d.keys(), collections.KeysView)
assert set(d.keys()) == {"a", "b"}

assert type(d.values()) is not collections.ValuesView
assert isinstance(d.values(), collections.ValuesView)
assert set(d.values()) == {3, 4}

assert type(d.items()) is not collections.ItemsView
assert isinstance(d.items(), collections.ItemsView)
assert set(d.items()) == {("a", 3), ("b", 4)}

assert d                      == {'b' : 4, 'a' : 3}
assert d                      == {'a' : 3, 'b' : 4}
assert f(2, d, 5)             == [2, {'a' : 3, 'b' : 4}, 5]
assert f(2, 5, d)             == [2, 5, {'a' : 3, 'b' : 4}]
assert set(f(2, *d.keys()))   == {2, 'a', 'b'}
assert set(f(2, *d.values())) == {2, 3, 4}
assert set(f(2, *d.items()))  == {2, ('a', 3), ('b', 4)}
assert set(f(2, *d))          == {2, 'a', 'b'}
assert set(f(z = 2, *d))      == {2, 'a', 'b'}
assert set(f(*d, z = 2))      == {2, 'a', 'b'}
#f(*d, 2)                                                    # SyntaxError: only named arguments may follow *expression
#f(x = 2, *d)                                                # f() got multiple values for argument 'x'
#f(*d)                                                       # TypeError: f() missing 1 required positional argument: 'z'
#f(2, 5, *d)                                                 # TypeError: f() takes 3 positional arguments but 4 were given
#f(2, **d)                                                   # TypeError: f() got an unexpected keyword argument 'a'

d = {"z" : 4, "y" : 3, "x" : 2}
#f(2, **d)                      # TypeError: f() got multiple values for keyword argument 'x'
assert f(**d) == [2, 3, 4]

d = {"z" : 4, "y" : 3}
assert f(2,     **d) == [2, 3, 4]
assert f(x = 2, **d) == [2, 3, 4]
#f(**d, 2)                        # SyntaxError: invalid syntax
#f(**d, x = 2)                    # SyntaxError: invalid syntax
#f(**d)                           # TypeError: f() takes exactly 3 arguments (2 given)
#f(2, 5, **d)                     # TypeError: f() got multiple values for keyword argument 'y'

d = {"y" : 3}
#f(2, 4, **d)                        # TypeError: f() got multiple values for argument 'y'
assert f(2, z = 4, **d) == [2, 3, 4]

d = {"z" : 4, "y" : 3, "t" : 5}
#f(2,     **d)                  # TypeError: f() got an unexpected keyword argument 't'
#f(x = 2, **d)                  # TypeError: f() got an unexpected keyword argument 't'
#f(**d)                         # TypeError: f() got an unexpected keyword argument 't'

t = (2, 3)
d = {"z" : 4}
assert f(*t, **d) == [2, 3, 4]
#f(**d, *t)                    # SyntaxError: invalid syntax

print("Done.")
