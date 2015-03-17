#!/usr/bin/env python3

# -------
# Map3.py
# -------

# https://docs.python.org/3.4/library/functions.html#map

from unittest import main, TestCase

def map (nf, *a) :
    ...

class MyUnitTests (TestCase) :
    def test_1 (self) :
        a = ()
        assert list(map(lambda x : x + x, a)) == []

    def test_2 (self) :
        a = (2, 3, 4)
        assert list(map(lambda x : x + x, a)) == [4, 6, 8]

    def test_3 (self) :
        a = (2, 3, 4)
        b = (5, 6, 7)
        assert list(map(lambda x, y : x + y, a, b)) == [7, 9, 11]

    def test_4 (self) :
        a = (2, 3)
        b = (4, 5)
        c = (6, 7)
        assert list(map(lambda x, y, z : x + y + z, a, b, c)) == [12, 15]

if __name__ == "__main__" :
    main()
