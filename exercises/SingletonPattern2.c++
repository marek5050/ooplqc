// ---------------------
// SingletonPattern2.c++
// ---------------------

// https://en.wikipedia.org/wiki/Singleton_pattern

#include <cassert>  // assert
#include <iostream> // cout, endl
#include <memory>   // shared_ptr
#include <string>   // string, ==

using namespace std;

class LazyClass {
    private:
        static shared_ptr<LazyClass> _only;

        LazyClass ()
            {}

        LazyClass (const LazyClass&);

    public:
        static LazyClass& only () {
            if (!_only)
                _only = shared_ptr<LazyClass>(new LazyClass());
            return *_only;}

        string f () const {
            return "LazyClass::f()";}};

shared_ptr<LazyClass> LazyClass::_only;

class EagerClass {
    private:
        static EagerClass _only;

        EagerClass ()
            {}

        EagerClass (const EagerClass&);

    public:
        static EagerClass& only () {
            return _only;}

        string f () const {
            return "EagerClass::f()";}};

EagerClass EagerClass::_only;

class LazyLocal {
    private:
        LazyLocal ()
            {}

        LazyLocal (const LazyLocal&);

    public:
        static LazyLocal& only () {
            static LazyLocal x;
            return x;}

        string f () const {
            return "LazyLocal::f()";}};
template <typename T>
void test (const string& s) {
    assert(&T::only()     == &T::only());
    assert( T::only().f() == s);}

int main () {
    cout << "SingletonPattern2.c++" << endl;

    test<EagerClass>("EagerClass::f()");
    test<LazyClass>("LazyClass::f()");
    test<LazyLocal>("LazyLocal::f()");

    cout << "Done." << endl;
    return 0;}
