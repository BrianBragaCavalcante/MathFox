import mathfox
import decimal
import math


inf = math.inf


def prime(count):
    """
    :param count: The number of prime numbers
    :return: A list of all desired prime numbers
    """
    prime = list()
    num = 2
    while len(prime) < count:
        if mathfox.numis.isprime(num):
            prime.append(num)
        num += 1
    return prime


def pi(count=48):
    """
    :param count: The number of places after the decimal point
    :return: The PI value
    """
    decimal.getcontext().prec = 48
    pi = decimal.Decimal(3.141592653589793238462643383279502884197169399375)
    if count > 48:
        return None
    else:
        return decimal.Decimal(str(pi)[:count + 2])


def e(count=48):
    """
    :param count: The number of places after the decimal point
    :return: The e value
    """
    decimal.getcontext().prec = 48
    e = decimal.Decimal(2.718281828459045235360287471352662497757247093699)
    if count > 48:
        return None
    else:
        return decimal.Decimal(str(e)[:count + 2])


class Fraction:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

        if self.denominator == 0:
            raise ValueError("Cannot divide by zero.")

        if type(self.numerator) == float:
            _, h = mathfox.numis.isdecimal(self.numerator, decimal_places=True)

            self.numerator = int(int(f'1{"0"*h}') * self.numerator)
            self.denominator = int(int(f'1{"0"*h}') * self.denominator)
            self.simplification()

        if type(self.denominator) == float:
            _, h = mathfox.numis.isdecimal(self.denominator, decimal_places=True)

            self.numerator = int(int(f'1{"0" * h}') * self.numerator)
            self.denominator = int(int(f'1{"0" * h}') * self.denominator)
            self.simplification()

        self.result = self.numerator / self.denominator

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def __int__(self):
        return int(self.result)

    def __float__(self):
        return self.result

    def __iter__(self):
        return [self.numerator, self.denominator]

    def __repr__(self):
        return f'Fraction("{self.numerator}, {self.denominator}")'

    def __add__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result + other.result)
        else:
            Fraction(self.result + other)

    def __sub__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result - other.result)
        else:
            return Fraction(self.result - other)

    def __mul__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result * other.result)
        else:
            return Fraction(self.result * other)

    def __truediv__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result / other.result)
        else:
            return Fraction(self.result / other)

    def __floordiv__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result // other.result)
        else:
            return Fraction(self.result // other)

    def __mod__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result % other.result)
        else:
            return Fraction(self.result % other)

    def __divmod__(self, other):
        if type(other) == Fraction:
            return self.result // other.result, self.result % other.result
        else:
            return self.result // other, self.result % other

    def __pow__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result ** other.result)
        else:
            return Fraction(self.result ** other)

    def __invert__(self):
        return Fraction(self.numerator * -1, self.denominator * -1)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __lt__(self, other):
        if type(other) == Fraction:
            return True if self.result < other.result else False
        else:
            return True if self.result < other else False

    def __le__(self, other):
        if type(other) == Fraction:
            return True if self.result <= other.result else False
        else:
            return True if self.result <= other else False

    def __eq__(self, other):
        if type(other) == Fraction:
            return True if self.result == other.result else False
        else:
            return True if self.result == other else False

    def __ne__(self, other):
        if type(other) == Fraction:
            return True if self.result != other.result else False
        else:
            return True if self.result != other else False

    def __ge__(self, other):
        if type(other) == Fraction:
            return True if self.result >= other.result else False
        else:
            return True if self.result >= other else False

    def __gt__(self, other):
        if type(other) == Fraction:
            return True if self.result > other.result else False
        else:
            return True if self.result > other else False

    def __getitem__(self, idx):
        if idx == 0:
            return self.numerator
        if idx == 1:
            return self.denominator

    def __setitem__(self, idx, value):
        if idx == 0:
            self.numerator = value
            if type(self.numerator) == float:
                _, h = mathfox.numis.isdecimal(self.numerator, decimal_places=True)

                self.numerator = int(int(f'1{"0"*h}') * self.numerator)
                self.denominator = int(int(f'1{"0"*h}') * self.denominator)
                self.simplification()
        if idx == 1:
            if type(self.denominator) == float:
                _, h = mathfox.numis.isdecimal(self.denominator, decimal_places=True)

                self.numerator = int(int(f'1{"0" * h}') * self.numerator)
                self.denominator = int(int(f'1{"0" * h}') * self.denominator)
                self.simplification()

        self.result = self.numerator / self.denominator

    def simplification(self):
        gcd = mathfox.calculation.gcd(self.numerator, self.denominator, result=True)
        try:
            self.numerator /= gcd['result']
            self.denominator /= gcd['result']
            self.numerator = int(self.numerator)
            self.denominator = int(self.denominator)
        except Exception:
            pass

    def invert(self):
        numerator = self.numerator
        denominator = self.denominator

        self.numerator = denominator
        self.denominator = numerator
