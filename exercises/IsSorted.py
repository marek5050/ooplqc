#!/usr/bin/env python3

# -----------
# IsSorted.py
# -----------

from operator import gt, lt
from unittest import main, TestCase

def is_sorted (a, b, e, f = lt) :
    ...

class MyUnitTestsLT (TestCase) :
    def setUp (self) :
        self.a = (5, 2, 2, 3, 1)

    def test_1 (self) :
        self.assertTrue(f(self.a, 1, 1)) # ()

    def test_2 (self) :
        self.assertTrue(f(self.a, 1, 2)) # (2)

    def test_3 (self) :
        self.assertTrue(f(self.a, 1, 3)) # (2, 2)

    def test_4 (self) :
        self.assertTrue(f(self.a, 1, 4)) # (2, 2, 3)

    def test_5 (self) :
        self.assertFalse(f(self.a, 0, 4)) # (5, 2, 2, 3)

    def test_6 (self) :
        self.assertFalse(f(self.a, 1, 5)) # (2, 2, 3, 1)

    def test_7 (self) :
        self.assertFalse(f(self.a, 0, 5)) # (5, 2, 2, 3, 1)

class MyUnitTestsGT (TestCase) :
    def setUp (self) :
        self.a = (1, 4, 4, 3, 5)

    def test_1 (self) :
        self.assertTrue(f(self.a, 1, 1, gt)) # ()

    def test_2 (self) :
        self.assertTrue(f(self.a, 1, 2, gt)) # (4)

    def test_3 (self) :
        self.assertTrue(f(self.a, 1, 3, gt)) # (4, 4)

    def test_4 (self) :
        self.assertTrue(f(self.a, 1, 4, gt)) # (4, 4, 3)

    def test_5 (self) :
        self.assertFalse(f(self.a, 0, 4, gt)) # (1, 4, 4, 3)

    def test_6 (self) :
        self.assertFalse(f(self.a, 1, 5, gt)) # (4, 4, 3, 5)

    def test_7 (self) :
        self.assertFalse(f(self.a, 0, 5, gt)) # (1, 4, 4, 3, 5)

if __name__ == "__main__" :
    main()
