#!/usr/bin/env python3

# ---------
# Digits.py
# ---------

from unittest import main, TestCase

class digits_class :
    def __init__ (self, n) :
        self.n = n

    def __iter__ (self) :
        ...

class digits_function :
    def __init__ (self, n) :
        self.n = n

    def __iter__ (self) :
        ...

def bind (c) :
    class MyUnitTests (TestCase) :
        def setUp (self) :
            self.x = c(234)

        def test_1 (self) :
            self.assertIsNot(iter(self.x), self.x)

        def test_2 (self) :
            self.assertEqual(list(self.x), [4, 3, 2])
            self.assertEqual(list(self.x), [4, 3, 2])

    return MyUnitTests

digits_class_tests    = bind(digits_class)
digits_function_tests = bind(digits_function)

if __name__ == "__main__" :
    main()
