#!/usr/bin/env python3

# ------------
# Functions.py
# ------------

from functools import reduce
from types     import FunctionType, LambdaType, MethodType

print("Functions.py")

def plus_1 (x, y) :
    return x + y

def mult_1 (x, y) :
    return x * y

assert type(plus_1) is FunctionType
assert type(mult_1) is FunctionType

assert hasattr(plus_1, "__call__")
assert hasattr(mult_1, "__call__")

assert plus_1(2, 3) == 5
assert mult_1(2, 3) == 6

assert reduce(plus_1, [2, 3, 4]) ==  9
assert reduce(mult_1, [2, 3, 4]) == 24

plus_2 = lambda x, y : x + y
mult_2 = lambda x, y : x * y

assert type(plus_2) is LambdaType
assert type(mult_2) is LambdaType

assert hasattr(plus_2, "__call__")
assert hasattr(mult_2, "__call__")

assert plus_2(2, 3) == 5
assert mult_2(2, 3) == 6

assert reduce(plus_2, [2, 3, 4]) ==  9
assert reduce(mult_2, [2, 3, 4]) == 24

class Plus_3 (object) :
    def my_call (self, x, y) :
        return x + y

class Mult_3 (object) :
    def my_call (self, x, y) :
        return x * y

x = Plus_3()
y = Mult_3()

assert type(x) is Plus_3
assert type(y) is Mult_3

assert x.my_call(2, 3) == 5
assert y.my_call(2, 3) == 6

plus_3b = x.my_call
mult_3b = y.my_call

assert type(plus_3b) is MethodType
assert type(mult_3b) is MethodType

assert str(plus_3b)[1:6] == "bound"
assert str(mult_3b)[1:6] == "bound"

assert hasattr(plus_3b, "__call__")
assert hasattr(mult_3b, "__call__")

assert plus_3b(2, 3) == 5
assert mult_3b(2, 3) == 6

assert reduce(plus_3b, [2, 3, 4]) ==  9
assert reduce(mult_3b, [2, 3, 4]) == 24

plus_3u = Plus_3.my_call
mult_3u = Mult_3.my_call

assert type(plus_3u) is FunctionType
assert type(mult_3u) is FunctionType

assert hasattr(plus_3u, "__call__")
assert hasattr(mult_3u, "__call__")

#plus_3u(2, 3) # TypeError: unbound method my_call() must be called with Plus_3 instance as first argument (got int instance instead
#mult_3u(2, 3) # TypeError: unbound method my_call() must be called with Mult_3 instance as first argument (got int instance instead

assert plus_3u(x, 2, 3) == 5
assert mult_3u(y, 2, 3) == 6

#reduce(plus_3u, [2, 3, 4]) # TypeError: unbound method my_call() must be called with Plus_3 instance as first argument (got int instance instead
#reduce(mult_3u, [2, 3, 4]) # TypeError: unbound method my_call() must be called with Mult_3 instance as first argument (got int instance instead

class Plus_4 (object) :
    @staticmethod
    def my_call (x, y) :
        return x + y

class Mult_4 (object) :
    @staticmethod
    def my_call (x, y) :
        return x * y

plus_4 = Plus_4.my_call
mult_4 = Mult_4.my_call

assert type(plus_4) is FunctionType
assert type(mult_4) is FunctionType

assert hasattr(plus_4, "__call__")
assert hasattr(mult_4, "__call__")

assert plus_4(2, 3) == 5
assert mult_4(2, 3) == 6

assert reduce(plus_4, [2, 3, 4]) ==  9
assert reduce(mult_4, [2, 3, 4]) == 24

class Plus_5 (object) :
    def __call__ (self, x, y) :
        return x + y

class Mult_5 (object) :
    def __call__ (self, x, y) :
        return x * y

x = Plus_5()
y = Mult_5()

assert type(x) is Plus_5
assert type(y) is Mult_5

assert hasattr(x, "__call__")
assert hasattr(y, "__call__")

assert x(2, 3) == 5
assert y(2, 3) == 6

assert reduce(x, [2, 3, 4]) ==  9
assert reduce(y, [2, 3, 4]) == 24

print("Done.")
