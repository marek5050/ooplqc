// -----------
// IsPrime.c++
// -----------

#include <cassert>  // assert
#include <cmath>    // sqrt
#include <iostream> // cout, endl

bool is_prime (int n) {
    assert(n > 0);
    if ((n == 1) || ((n % 2) == 0))
        return false;
    for (int i = 3; i < sqrt(n); ++i)
        if ((n % i) == 0)
            return false;
    return true;}

int main () {
    using namespace std;
    cout << "IsPrime.c++" << endl;

    assert(!is_prime(1));
    assert(!is_prime(2));
    assert( is_prime(3));
    assert(!is_prime(4));
    assert( is_prime(5));
    assert( is_prime(7));
    assert( is_prime(9));
    assert(!is_prime(27));
    assert( is_prime(29));

    cout << "Done." << endl;
    return 0;}

/*
% IsPrime
IsPrime.c++
Done.



% gcov -b IsPrime.c++ | grep -A 5 "File 'IsPrime.c++'"
File 'IsPrime.c++'
Lines executed:100.00% of 19
Branches executed:100.00% of 28
Taken at least once:64.29% of 28
No calls
IsPrime.c++:creating 'IsPrime.c++.gcov'
*/
