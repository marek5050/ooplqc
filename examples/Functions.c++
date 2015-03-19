// -------------
// Functions.c++
// -------------

#include <cassert>    // assert
#include <functional> // function, negate
#include <iostream>   // cout, endl

int negate_1 (int x) {
    return -x;}

template <typename T>
T negate_2 (const T& x) {
    return -x;}

struct negate_3 {
    int operator () (int x) const {
        return -x;}};

template <typename T>
struct negate_4 {
    T operator () (const T& x) const {
        return -x;}};

template <typename T>
struct negate_5 {
    typedef T argument_type;
    typedef T result_type;

    T operator () (const T& x) const {
        return -x;}};

int main () {
    using namespace std;
    cout << "Functions.c++" << endl;

    {
    assert(negate_1(2) == -2);
    function<int (int)> f = negate_1;
    assert(f(2) == -2);
    assert(sizeof(function<int (int)>::argument_type) == 4);
    assert(sizeof(function<int (int)>::result_type)   == 4);
    }

    {
    assert(negate_2(2) == -2);
    function<int (int)> f = negate_2<int>;
    assert(f(2) == -2);
    assert(sizeof(function<int (int)>::argument_type) == 4);
    assert(sizeof(function<int (int)>::result_type)   == 4);
    }

    {
    assert(negate_3()(2) == -2);
    function<int (int)> f = negate_3();
    assert(f(2) == -2);
    assert(sizeof(function<int (int)>::argument_type) == 4);
    assert(sizeof(function<int (int)>::result_type)   == 4);
    }

    {
    assert(negate_4<int>()(2) == -2);
    function<int (int)> f = negate_4<int>();
    assert(f(2) == -2);
    assert(sizeof(function<int (int)>::argument_type) == 4);
    assert(sizeof(function<int (int)>::result_type)   == 4);
    }

    {
    assert(negate_5<int>()(2) == -2);
    assert(sizeof(negate_5<int>::argument_type) == 4);
    assert(sizeof(negate_5<int>::result_type)   == 4);
    }

    {
    assert(negate<int>()(2) == -2);
    assert(sizeof(negate<int>::argument_type) == 4);
    assert(sizeof(negate<int>::result_type)   == 4);
    }

    cout << "Done." << endl;
    return 0;}
