#!/usr/bin/env python3

# -----------
# IsPrime2.py
# -----------

from math     import sqrt
from unittest import main, TestCase

def is_prime (n) :
    assert n > 0
    if (n == 1) or ((n % 2) == 0) :
        return n == 2
    for i in range(3, int(sqrt(n)) + 1, 2) :
        if (n % i) == 0 :
            return False
    return True

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertFalse(is_prime( 1))

    def test_2 (self) :
        self.assertTrue(is_prime( 2))

    def test_3 (self) :
        self.assertTrue(is_prime( 3))

    def test_4 (self) :
        self.assertFalse(is_prime( 4))

    def test_5 (self) :
        self.assertTrue(is_prime( 5))

    def test_6 (self) :
        self.assertTrue(is_prime( 7))

    def test_7 (self) :
        self.assertFalse(is_prime( 9))

    def test_8 (self) :
        self.assertFalse(is_prime(27))

    def test_9 (self) :
        self.assertTrue(is_prime(29))

if __name__ == "__main__" :
    main()

""" #pragma: no cover
coverage3 run --branch IsPrime2.py
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK



coverage3 report -m
Name       Stmts   Miss Branch BrMiss  Cover   Missing
------------------------------------------------------
IsPrime2      35      0     10      0   100%
"""
