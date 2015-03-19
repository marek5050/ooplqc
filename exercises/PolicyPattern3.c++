// -----------------
// PolicyPattern.c++
// -----------------

#include <algorithm> // copy, equal, fill, swap
#include <cassert>   // assert
#include <cstddef>   // size_t
#include <iostream>  // cout, endl
#include <iterator>  // ostream_iterator
#include <memory>    // allocator
#include <sstream>   // ostringstream

using namespace std;

template <typename A, typename BI>
void my_destroy (A& a, BI b, BI e) {
    while (b != e) {
        --e;
        a.destroy(&*e);}}

template <typename A, typename II, typename BI>
BI my_uninitialized_copy (A& a, II b, II e, BI x) {
    BI p = x;
    try {
        while (b != e) {
            a.construct(&*x, *b);
            ++b;
            ++x;}}
    catch (...) {
        my_destroy(a, p, x);
        throw;}
    return x;}

template <typename A, typename BI, typename U>
void my_uninitialized_fill (A& a, BI b, BI e, const U& v) {
    BI p = b;
    try {
        while (b != e) {
            a.construct(&*b, v);
            ++b;}}
    catch (...) {
        my_destroy(a, p, b);
        throw;}}

template <typename T, typename A = allocator<T> >
class my_vector {
    private:
        A      _x;
        size_t _s;
        T*     _a;

    public:
        my_vector (size_t s = 0, const T& v = T(), const A& x = A()) :
                _x (x),
                _s (s),
                _a (_x.allocate(_s)) {
            my_uninitialized_fill(_x, _a, _a + _s, v);}

        my_vector (const my_vector& rhs) :
                _x (rhs._x),
                _s (rhs._s),
                _a (_x.allocate(_s)) {
            my_uninitialized_copy(_x, rhs._a, rhs._a + _s, _a);}

        my_vector& operator = (my_vector rhs) {
            swap(_a, rhs._a);
            swap(_s, rhs._s);
            return *this;}

        ~my_vector () {
            my_destroy(_x, _a, _a + _s);
            _x.deallocate(_a, _s);}

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
    cout << "PolicyPattern3.c++" << endl;

    {
    allocator<int> x;
    int* p = x.allocate(1);
    x.construct(p, 2);
    assert(*p == 2);
    x.destroy(p);
    x.deallocate(p, 1);
    }

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
    my_vector<int> x(3, 4);
    assert(x.size() == 3);
    assert(x[1] == 4);
    x[1] = 2;
    assert(x[1] == 2);
    ostringstream out;
    copy(x.begin(), x.end(), ostream_iterator<int>(out));
    assert(out.str() == "424");
    }

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

    cout << "Done." << endl;
    return 0;}
