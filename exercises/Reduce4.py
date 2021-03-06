#!/usr/bin/env python3

# ----------
# Reduce4.py
# ----------

# https://docs.python.org/3.4/library/functools.html

from functools import reduce
from operator  import sub
from unittest  import main, TestCase

def reduce_while (bf, a, v = None) :
    if (not a) and (v is None) :
        raise TypeError("reduce() of empty sequence with no initial value")
    if not a :
        return v
    p = iter(a)
    if v is None :
        v = next(p)
    try :
        while True :
            v = bf(v, next(p))
    except StopIteration :
        pass
    return v

def reduce_for (bf, a, v = None) :
    if (not a) and (v is None) :
        raise TypeError("reduce() of empty sequence with no initial value")
    if not a :
        return v
    p = iter(a)
    if v is None :
        v = next(p)
    for w in p :
        v = bf(v, w)
    return v

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            self.assertEqual(f(sub, [2]),           2)

        def test_2 (self) :
            self.assertEqual(f(sub, [2, 3]),       -1)

        def test_3 (self) :
            self.assertEqual(f(sub, [2, 3, 4]),    -5)

        def test_4 (self) :
            self.assertEqual(f(sub, [],        0),  0)

        def test_5 (self) :
            self.assertEqual(f(sub, [2],       0), -2)

        def test_6 (self) :
            self.assertEqual(f(sub, [2, 3],    0), -5)

        def test_7 (self) :
            self.assertEqual(f(sub, [2, 3, 4], 0), -9)

        def test_8 (self) :
            self.assertRaises(TypeError, f, sub, [])

    return MyUnitTests

reduce_while_tests = bind(reduce_while)
reduce_for_tests   = bind(reduce_for)
reduce_tests       = bind(reduce)

if __name__ == "__main__" :
    main()
