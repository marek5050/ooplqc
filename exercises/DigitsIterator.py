#!/usr/bin/env python3

# -----------------
# DigitsIterator.py
# -----------------

from unittest import main, TestCase

class digits_iterator_class () :
    ...

def digits_iterator_function (n) :
    ...

def bind (c) :
    class MyUnitTests (TestCase) :
        def setUp (self) :
            self.p = c(234)

        def test_1 (self) :
            self.assertIs(iter(self.p), self.p)

        def test_2 (self) :
            self.assertEqual(list(self.p), [4, 3, 2])
            self.assertEqual(list(self.p), [])

    return MyUnitTests

digits_iterator_class_tests    = bind(digits_iterator_class)
digits_iterator_function_tests = bind(digits_iterator_function)

if __name__ == "__main__" :
    main()
