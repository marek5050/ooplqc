// -------------
// Coverage2.c++
// -------------

// http://gcc.gnu.org/onlinedocs/gcc/Gcov.html

#include <cassert>  // assert
#include <iostream> // cout, endl

int cycle_length (int n) {
    assert(n > 0);
    int c = 1;
    while (n > 1) {
        if ((n % 2) == 0)
            n = (n / 2);
        else
            n = (3 * n) + 1;
        ++c;}
    assert(c > 0);
    return c;}

int main () {
    using namespace std;
    cout << "Coverage2.c++" << endl;

    assert(cycle_length(1) == 1);
    assert(cycle_length(2) == 2);

    cout << "Done." << endl;
    return 0;}

/*
% g++-4.7 -fprofile-arcs -ftest-coverage -pedantic -std=c++11 -Wall Coverage1.c++ -o Coverage1 -lgtest -lgtest_main -pthread
Coverage2
Coverage2.c++
Done.



% gcov -b Coverage2.c++
File 'Coverage2.c++'
Lines executed:92.86% of 14
Branches executed:100.00% of 12
Taken at least once:58.33% of 12
No calls
Coverage2.c++:creating 'Coverage2.c++.gcov'
...



% cat Coverage2.c++.gcov
...
*/
