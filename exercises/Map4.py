#!/usr/bin/env python3

# -------
# Map4.py
# -------

# https://docs.python.org/3.4/library/functions.html#map

from unittest import TestCase, TestLoader, TestSuite, TextTestRunner

def map_for_zip (nf, *a) :
    for v in zip(*a) :
        yield nf(*v)

def map_generator_zip (nf, *a) :
    return (nf(*v) for v in zip(*a))

def bind (f) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            a = ()
            assert list(f(lambda x : x + x, a)) == []

        def test_2 (self) :
            a = (2, 3, 4)
            assert list(f(lambda x : x + x, a)) == [4, 6, 8]

        def test_3 (self) :
            a = (2, 3, 4)
            b = (5, 6, 7)
            assert list(f(lambda x, y : x + y, a, b)) == [7, 9, 11]

        def test_4 (self) :
            a = (2, 3)
            b = (4, 5)
            c = (6, 7)
            assert list(f(lambda x, y, z : x + y + z, a, b, c)) == [12, 15]
    return MyUnitTests

if __name__ == "__main__" :
    s = TestSuite()
    s.addTest(TestLoader().loadTestsFromTestCase(bind(map_for_zip)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(map_generator_zip)))
    s.addTest(TestLoader().loadTestsFromTestCase(bind(map)))
    TextTestRunner().run(s)
