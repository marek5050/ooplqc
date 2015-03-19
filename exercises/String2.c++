// -----------
// String2.c++
// -----------

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
    private:
        size_t _s;
        char*  _a;

    public:
        my_string (const char* a) {
            _s = strlen(a);
            _a = new char[_s + 1];
            strcpy(_a, a);}

        ~my_string () {
            delete [] _a;}

        char& operator [] (size_t i) {
            return _a[i];}

        const char& operator [] (size_t i) const {
            return _a[i];}

        char* begin () {
            return _a;}

        const char* begin () const {
            return _a;}

        char* end () {
            return _a + _s;}

        const char* end () const {
            return _a + _s;}

        size_t size () const {
            return _s;}
    };

bool operator == (const my_string& lhs, const my_string& rhs) {
    return strcmp(lhs.begin(), rhs.begin()) == 0;}

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
    cout << "String2.c++" << endl;

    test<my_string>();
    test<   string>();

    cout << "Done." << endl;
    return 0;}
