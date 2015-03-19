// --------------------
// DecoratorPattern.c++
// --------------------

// http://en.wikipedia.org/wiki/Decorator_pattern
// http://en.wikipedia.org/wiki/Open/closed_principle

#include <cassert>    // assert
#include <functional> // function
#include <iostream>   // cout, endl

using namespace std;

template <typename F>
class pre_gtz {
    ...};

int cycle_length_1 (int n) {
    int c = 1;
    while (n > 1) {
        if ((n % 2) == 0)
            n = (n / 2);
        else
            n = (3 * n) + 1;
        ++c;}
    assert(c > 0);
    return c;}

struct cycle_length_2 {
    typedef int argument_type;
    typedef int result_type;

    int operator () (int n) const {
        int c = 1;
        while (n > 1) {
            if ((n % 2) == 0)
                n = (n / 2);
            else
                n = (3 * n) + 1;
            ++c;}
        assert(c > 0);
        return c;}};

int main () {
    cout << "DecoratorPattern2.c++" << endl;

    {
    assert(cycle_length_1(1)  == 1);
    assert(cycle_length_1(5)  == 6);
    assert(cycle_length_1(10) == 7);

    pre_gtz<function<int (int)>> f = function<int (int)>(cycle_length_1);

    assert(f(1)  == 1);
    assert(f(5)  == 6);
    assert(f(10) == 7);
    }

    {
    assert(cycle_length_2()(1)  == 1);
    assert(cycle_length_2()(5)  == 6);
    assert(cycle_length_2()(10) == 7);

    pre_gtz<cycle_length_2> f = cycle_length_2();

    assert(f(1)  == 1);
    assert(f(5)  == 6);
    assert(f(10) == 7);
    }

    cout << "Done." << endl;
    return 0;}
