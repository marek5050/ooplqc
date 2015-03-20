// ----------------
// ProxPattern3.c++
// ----------------

// http://en.wikipedia.org/wiki/Proxy_pattern

#include <algorithm> // swap
#include <cassert>   // assert
#include <iostream>  // cout, endl

using namespace std;

class AbstractShape {
    friend bool operator == (const AbstractShape& lhs, const AbstractShape& rhs) {
        return lhs.equals(rhs);}

    friend bool operator != (const AbstractShape& lhs, const AbstractShape& rhs) {
        return !(lhs == rhs);}

    friend std::istream& operator >> (std::istream& lhs, AbstractShape& rhs) {
        return rhs.read(lhs);}

    friend std::ostream& operator << (std::ostream& lhs, const AbstractShape& rhs) {
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

        virtual std::istream& read (std::istream& in) = 0;

        virtual std::ostream& write (std::ostream& out) const = 0;

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

std::istream& AbstractShape::read (std::istream& in) {
    return in >> _x >> _y;}

std::ostream& AbstractShape::write (std::ostream& out) const {
    return out << _x << " " << _y;}

class Circle : public AbstractShape {
    private:
        int _r;

    protected:
        virtual bool equals (const AbstractShape& that) const {
            if (const Circle* const p = dynamic_cast<const Circle*>(&that))
                return AbstractShape::equals(*p) && (_r == p->_r);
            return false;}

        virtual std::istream& read (std::istream& in) {
            return AbstractShape::read(in) >> _r;}

        virtual std::ostream& write (std::ostream& out) const {
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

typedef Handle<AbstractShape> Shape;

int main () {
    using namespace std;
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
//  x->move(5, 6);                                                           // doesn't compile
    assert(x->area() == (3.14 * 4 * 4));
//  assert(x->radius() == 4);                                                // doesn't compile
    if (const Circle* const q = dynamic_cast<const Circle*>(x.operator->()))
        assert(q->radius() == 4);
    try {
        const Circle& r = dynamic_cast<const Circle&>(x.operator*());
        assert(r.radius() == 4);}
    catch (const bad_cast& e) {
        assert(false);}
    }

    {
    Shape x = new Circle(2, 3, 4);
    x->move(5, 6);
    assert(x->area() == (3.14 * 4 * 4));
//  assert(x->radius() == 4);                                          // doesn't compile
    if (const Circle* const q = dynamic_cast<Circle*>(x.operator->()))
        assert(q->radius() == 4);
    try {
        const Circle& r = dynamic_cast<Circle&>(x.operator*());
        assert(r.radius() == 4);}
    catch (const bad_cast& e) {
        assert(false);}
    }

    {
    const Shape x = new Circle(2, 3, 4);
          Shape y = x;
    y->move(5, 6);
    assert(y->area() == (3.14 * 4 * 4));
    }

    {
    const Shape x = new Circle(2, 3, 4);
          Shape y = new Circle(2, 3, 5);
    assert(x != y);
    y = x;
    assert(x == y);
    }

    {
    Shape x = new Circle(2, 3, 4);
    assert(x->area() == (3.14 * 4 * 4));
    x = new Circle(5, 6, 7);
    assert(x->area() == (3.14 * 7 * 7));
    }

    cout << "Done." << endl;
    return 0;}
