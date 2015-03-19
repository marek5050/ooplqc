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

struct cycle_length {
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
    cout << "DecoratorPattern.c++" << endl;

    assert(cycle_length()(1)  == 1);
    assert(cycle_length()(5)  == 6);
    assert(cycle_length()(10) == 7);

    pre_gtz<cycle_length> f = cycle_length();

    assert(f(1)  == 1);
    assert(f(5)  == 6);
    assert(f(10) == 7);

    cout << "Done." << endl;
    return 0;}
