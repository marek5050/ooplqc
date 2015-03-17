#!/usr/bin/env python3

# ----------
# Complex.py
# ----------

# https://docs.python.org/3.4/library/stdtypes.html#typesnumeric

from unittest import main, TestCase

class my_complex :
    def __init__ (self, real = 0, imag = 0) :
        self.real = real
        self.imag = imag

    def __add__ (self, rhs) :
        return my_complex(self.real + rhs.real, self.imag + rhs.imag)

    def __eq__ (self, rhs) :
        if not isinstance(rhs, my_complex) :
            return False
        return (self.real == rhs.real) and (self.imag == rhs.imag)

    def __str__ (self) :
        return "(" + str(self.real) + "+" + str(self.imag) + "j)"

    def __sub__ (self, rhs) :
        return my_complex(self.real - rhs.real, self.imag - rhs.imag)

    def __isub__ (self, rhs) :
        return my_complex(self.real - rhs.real, self.imag - rhs.imag)

    def conjugate (self) :
        return my_complex(self.real, -self.imag)

def bind (c) :
    class MyUnitTests (TestCase) :
        def test_1 (self) :
            x = c()
            self.assertEqual(x.real, 0)
            self.assertEqual(x.imag, 0)

        def test_2 (self) :
            x = c(2)
            self.assertEqual(x.real, 2)
            self.assertEqual(x.imag, 0)

        def test_3 (self) :
            x = c(2, 3)
            self.assertEqual(x.real, 2)
            self.assertEqual(x.imag, 3)

        def test_4 (self) :
            x = c(2, 3)
            self.assertEqual(str(x), "(2+3j)")  # x.__str__()

        def test_5 (self) :
            x = c(2, 3)
            y = c(2, 3)
            self.assertEqual(x, y)              # x.__eq__(y)

        def test_6 (self) :
            x = c(2, 3)
            y = c(4, 5)
            x = x + y                           # x = x.__add__(y)
            self.assertEqual(x, c(6, 8))

        def test_7 (self) :
            x = c(2, 3)
            y = c(4, 5)
            x += y                              # x = x.__add__(y)
            self.assertEqual(x, c(6, 8))

        def test_8 (self) :
            x = c(4, 5)
            y = c(2, 3)
            x = x - y                           # x = x.__sub__(y)
            self.assertEqual(x, c(2, 2))

        def test_9 (self) :
            x = c(4, 5)
            y = c(2, 3)
            x -= y                              # x = x.__isub__(y)
            self.assertEqual(x, c(2, 2))

        def test_10 (self) :
            x = c(2, 3)
            y = x.conjugate()                   # y = A.conjugate(x)
            self.assertEqual(x, c(2,  3))
            self.assertEqual(y, c(2, -3))

    return MyUnitTests

my_complex_tests = bind(my_complex)
complex_tests    = bind(   complex)

if __name__ == "__main__" :
    main()
