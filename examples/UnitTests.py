#!/usr/bin/env python3

# ------------
# UnitTests.py
# ------------

# https://docs.python.org/3.2/library/unittest.html

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

if __name__ == "__main__" :
    main()

"""
FFF
======================================================================
FAIL: test_1 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 25, in test_1
    self.assertEqual(cycle_length( 1), 1)
  File "./UnitTests.py", line 20, in cycle_length
    assert c > 0
AssertionError

======================================================================
FAIL: test_2 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 28, in test_2
    self.assertEqual(cycle_length( 5), 6)
AssertionError: 5 != 6

======================================================================
FAIL: test_3 (__main__.MyUnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests.py", line 31, in test_3
    self.assertEqual(cycle_length(10), 7)
AssertionError: 6 != 7

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=3)
"""
