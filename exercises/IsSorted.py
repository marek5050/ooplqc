#!/usr/bin/env python

# -----------
# IsSorted.py
# -----------

from operator import gt, lt

def is_sorted (a, b, e, f = lt) :
    ...

print "IsSorted.py"

a = (5, 2, 2, 3, 1)
assert     is_sorted(a, 1, 1) # ()
assert     is_sorted(a, 1, 2) # (2)
assert     is_sorted(a, 1, 3) # (2, 2)
assert     is_sorted(a, 1, 4) # (2, 2, 3)
assert not is_sorted(a, 0, 4) # (5, 2, 2, 3)
assert not is_sorted(a, 1, 5) # (2, 2, 3, 1)
assert not is_sorted(a, 0, 5) # (5, 2, 2, 3, 1)

a = (1, 4, 4, 3, 5)
assert     is_sorted(a, 1, 1, gt) # ()
assert     is_sorted(a, 1, 2, gt) # (4)
assert     is_sorted(a, 1, 3, gt) # (4, 4)
assert     is_sorted(a, 1, 4, gt) # (4, 4, 3)
assert not is_sorted(a, 0, 4, gt) # (1, 4, 4, 3)
assert not is_sorted(a, 1, 5, gt) # (4, 4, 3, 5)
assert not is_sorted(a, 1, 5, gt) # (1, 4, 4, 3, 5)

print "Done."
