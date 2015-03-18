// -------------------
// AdapterPattern.c++
// -------------------

#include <algorithm> // copy
#include <cassert>   // assert
#include <iostream>  // cout, endl, ostream
#include <iterator>  // iterator, ostream_iterator, output_iterator_tag
#include <sstream>   // ostringstream
#include <string>    // string, ==

using namespace std;

template <typename T>
class my_ostream_iterator {
    // <your code>
    };

template <typename T>
void test () {
    const string  s   = "abCbA";
    ostringstream out;
    T             x   = out;
    copy(s.begin(), s.end(), x);
    assert(out.str() == s);}

int main () {
    cout << "AdapterPattern.c++." << endl;

//  test<my_ostream_iterator<char>>();
    test<   ostream_iterator<char>>();

    cout << "Done." << endl;
    return 0;}
