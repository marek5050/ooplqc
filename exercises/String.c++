// ----------
// String.c++
// ----------

#include <algorithm> // copy
#include <cassert>   // assert
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
    string x = "abc";
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
    assert(out.str() == "azc");};

int main () {
    cout << "String.c++" << endl;

//  test<my_string>();
    test<   string>();

    cout << "Done." << endl;
    return 0;}
