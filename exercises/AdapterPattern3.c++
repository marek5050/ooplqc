// -------------------
// AdapterPattern3.c++
// -------------------

#include <algorithm> // copy,
#include <cassert>   // assert
#include <iostream>  // cout, endl, istream
#include <iterator>  // input_iterator_tag, istream_iterator, iterator
#include <sstream>   // istringstream
#include <string>    // string
#include <utility>   // !=, <=, >, >=

using namespace std;

template <typename T>
class my_istream_iterator {
    // <your code>
    };

template <typename T>
void test () {
    const string     s = "abCbA";
    istringstream    in(s);
    T                b = in;
    T                e;
    string           t = "xxxxx";
    string::iterator x = t.begin();
    copy(b, e, x);
    assert(t == s);}

int main () {
    cout << "AdapterPattern3.c++." << endl;

//  test<my_istream_iterator<char>>();
    test<   istream_iterator<char>>();

    cout << "Done." << endl;
    return 0;}
