#!/usr/bin/env python

# -----------
# IsSorted.py
# -----------

from operator import gt, lt

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

def test (f) :
    a = (5, 2, 2, 3, 1)
    assert     f(a, 1, 1) # ()
    assert     f(a, 1, 2) # (2)
    assert     f(a, 1, 3) # (2, 2)
    assert     f(a, 1, 4) # (2, 2, 3)
    assert not f(a, 0, 4) # (5, 2, 2, 3)
    assert not f(a, 1, 5) # (2, 2, 3, 1)
    assert not f(a, 0, 5) # (5, 2, 2, 3, 1)

    a = (1, 4, 4, 3, 5)
    assert     f(a, 1, 1, gt) # ()
    assert     f(a, 1, 2, gt) # (4)
    assert     f(a, 1, 3, gt) # (4, 4)
    assert     f(a, 1, 4, gt) # (4, 4, 3)
    assert not f(a, 0, 4, gt) # (1, 4, 4, 3)
    assert not f(a, 1, 5, gt) # (4, 4, 3, 5)
    assert not f(a, 1, 5, gt) # (1, 4, 4, 3, 5)

print "IsSorted.py"

test(is_sorted_recursion)
test(is_sorted_while)
test(is_sorted_for)
test(is_sorted_any)

print "Done."
