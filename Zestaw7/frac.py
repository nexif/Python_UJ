import math

class Frac: #Klasa reprezentująca ułamki

    def __init__(self, x=0, y=1): #sprawdzamy czy y=0
        if y == 0: raise ValueError("Wartość 0 nie może występować w mianowniku")
        self.x = x
        self.y = y

    def __str__(self): #Zwraca string 'x/y'
        if self.y == 1:
            return "{0}".format(self.x)
        else:
            return "{0}/{1}".format(self.x, self.y)

    def __repr__(self): #Zwraca string "Frac(x, y)
        return "Frac({0}, {1})".format(self.x, self.y)

    def __eq__(self, other): #Obsługa Frac1 == Frac2
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x == frac2.x

    def __ne__(self, other): #Obsługa Frac1 != Frac2
        return not self == other

    def __lt__(self, other): #Obsługa Frac1 < Frac2
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x < frac2.x

    def __le__(self, other): #Obsługa Frac1 <= Frac2
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x <= frac2.x

    def __gt__(self, other): #Obsługa Frac1 > Frac2
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x > frac2.x

    def __ge__(self, other): #Obsługa Frac1 >= Frac2
        frac1, frac2 = to_common_denominator(self, other)
        return frac1.x >= frac2.x

    def __add__(self, other):
        if isinstance(other, Frac): #frac1 + frac2
            y = least_common_multiple(self.y, other.y)
            x = self.x * (y / self.y) + other.x * (y / other.y)
            return Frac(x, y)
        elif isinstance(other, int): #frac1 + int
            x = self.x + other * self.y
            y = self.y
            return Frac(x, y)
        elif isinstance(other, float): #frac1 + float
            a, b = other.as_integer_ratio()
            y = least_common_multiple(self.y, b)
            x = self.x * (y / self.y) + a * (y / b)
            return Frac(x, y)

    #int+frac
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac): #frac1 - frac2
            y = least_common_multiple(self.y, other.y)
            x = self.x * (y / self.y) - other.x * (y / other.y)
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, int): #frac1 - int
            x = self.x - other * self.y
            y = self.y
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, float): #frac1 - float
            a, b = other.as_integer_ratio()
            y = least_common_multiple(self.y, b)
            x = self.x * (y / self.y) - a * (y / b)
            return Frac(x, y)

    def __rsub__(self, other): #int-frac, tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac): #frac1 * frac2
            x = self.x * other.x
            y = self.y * other.y
            gcd = math.gcd(x, y)
            return Frac(x // gcd, y // gcd)
        elif isinstance(self, Frac) and isinstance(other, int): #frac1 * int
            x = self.x * other
            y = self.y
            gcd = math.gcd(x, y)
            return Frac(x // gcd, y // gcd)
        elif isinstance(self, Frac) and isinstance(other, float): #frac1 * float
            a, b = other.as_integer_ratio()
            x = self.x * a
            y = self.y * b
            gcd = math.gcd(x, y)
            return Frac(x // gcd, y // gcd)

    #int*frac
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac): #frac1 / frac2
            return self * ~other
        elif isinstance(self, Frac) and isinstance(other, int): #frac1 / int
            return self * Frac(1, other)
        elif isinstance(self, Frac) and isinstance(other, float): #frac1 / float
            a, b = other.as_integer_ratio()
            return self * Frac(b, a)
        else:
            return Frac()

    def __rtruediv__(self, other): #int/frac
        return other * ~self

    def __pos__(self): #+frac = (+1)*frac
        return self

    def __neg__(self): # -frac = (-1)*frac
        return -1 * self

    def __invert__(self): #odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self): #float(frac)
        return self.x / self.y


def least_common_multiple(a, b):
    return (a * b) // math.gcd(a, b)

def to_common_denominator(frac1, frac2):
    y = least_common_multiple(frac1.y, frac2.y)
    x1 = frac1.x * (y / frac1.y)
    x2 = frac2.x * (y / frac2.y)
    return Frac(x1, y), Frac(x2, y)