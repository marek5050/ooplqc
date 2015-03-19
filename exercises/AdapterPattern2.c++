// -------------------
// AdapterPattern2.c++
// -------------------

#include <algorithm> // copy
#include <cassert>   // assert
#include <iostream>  // cout, endl, ostream
#include <iterator>  // iterator, ostream_iterator, output_iterator_tag
#include <sstream>   // ostringstream
#include <string>    // string, ==

using namespace std;

template <typename II, typename OI>
OI my_copy (II b, II e, OI x) {
    while (b != e) {
        *x = *b;
        ++b;
        ++x;}
    return x;}

template <typename T>
class my_ostream_iterator {
    private:
        ostream& _out;

    public:
        my_ostream_iterator (ostream& out) :
                _out (out)
            {}

        // Default copy, destructor, and copy assignment.
        // my_ostream_iterator (const my_ostream_iterator&);
        // ~my_ostream_iterator ();
        // my_ostream_iterator& operator = (const my_ostream_iterator&);

        my_ostream_iterator& operator = (const T& v) {
            _out << v;
            return *this;}

        my_ostream_iterator& operator * () {
            return *this;}

        my_ostream_iterator& operator ++ () {
            return *this;}

        my_ostream_iterator operator ++ (int) {
            return *this;}};

template <typename T>
void test () {
    const string  s   = "abCbA";
    ostringstream out;
    T             x   = out;
    copy(s.begin(), s.end(), x);
    assert(out.str() == s);}

int main () {
    cout << "AdapterPattern2.c++." << endl;

    test<my_ostream_iterator<char>>();
    test<   ostream_iterator<char>>();

    cout << "Done." << endl;
    return 0;}
