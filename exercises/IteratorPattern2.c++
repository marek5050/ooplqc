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
    private:
        T _n;

    public:
        class iterator {
            friend bool operator != (const iterator& lhs, const iterator& rhs) {
                return lhs._n != rhs._n;}

            private:
                T _n;

            public:
                iterator (const T& n) :
                        _n (n)
                    {}

                T operator * () {
                    return _n % 10;}

                iterator& operator ++ () {
                    _n /= 10;
                    return *this;}};

        Digits (const T& n) :
                _n (n)
            {}

        const iterator begin () const {
            return iterator(_n);}

        const iterator end () const {
            return iterator(0);}};

int main () {
    cout << "IteratorPattern2.c++" << endl;

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
