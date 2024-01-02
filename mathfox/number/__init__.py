import mathfox
import math

inf = math.inf


def prime(count):
    """
    Generates a list of the first `count` prime numbers.

    Args:
        count: The number of prime numbers to generate.

    Returns:
        A list containing the first `count` prime numbers.

    Raises:
        ValueError: If `count` is less than or equal to 0.
    """
    if count <= 0:
        raise ValueError("count must be a positive integer.")

    prime = list()
    num = 2
    while len(prime) < count:
        if mathfox.numis.isprime(num):
            prime.append(num)
        num += 1
    return prime


def pi(precision=48):
    """
    Calculates the value of pi to a specified precision.

    Args:
        precision: The desired number of decimal places for pi.
                   Defaults to 48.

    Returns:
        The value of pi as a Decimal object with the specified precision.

    Raises:
        ValueError: If precision is less than or equal to 0.
    """
    import decimal
    decimal.getcontext().prec = 48
    pi = decimal.Decimal(3.141592653589793238462643383279502884197169399375)
    if precision > 48:
        return None
    else:
        return decimal.Decimal(str(pi)[:precision + 2])


def e(precision=48):
    """
    :param precision: The number of places after the decimal point
    :return: The e value
    """
    import decimal
    decimal.getcontext().prec = 48
    e = decimal.Decimal(2.718281828459045235360287471352662497757247093699)
    if precision > 48:
        return None
    else:
        return decimal.Decimal(str(e)[:precision + 2])


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

    def __rsub__(self, other):
        if type(other) == Fraction:
            return Fraction(other.result - self.result)
        else:
            return Fraction(other - self.result)

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

    def __rtruediv__(self, other):
        if type(other) == Fraction:
            return Fraction(other.result / self.result)
        else:
            return Fraction(other / self.result)

    def __floordiv__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result // other.result)
        else:
            return Fraction(self.result // other)

    def __rfloordiv__(self, other):
        if type(other) == Fraction:
            return Fraction(other.result // self.result)
        else:
            return Fraction(other // self.result)

    def __mod__(self, other):
        if type(other) == Fraction:
            return Fraction(self.result % other.result)
        else:
            return Fraction(self.result % other)

    def __rmod__(self, other):
        if type(other) == Fraction:
            return Fraction(other.result % self.result)
        else:
            return Fraction(other % self.result)

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

    def __rpow__(self, other):
        if type(other) == Fraction:
            return Fraction(other.result ** self.result)
        else:
            return Fraction(other ** self.result)

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
        gcd = mathfox.cal.gcd(self.numerator, self.denominator, result=True)
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


class Decimal:
    def __init__(self, num, comma='.', separator=''):

        self.comma = str(comma)
        self.separator = str(separator)
        self.num = str(num)
        self.numinit = str(num)

        for _ in self.num:
            if self.num.find('0') == 0:
                self.num = list(self.num)
                self.num.pop(0)
                self.num = ''.join(self.num)
            else:
                break

        for _ in self.num:
            if self.num.rfind('0') == len(self.num) - 1 and not self.num[-2] == self.separator:
                self.num = list(self.num)
                self.num.pop(-1)
                self.num = ''.join(self.num)
            else:
                break

        self.strint = list()
        self.strdecimal = list()

        for p, n in enumerate(list(self.num)):
            if n == '.':
                for i in list(self.num)[:p]:
                    self.strint.append(i)

                for i in list(self.num)[p + 1:]:
                    self.strdecimal.append(i)

        for i in range(len(self.strint), 0, -3):
            self.strint.insert(i, self.separator)

        self.strint = list(self.strint)
        self.strint.pop()
        self.strint = ''.join(self.strint)

        n = 0
        for i in range(3, len(self.strdecimal), 3):
            self.strdecimal.insert(i + n, self.separator)
            n += 1

    def __str__(self):
        return ''.join(self.strint) + self.comma + ''.join(self.strdecimal)

    def __repr__(self):
        return f'Decimal({self.numinit}, {self.comma} , {self.separator})'

    def __int__(self):
        return int(self.numinit)

    def __float__(self):
        return float(self.numinit)

    def __len__(self):
        num = list(self.numinit)
        num.pop(self.numinit.find('.'))
        return len(num)

    def __neg__(self):
        return Decimal({-self.numinit}, {self.comma} , {self.separator})
