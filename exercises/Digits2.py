#!/usr/bin/env python3

# ----------
# Digits2.py
# ----------

from unittest import main, TestCase

class digits_class :
    def __init__ (self, n) :
        self.n = n

    def __iter__ (self) :
        class iterator :
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

        return iterator(self.n)

class digits_function :
    def __init__ (self, n) :
        self.n = n

    def __iter__ (self) :
        n = self.n
        while n > 0 :
            yield n % 10
            n //= 10

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
