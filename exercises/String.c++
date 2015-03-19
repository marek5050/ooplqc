// ----------
// String.c++
// ----------

#include <algorithm> // copy
#include <cassert>   // assert
#include <cstddef>   // size_t
#include <cstring>   // strcmp, strcpy, strlen
#include <iostream>  // cout, endl
#include <iterator>  // ostream_iterator
#include <sstream>   // ostringstream
#include <string>    // string

using namespace std;

class my_string {
    // <your code>
    };

template <typename T>
void test () {
    {
    T x = "abc";
    assert(x.size() == 3);
    assert(x        == "abc");
    assert("abc"    == x);
    assert(x[1]     == 'b');
    x[1] = 'z';
    assert(x        == "azc");
    assert("azc"    == x);
    assert(x[1]     == 'z');
    ostringstream out;
    copy(x.begin(), x.end(), ostream_iterator<char>(out));
    assert(out.str() == "azc");
    }

    {
    const T x = "abc";
    assert(x.size() == 3);
    assert(x        == "abc");
    assert("abc"    == x);
    assert(x[1]     == 'b');
//  x[1] = 'z';                                            // error: read-only variable is not assignable
    ostringstream out;
    copy(x.begin(), x.end(), ostream_iterator<char>(out));
    assert(out.str() == "abc");
    }};

int main () {
    cout << "String.c++" << endl;

//  test<my_string>();
    test<   string>();

    cout << "Done." << endl;
    return 0;}
