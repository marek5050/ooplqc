#!/usr/bin/env python3

# -------------
# Generators.py
# -------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-yield_stmt

import types

def f () :
    yield 2
    yield 3
    yield 4

print "Generators.py"

p = f()
assert type(p) is types.GeneratorType

assert next(p) == 2
assert next(p) == 3
assert next(p) == 4

try :
    assert next(p) == 5
    assert False
except StopIteration as e :
    assert type(e)      is StopIteration
    assert type(e.args) is tuple
    assert len(e.args)  == 0
else :
    assert False

print "Done."
