#!/usr/bin/env python3

# -----------
# IsSorted.py
# -----------

from operator import gt, lt
from unittest import main, TestCase

def is_sorted_recursion (a, b, e, f = lt) :
    assert(b <= e)
    if (b == e) or ((b + 1) == e) :
        return True
    if f(a[b + 1], a[b]) :
        return False
    return is_sorted_recursion(a, b + 1, e, f)

def is_sorted_while (a, b, e, f = lt) :
    assert(b <= e)
    while (b != e) and ((b + 1) != e) :
        if f(a[b + 1], a[b]) :
            return False
        b += 1
    return True

def is_sorted_for (a, b, e, f = lt) :
    assert(b <= e)
    for i in range(b, e - 1) :
        if f(a[i + 1], a[i]) :
            return False
    return True

def is_sorted_any (a, b, e, f = lt) :
    assert(b <= e)
    return not any(f(a[i + 1], a[i]) for i in range(b, e - 1))

def bind_lt (f) :
    class MyUnitTests (TestCase) :
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

    return MyUnitTests

def bind_gt (f) :
    class MyUnitTests (TestCase) :
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

    return MyUnitTests

is_sorted_recursion_tests_lt = bind_lt(is_sorted_recursion)
is_sorted_while_tests_lt     = bind_lt(is_sorted_while)
is_sorted_for_tests_lt       = bind_lt(is_sorted_for)
is_sorted_any_tests_lt       = bind_lt(is_sorted_any)

is_sorted_recursion_tests_gt = bind_gt(is_sorted_recursion)
is_sorted_while_tests_gt     = bind_gt(is_sorted_while)
is_sorted_for_tests_gt       = bind_gt(is_sorted_for)
is_sorted_any_tests_gt       = bind_gt(is_sorted_any)

if __name__ == "__main__" :
    main()
