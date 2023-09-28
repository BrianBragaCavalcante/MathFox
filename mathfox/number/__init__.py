import mathfox.numis
import decimal
import math


def prime(count):
    """
    :param count: The number of prime numbers
    :return: A list of all desired prime numbers
    """
    prime = []
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
        return decimal.Decimal(str(pi)[:count+2])


def inf():
    """
    :return: The INF
    """
    return math.inf
