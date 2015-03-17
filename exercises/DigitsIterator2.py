#!/usr/bin/env python3

# ------------------
# DigitsIterator2.py
# ------------------

from unittest import main, TestCase

class digits_iterator_class () :
    def __init__ (self, n) :
        self.n = n

    def __iter__ (self) :
        return self

    def __next__ (self) :
        if self.n == 0 :
            raise StopIteration()
        m = self.n % 10
        self.n //= 10
        return m

def digits_iterator_function (n) :
    while n > 0 :
        yield n % 10
        n //= 10

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
