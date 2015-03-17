#!/usr/bin/env python3

# ----------
# Complex.py
# ----------

# https://docs.python.org/3.4/library/stdtypes.html#typesnumeric

from unittest import main, TestCase

class complex :
    ...

class MyUnitTests (TestCase) :
    def test_1 (self) :
        x = complex()
        self.assertEqual(x.real, 0)
        self.assertEqual(x.imag, 0)

    def test_2 (self) :
        x = complex(2)
        self.assertEqual(x.real, 2)
        self.assertEqual(x.imag, 0)

    def test_3 (self) :
        x = complex(2, 3)
        self.assertEqual(x.real, 2)
        self.assertEqual(x.imag, 3)

    def test_4 (self) :
        x = complex(2, 3)
        self.assertEqual(str(x), "(2+3j)")  # x.__str__()

    def test_5 (self) :
        x = complex(2, 3)
        y = complex(2, 3)
        self.assertEqual(x, y)              # x.__eq__(y)

    def test_6 (self) :
        x = complex(2, 3)
        y = complex(4, 5)
        x = x + y                           # x = x.__add__(y)
        self.assertEqual(x, complex(6, 8))

    def test_7 (self) :
        x = complex(2, 3)
        y = complex(4, 5)
        x += y                              # x = x.__add__(y)
        self.assertEqual(x, complex(6, 8))

    def test_8 (self) :
        x = complex(4, 5)
        y = complex(2, 3)
        x = x - y                           # x = x.__sub__(y)
        self.assertEqual(x, complex(2, 2))

    def test_9 (self) :
        x = complex(4, 5)
        y = complex(2, 3)
        x -= y                              # x = x.__isub__(y)
        self.assertEqual(x, complex(2, 2))

    def test_10 (self) :
        x = complex(2, 3)
        y = x.conjugate()                   # y = A.conjugate(x)
        self.assertEqual(x, complex(2,  3))
        self.assertEqual(y, complex(2, -3))

if __name__ == "__main__" :
    main()
