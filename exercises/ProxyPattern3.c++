// ----------------
// ProxPattern3.c++
// ----------------

// http://en.wikipedia.org/wiki/Proxy_pattern

#include <algorithm> // swap
#include <cassert>   // assert
#include <cstddef>   // size_t
#include <iostream>  // cout, endl

using namespace std;

class AbstractShape {
    friend bool operator == (const AbstractShape& lhs, const AbstractShape& rhs) {
        return lhs.equals(rhs);}

    friend bool operator != (const AbstractShape& lhs, const AbstractShape& rhs) {
        return !(lhs == rhs);}

    friend istream& operator >> (istream& lhs, AbstractShape& rhs) {
        return rhs.read(lhs);}

    friend ostream& operator << (ostream& lhs, const AbstractShape& rhs) {
        return rhs.write(lhs);}

    private:
        int _x;
        int _y;

    protected:
        AbstractShape& operator = (const AbstractShape& that) {
            _x = that._x;
            _y = that._y;
            return *this;}

        virtual bool equals (const AbstractShape& that) const = 0;

        virtual istream& read (istream& in) = 0;

        virtual ostream& write (ostream& out) const = 0;

    public:
        AbstractShape (int x, int y) :
                _x (x),
                _y (y)
            {}
/*
        AbstractShape (const AbstractShape& that) :
                _x (that._x),
                _y (that._y)
            {}
*/
        virtual ~AbstractShape ()
            {}

        virtual double area () const = 0;

        virtual AbstractShape* clone () const = 0;

        void move (int x, int y) {
            _x = x;
            _y = y;}};

bool AbstractShape::equals (const AbstractShape& that) const {
    return (_x == that._x) && (_y == that._y);}

istream& AbstractShape::read (istream& in) {
    return in >> _x >> _y;}

ostream& AbstractShape::write (ostream& out) const {
    return out << _x << " " << _y;}

class Circle : public AbstractShape {
    private:
        int _r;

    protected:
        virtual bool equals (const AbstractShape& that) const {
            if (const Circle* const p = dynamic_cast<const Circle*>(&that))
                return AbstractShape::equals(*p) && (_r == p->_r);
            return false;}

        virtual istream& read (istream& in) {
            return AbstractShape::read(in) >> _r;}

        virtual ostream& write (ostream& out) const {
            return AbstractShape::write(out) << " " << _r;}

    public:
        Circle (int x, int y, int r) :
                AbstractShape (x, y),
                _r            (r)
            {}
/*
        Circle (const Circle& that) :
                AbstractShape (that),
                _r            (that._r)
            {}

        virtual ~Circle ()
            {}

        Circle& operator = (const Circle& that) {
            AbstractShape::operator=(that);
            _r = that._r;
            return *this;}
*/

        virtual double area () const {
            return 3.14 * _r * _r;}

        virtual Circle* clone () const {
            return new Circle(*this);}

        int radius () const {
            return _r;}};

template <typename T>
class Handle {
    // <your code>
    };

struct Shape : Handle<AbstractShape> {
    Shape (AbstractShape* p) :
            Handle<AbstractShape> (p)
        {}
/*
    Shape (const Shape& that) :
            Handle<AbstractShape> (that)
        {}

    ~Shape ()
        {}

    Shape& operator = (const Shape& that) {
        Handle<AbstractShape>::operator=(that);
        return *this;}
*/
    double area () const {
        return get()->area();}

    void move (int x, int y) {
        return get()->move(x, y);}};

int main () {
    cout << "ProxyPattern3.c++" << endl;

    {
    Circle x(2, 3, 4);
    assert(x.area() == 3.14 * 4 * 4);
    x.move(5, 6);
    assert(x.radius() == 4);
    }

    {
    const Circle x(2, 3, 4);
          Circle y(2, 3, 5);
    assert(x != y);
    y = x;
    assert(x == y);
    }

    {
    const Shape x = new Circle(2, 3, 4);
//  x.move(5, 6);                         // doesn't compile
    assert(x.area()   == (3.14 * 4 * 4));
//  assert(x.radius() == 4);              // doesn't compile
    assert(x.unique());
    assert(x.use_count() == 1);
    }

    {
    Shape x = new Circle(2, 3, 4);
    x.move(5, 6);
    assert(x.area()   == (3.14 * 4 * 4));
//  assert(x.radius() == 4);              // doesn't compile
    assert(x.unique());
    assert(x.use_count() == 1);
    }

    {
    const Shape x = new Circle(2, 3, 4);
          Shape y = x;
    assert(x == y);
    assert(!x.unique());
    assert(x.use_count() == 2);
    assert(!y.unique());
    assert(y.use_count() == 2);
    y.move(5, 6);
    assert(x.unique());
    assert(x.use_count() == 1);
    assert(y.unique());
    assert(y.use_count() == 1);
    assert(y.area() == (3.14 * 4 * 4));
    }

    {
    const Shape x = new Circle(2, 3, 4);
          Shape y = new Circle(2, 3, 5);
    assert(x != y);
    y = x;
    assert(x == y);
    assert(!x.unique());
    assert(x.use_count() == 2);
    assert(!y.unique());
    assert(y.use_count() == 2);
    y.move(5, 6);
    assert(x.unique());
    assert(x.use_count() == 1);
    assert(y.unique());
    assert(y.use_count() == 1);
    assert(y.area() == (3.14 * 4 * 4));
    }

    {
    Shape x = new Circle(2, 3, 4);
    assert(x.area() == (3.14 * 4 * 4));
    x = new Circle(5, 6, 7);
    assert(x.area() == (3.14 * 7 * 7));
    assert(x.unique());
    assert(x.use_count() == 1);
    }

    cout << "Done." << endl;
    return 0;}
