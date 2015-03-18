// ------------
// IsPrime2.c++
// ------------

#include <cassert>  // assert
#include <cmath>    // sqrt
#include <iostream> // cout, endl

bool is_prime (int n) {
    assert(n > 0);
    if (n == 1)
        return false;
    if (n == 2)
        return true;
    if ((n % 2) == 0)
        return false;
    for (int i = 3; i <= sqrt(n); ++++i)
        if ((n % i) == 0)
            return false;
    return true;}

int main () {
    using namespace std;
    cout << "IsPrime2.c++" << endl;

    assert(!is_prime(1));
    assert( is_prime(2));
    assert( is_prime(3));
    assert(!is_prime(4));
    assert( is_prime(5));
    assert( is_prime(7));
    assert(!is_prime(9));
    assert(!is_prime(27));
    assert( is_prime(29));

    cout << "Done." << endl;
    return 0;}

/*
% IsPrime2
IsPrime2.c++
Done.



% gcov -b IsPrime2.c++ | grep -A 5 "File 'IsPrime2.c++'"
File 'IsPrime2.c++'
Lines executed:100.00% of 23
Branches executed:100.00% of 30
Taken at least once:66.67% of 30
No calls
IsPrime2.c++:creating 'IsPrime2.c++.gcov'
*/
