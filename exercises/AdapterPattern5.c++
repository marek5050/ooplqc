// -------------------
// AdapterPattern5.c++
// -------------------

#include <algorithm> // copy
#include <cassert>   // assert
#include <iostream>  // cout, endl
#include <iterator>  // back_insert_iterator
#include <vector>    // vector

using namespace std;

template <typename II, typename OI>
OI my_copy (II b, II e, OI x) {
    while (b != e) {
        *x = *b;
        ++b;
        ++x;}
    return x;}

template <typename C>
class my_back_insert_iterator {
    // <your code>
    };

template <typename T>
void test () {
    const vector<int> x = {5, 6};
          vector<int> y = {2, 3, 4};
          T           z(y);
    copy(x.begin(), x.end(), z);
    assert(y == vector<int>({2, 3, 4, 5, 6}));}

int main () {
    cout << "AdapterPattern5.c++" << endl;

//  test<my_back_insert_iterator<vector<int>>>();
    test<   back_insert_iterator<vector<int>>>();

    cout << "Done." << endl;
    return 0;}
