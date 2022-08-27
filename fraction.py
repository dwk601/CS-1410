''' fraction.py:    Defines a Fraction class
    A Fraction object holds the numerator and denominator as integers.
    Illustrates class syntax, constructors/initializers, instances/objects, 
    and the self parameter.
    Provides a __str__ method for use with the print function.
'''


class Fraction:
    def __init__(self, n, d):
        assert d != 0
        self.num = n
        self.den = d

    def add(self, rhs):
        assert type(rhs) is Fraction
        num = self.num * rhs.den + rhs.num * self.den
        den = self.den * rhs.den
        return Fraction(num, den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)


x = Fraction(1, 2)
y = Fraction(3, 4)
print(x, '+', y, '=', x.add(y))  # 1/2 + 3/4 = 5/4 = 10/8
