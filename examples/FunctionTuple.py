#!/usr/bin/env python3

# ----------------
# FunctionTuple.py
# ----------------

print("FunctionTuple.py")

def f (x, y, *z) :
    assert type(z) is tuple
    return [x, y, z]

def g (x, y, *z) :
    assert type(z) is tuple
    return [x, y, set(z)]

assert f(2, 3)       == [2, 3, ()]
assert f(2, 3, 4)    == [2, 3, (4,)]
assert f(2, 3, 4, 5) == [2, 3, (4, 5)]

t = (3, 4)
u = (2,)
assert t            == (3, 4)
assert t            != (4, 3)
assert f(2, t,  5)  == [2, (3, 4), (5,)]
assert f(2, 5,  t)  == [2, 5, ((3, 4),)]
assert f(2, 5, *t)  == [2, 5, (3, 4)]
assert f(2, *t)     == [2, 3, (4,)]
assert f(*t)        == [3, 4, ()]
assert f(y = 3, *u) == [2, 3, ()]
assert f(*u, y = 3) == [2, 3, ()]
#f(2, y = 5, *t)                          # TypeError: f() got multiple values for argument 'y'
#f(x = 2, y = 5, *t)                      # TypeError: f() got multiple values for argument 'x'

l = [3, 4]
u = [2]
assert l            == [3, 4]
assert l            != [4, 3]
assert f(2, l,  5)  == [2, [3, 4], (5,)]
assert f(2, 5,  l)  == [2, 5, ([3, 4],)]
assert f(2, 5, *l)  == [2, 5, (3, 4)]
assert f(2, *l)     == [2, 3, (4,)]
assert f(y = 3, *u) == [2, 3, ()]
assert f(*u, y = 3) == [2, 3, ()]
#f(2, y = 5, *l)                          # TypeError: f() got multiple values for argument 'y'
#f(x = 2, y = 5, *l)                      # TypeError: f() got multiple values for argument 'x'

s = {3, 4}
u = {2}
assert s            == {4, 3}
assert s            == {3, 4}
assert f(2, s,  5)  == [2, {3, 4}, (5,)]
assert f(2, 5,  s)  == [2, 5, ({3, 4},)]
assert g(2, 5, *s)  == [2, 5, {3, 4}]
assert g(2, *s)     == [2, 3, {4}]       # ?
assert g(y = 3, *u) == [2, 3, set()]
assert g(*u, y = 3) == [2, 3, set()]
#g(2, y = 5, *s)                          # TypeError: f() got multiple values for argument 'y'
#g(x = 2, y = 5, *s)                      # TypeError: f() got multiple values for argument 'x'

d = {"b" : 4, "a" : 3}
u = {2 : "c"}
assert d                    == {'b' : 4, 'a' : 3}
assert d                    == {'a' : 3, 'b' : 4}
assert f(2, d,  5)          == [2, {'a' : 3, 'b' : 4}, (5,)]
assert f(2, 5,  d)          == [2, 5, ({'a' : 3, 'b' : 4},)]
assert g(2, 5, *d.keys())   == [2, 5, {'a', 'b'}]
assert g(2, 5, *d.values()) == [2, 5, {3, 4}]
assert g(2, 5, *d.items())  == [2, 5, {('a', 3), ('b', 4)}]
assert g(2, 5, *d)          == [2, 5, {'a', 'b'}]
assert g(2, *d)             == [2, 'a', {'b'}]               # ?
assert g(y = 3, *u)         == [2, 3, set()]
assert g(*u, y = 3)         == [2, 3, set()]
#f(2, y = 5, *d)                                             # TypeError: f() got multiple values for argument 'y'
#f(x = 2, y = 5, *d)                                         # TypeError: f() got multiple values for argument 'x'
#f(**d)                                                      # TypeError: f() got an unexpected keyword argument 'a'

d = {"z" : 4, "y" : 3}
#f(2, **d)             # TypeError: f() got an unexpected keyword argument 'z'
#f(**d)                # TypeError: f() got an unexpected keyword argument 'z'

d = {"y" : 3, "x" : 2}
#f(2, **d)                   # TypeError: f() got multiple values for keyword argument 'x'
assert f(**d) == [2, 3, ()]

d = {"y" : 3}
assert f(2,     **d) == [2, 3, ()]
assert f(x = 2, **d) == [2, 3, ()]
#f(**d)                             # TypeError: f() takes at least 2 arguments (1 given)

d = {"y" : 3, "t" : 5}
#f(2,     **d)         # TypeError: f() got an unexpected keyword argument 't'
#f(x = 2, **d)         # TypeError: f() got an unexpected keyword argument 't'
#f(**d)                # TypeError: f() got an unexpected keyword argument 't'

print("Done.")
