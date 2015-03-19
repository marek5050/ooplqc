// ------------------
// PolicyPattern2.c++
// ------------------

#include <algorithm> // copy, equal, fill, swap
#include <algorithm> // fill
#include <cassert>   // assert
#include <cstddef>   // size_t
#include <iostream>  // cout, endl
#include <iterator>  // ostream_iterator
#include <memory>    // allocator
#include <sstream>   // ostringstream

using namespace std;

template <typename II, typename OI>
OI my_copy (II b, II e, OI x) {
    while (b != e) {
        *x = *b;
        ++b;
        ++x;}
    return x;}

template <typename II1, typename II2>
bool my_equal (II1 b, II1 e, II2 c) {
    while (b != e) {
        if (*b != *c)
            return false;
        ++b;
        ++c;}
    return true;}

template <typename T>
class my_vector {
    private:
        size_t _s;
        T*     _a;

    public:
        my_vector (size_t s = 0, const T& v = T()) :
                _s (s),
                _a (s == 0 ? 0 : new T[s]) {
            fill(begin(), end(), v);}

        my_vector (const my_vector& rhs) {
            // <your code>
            }

        my_vector& operator = (my_vector rhs) {
            // <your code>
            return *this;}

        ~my_vector () {
            delete [] _a;}

        T& operator [] (size_t i) {
            return _a[i];}

        const T& operator [] (size_t i) const {
            return const_cast<my_vector<T>*>(this)->operator[](i);}

        T* begin () {
            return _a;}

        const T* begin () const {
            return const_cast<my_vector<T>*>(this)->begin();}

        T* end () {
            return _a + _s;}

        const T* end () const {
            return const_cast<my_vector<T>*>(this)->end();}

        size_t size () const {
            return _s;}};

int main () {
    cout << "PolicyPattern2.c++" << endl;

    {
    my_vector<int> x;
    }

    {
    my_vector<int> x(3);
    assert(x.size() == 3);
    assert(x[1] == 0);
    x[1] = 2;
    assert(x[1] == 2);
    }

    {
    const my_vector<int> x(3, 4);
    assert(x.size() == 3);
    assert(x[1] == 4);
    ostringstream out;
    copy(x.begin(), x.end(), ostream_iterator<int>(out));
    assert(out.str() == "444");
    }
/*
    {
    const my_vector<int> x(10, 2);
    const my_vector<int> y = x;
    assert(equal(x.begin(), x.end(), y.begin()) == true);
    }

    {
          my_vector<int> x(10, 2);
    const my_vector<int> y(20, 3);
    x = y;
    assert(equal(x.begin(), x.end(), y.begin()) == true);
    }
*/
    cout << "Done." << endl;
    return 0;}
