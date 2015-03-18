// --------------------
// IteratorPattern2.c++
// --------------------

#include <algorithm> // copy
#include <cassert>   // assert
#include <iostream>  // cout, endl
#include <iterator>  // ostream_iterator
#include <sstream>   // ostringstream

using namespace std;

template <typename II, typename OI>
OI my_copy (II b, II e, OI x) {
    while (b != e) {
        *x = *b;
        ++b;
        ++x;}
    return x;}

template <typename T>
class Digits {
    ...};

int main () {
    cout << "IteratorPattern.c++" << endl;

    {
    Digits<int> x = 0;
    Digits<int>::iterator b = x.begin();
    Digits<int>::iterator e = x.end();
    ostringstream out;
    copy(b, e, ostream_iterator<int>(out));
    assert(out.str() == "");
    }

    {
    Digits<int> x = 2;
    Digits<int>::iterator b = x.begin();
    Digits<int>::iterator e = x.end();
    ostringstream out;
    copy(b, e, ostream_iterator<int>(out));
    assert(out.str() == "2");
    }

    {
    Digits<int> x = 23;
    Digits<int>::iterator b = x.begin();
    Digits<int>::iterator e = x.end();
    ostringstream out;
    copy(b, e, ostream_iterator<int>(out));
    assert(out.str() == "32");
    }

    {
    Digits<int> x = 234;
    Digits<int>::iterator b = x.begin();
    Digits<int>::iterator e = x.end();
    ostringstream out;
    copy(b, e, ostream_iterator<int>(out));
    assert(out.str() == "432");
    }

    cout << "Done." << endl;
    return 0;}
