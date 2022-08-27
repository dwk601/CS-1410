"""
Example Money class.

Shows a simple Python class with with various magic methods and basic doctests.
Also deals with floating point issues and illustrates using divmod.

Author: George Rudolph
"""

import numbers
import math


class Money:
    """Stores money as pennies, uses integer arithmetic.

    >>> m = Money(123)
    >>> m1 = Money(1.23)
    Traceback (most recent call last):
    """

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        """Return money value as string in currency format.

        >>> print(Money(123))
        $1.23
        >>> print(Money(-123))
        -$1.23
        """
        sign = '-' if self.amount < 0 else ''

        dollars, cents = divmod(abs(self.amount), 100)
        return f"{sign}${dollars}.{cents:02}"

    def __add__(self, other):
        """Add an amount of money to this Money amount and return a new Money object.

        >>> m = Money(123) 
        >>> m2 = m + 79
        >>> print(m2)
        $2.02
        >>> m3 = 79 + Money(123)
        >>> print(m3)
        $2.02
        """
        if isinstance(other, int):
            other = Money(other)
        return Money(self.amount + other.amount)

    __radd__ = __add__

    def __sub__(self, other):
        """Subtract Money values from each other.

        >>> m = Money(123) 
        >>> m2 = m - 25
        >>> print(m2)
        $0.98
        """
        if isinstance(other, int):
            other = Money(other)
        return Money(self.amount - other.amount)

    def __rsub__(self, other):
        """Reverse the values before subtracting.

        >>> m3 = 25 - Money(123)
        >>> print(m3)
        -$0.98
        """
        if isinstance(other, int):
            other = Money(other)
        return other - self  # these are Money objects

    def compare(self, other):
        """Users should not call this function directly outside the class."""
        if isinstance(other, int):
            other = Money(other)
        return self.amount - other.amount

    def __eq__(self, other):
        """Compare for value equality.

        >>> Money(123) == Money(123)
        True
        >>> Money(123) == Money(200)
        False
        """
        return self.compare(other.amount) == 0

    def __ne__(self, other):
        """Compare for value non-equality.

        >>> Money(123) != Money(123)
        False
        >>> Money(123) != Money(200)
        True
        """
        return self.compare(other.amount) != 0

    def __lt__(self, other):
        """Compare for less than.

        >>> Money(123) < Money(123)
        False
        >>> Money(123) < Money(200)
        True
        """
        return self.compare(other.amount) < 0

    def __le__(self, other):
        """Compare for less than-or-equal.

        >>> Money(200) <= Money(123)
        False
        >>> Money(123) <= Money(123)
        True
        >>> Money(123) <= Money(200)
        True
        """
        return self.compare(other.amount) <= 0

    def __gt__(self, other):
        """Compare for greater than.

        >>> Money(123) > Money(123)
        False
        >>> Money(123) < Money(200)
        True
        """
        return self.compare(other.amount) > 0

    def __ge__(self, other):
        """Compare for greater than-or-equal.

        >>> Money(200) >= Money(123)
        True
        >>> Money(123) >= Money(123)
        True
        >>> Money(200) <= Money(123)
        False
        """
        return self.compare(other.amount) >= 0

    def __mul__(self, factor):
        """Mulitply a Money value by a Real number.

        This operation has 3 parts:
        1. integer math for the whole part.
        2. floating point math for the fractional part
        3. determining the sign of the result
        """

        # Determine magnitude of result
        amount = abs(self.amount)
        frac, whole = math.modf(abs(factor))
        amount = whole*amount + round(amount*frac)

        # Determine sign (exclusive-or of original signs)
        if (self.amount < 0) != (factor < 0):
            amount = -amount
        return Money(amount)

    __rmul__ = __mul__


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Test Money class
m1 = Money(123)     # $1.23
m2 = Money(456)     # $4.56
print(m1+m2)        # $5.79
print(789+m2)       # $12.45
print(m1+789)       # $9.12
print(m1-m2)        # -$3.33
print(100-m2)       # -$3.56
print(0.099*m2)     # $0.09
