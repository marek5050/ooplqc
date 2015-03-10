#!/usr/bin/env python3

# --------
# Hello.py
# --------

# https://www.python.org

print("Nothing to be done.")

"""
Developed in 1989 by Guido van Rossum of the Netherlands, now at Dropbox.
Python is procedural, object-oriented, dynamically typed, and garbage collected.



% python3 -V
Python 3.2.3



% python3 Hello.py
Nothing to be done.



% chmod ugo+x Hello.py
% Hello.py
Nothing to be done.



% python3
Python 3.2.3 (default, Sep 25 2013, 18:22:43)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

>>> import Hello
Nothing to be done.

>>> quit()



% python3
Python 3.2.3 (default, Sep 25 2013, 18:22:43)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

>>> help()

Welcome to Python 3.2!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> range

Help on built-in function range in module __builtin__:

range(...)
Help on class range in module builtins:

class range(object)
 |  range([start,] stop[, step]) -> range object
 |
 |  Returns a virtual sequence of numbers from start to stop by step.
 |
 |  Methods defined here:
 |
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x
 |
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |
 |  __reduce__(...)
 |
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |
 |  __reversed__(...)
 |      Returns a reverse iterator.
 |
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |
 |  index(...)
 |      rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.
 |      Raises ValueError if the value is not present.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.

>>> quit()



% python3
Python 3.2.3 (default, Sep 25 2013, 18:22:43)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

>>> quit()
"""
