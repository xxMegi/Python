class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        if not isinstance(c, (int, float)) or not isinstance(n, int):
            raise ValueError("ERROR! Współczynnik musi być liczbą, a stopień musi być liczbą całkowitą!!!")
        if n < 0:
            raise ValueError("ERROR! Stopień wielomianu nie może być ujemny!!!")

        self.size = n + 1       # rozmiar tablicy
        self.a = [0] * self.size
        self.a[n] = c

    def __str__(self):
        return " + ".join(f"{coeff}x^{i}" for i, coeff in enumerate(self.a) if coeff != 0) or "0"

    def __add__(self, other):       # poly1+poly2, poly+liczba
        if isinstance(other, (int, float)):
            result = Poly()
            result.a = self.a[:]
            result.a[0] += other
            return result
        elif isinstance(other, Poly):
            max_len = max(len(self), len(other))
            result = Poly()
            result.a = [0] * max_len
            for i in range(max_len):
                result.a[i] = (self[i] if i < len(self) else 0) + (other[i] if i < len(other) else 0)
            return result
        else:
            return NotImplemented

    __radd__ = __add__      # liczba+poly


    def __sub__(self, other):       # poly1-poly2, poly-liczba
        if isinstance(other, (int, float)):
            return self + (-other)
        elif isinstance(other, Poly):
            max_len = max(len(self), len(other))
            result = Poly()
            result.a = [0] * max_len
            for i in range(max_len):
                result.a[i] = (self[i] if i < len(self) else 0) - (other[i] if i < len(other) else 0)
            return result
        else:
            return NotImplemented

    def __rsub__(self, other):      # liczba-poly
        return (-self) + other

    def __mul__(self, other):       # poly1*poly2, poly*liczba
        if isinstance(other, (int, float)):
            result = Poly()
            result.a = [coeff * other for coeff in self.a]
            return result
        elif isinstance(other, Poly):
            result = Poly()
            result.a = [0] * (len(self) + len(other) - 1)
            for i, coeff1 in enumerate(self.a):
                for j, coeff2 in enumerate(other.a):
                    result.a[i + j] += coeff1 * coeff2
            return result
        else:
            return NotImplemented

    __rmul__ = __mul__      # liczba*poly

    def __pos__(self):      # +poly1 = (+1)*poly1
        return self

    def __neg__(self):      # -poly1 = (-1)*poly1
        result = Poly()
        result.a = [-coeff for coeff in self.a]
        return result
    
    def is_zero(self):      # bool, True dla [0], [0, 0],...
        return all(coeff == 0 for coeff in self.a)
    
    def __eq__(self, other):        # obsługa poly1 == poly2
        if not isinstance(other, Poly):
            return False
        return self.a == other.a
    
    def __ne__(self, other):        # obsługa poly1 != poly2
        return not self == other
    
    def eval(self, x):      # schemat Hornera
        if not isinstance(x, (int, float)):
            raise ValueError("ERROR! Argument musi być liczbą całkowitą lub rzeczywistą!!!")
        result = 0
        for coeff in reversed(self.a):
            result = result * x + coeff
        return result
    
    def combine(self, other):       # złożenie poly1(poly2(x))
        if not isinstance(other, Poly):
            raise ValueError("ERROR! Argument musi być instancją Poly!!!")
        result = Poly()
        for i, coeff in enumerate(self.a):
            result += other ** i * coeff
        return result
    
    def __pow__(self, n):       # poly(x)**n
        if not isinstance(n, int) or n < 0:
            raise ValueError("ERROR! Stopień potęgi musi być nieujemną liczbą całkowitą!!!")
        result = Poly(1, 0)
        for _ in range(n):
            result *= self
        return result
    
    def diff(self):     # różniczkowanie
        result = Poly()
        result.a = [i * self[i] for i in range(1, len(self))]
        return result

    def integrate(self):        # całkowanie
        result = Poly()
        result.a = [0] * (len(self) + 1)
        for i in range(len(self)):
            result.a[i + 1] = self[i] / (i + 1)
        return result
    
    def __len__(self):      # len(poly), rozmiar self.a
        return len(self.a)
    
    def __getitem__(self, i):       # poly[i], współczynnik przy x^i
        if i < 0 or i >= len(self):
            return 0
        return self.a[i]

    def __setitem__(self, i, value):        # poly[i] = value
        if i < 0:
            raise ValueError("ERROR! Indeks nie może być ujemny!!!")
        if i >= len(self):
            self.a.extend([0] * (i - len(self) + 1))
        self.a[i] = value

    def __call__(self, x):      # poly(x)
        # dla isinstance(x, (int,float)) odpowiada eval()
        if isinstance(x, (int, float)):
            return self.eval(x)
        # dla isinstance(x, Poly) odpowiada combine()
        elif isinstance(x, Poly):
            return self.combine(x)
        else:
            raise ValueError("ERROR! Argument musi być liczbą lub wielomianem!!!")

    def __iter__(self):
        return iter(self.a)

    
# Kod testujący moduł.
import unittest

class TestPoly(unittest.TestCase):

    def test_init(self):
        p = Poly(3, 2)
        self.assertEqual(p.a, [0, 0, 3])
        with self.assertRaises(ValueError):
            Poly(2, -1)

    def test_add(self):
        p1 = Poly(3, 2)
        p2 = Poly(4, 0)
        p3 = p1 + p2
        self.assertEqual(p3.a, [4, 0, 3])
        p4 = p1 + 5
        self.assertEqual(p4.a, [5, 0, 3])

    def test_sub(self):
        p1 = Poly(3, 2)
        p2 = Poly(1, 0)
        p3 = p1 - p2
        self.assertEqual(p3.a, [-1, 0, 3])

    def test_mul(self):
        p1 = Poly(3, 2)
        p2 = Poly(2, 1)
        p3 = p1 * p2
        self.assertEqual(p3.a, [0, 0, 0, 6])

    def test_eval(self):
        p = Poly(3, 2) + Poly(2, 0)
        self.assertEqual(p.eval(1), 5)
        self.assertEqual(p.eval(2), 14)

    def test_diff(self):
        p = Poly(3, 2)
        dp = p.diff()
        self.assertEqual(dp.a, [0, 6])

    def test_integrate(self):
        p = Poly(6, 1)
        ip = p.integrate()
        self.assertEqual(ip.a, [0, 0, 3])

    def test_iteration(self):
        p = Poly(3, 2) + Poly(1, 0)
        coeffs = [c for c in p]
        self.assertEqual(coeffs, [1, 0, 3])

    def test_power(self):
        p = Poly(2, 1)
        self.assertEqual((p ** 2).a, [0, 0, 4])

if __name__ == "__main__":
    unittest.main()