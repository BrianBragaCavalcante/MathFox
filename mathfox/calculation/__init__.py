import mathfox
import mathfox.calculation.geometry
import math


def sublist(list):
    """
    :param list: The list you want to subtract.
    :return: The subtracting all numbers from the list.
    """
    sub = list[0]
    for i in list:
        sub -= i
    return sub + list[0]


def multlist(list):
    """
    :param list: The list you want to multiply.
    :return: The multiplying all numbers in the list.
    """
    mult = 1
    for i in list:
        mult *= i
    return mult


def divlist(list):
    """
    :param list: The list you want to divide.
    :return: The division of all numbers in the list.
    """
    div = list[0]
    for i in list:
        div /= i
    return div * list[0]


def medium(*num):
    """
    :param num: The numbers you want to average
    :return: The average of all numbers
    """
    num = list(num)

    for p, n in enumerate(num):
        if type(n) == list or type(n) == tuple:
            for i in num[p]:
                num.append(i)
            del num[p]

    return sum(num) / len(num)


def root(num, ind):
    """
    :param num: Rooting
    :param ind: Index
    :return: Root
    """
    return num ** (1/ind)


def factorial(num):
    """
    :param num: Number
    :return: The factorial of the number
    """
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


def lcm(*num, result=False):
    """
    :param num: Numbers to be factored
    :param result: If set to True, it will return the least common multiple of all numbers together.
    :return: factoring numbers
    """

    num = list(num[:])
    mmc = []
    temp = []
    count = {}
    smash = False

    for p, n in enumerate(num):
        if type(n) == list or type(n) == tuple:
            for i in num[p]:
                num.append(i)
            del num[p]
        else:
            pass

    for i in range(2, max(num)+1):
        if mathfox.numis.isprime(i):
            for n1 in num:
                if n1 % i == 0:
                    while True:
                        mmc.append(i)
                        for p, n2 in enumerate(num):
                            if n2 % i == 0:
                                smash = True
                                num[p] /= i
                        if not smash:
                            break
                        else:
                            smash = False

    for i in mmc:

        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1

    for i in count.keys():
        count[i] -= 1

    for p, i in enumerate(mmc):
        if temp.count(i) == 0:
            temp.append(i)

    for i in temp:
        mmc.remove(i)

    if result:
        count['result'] = multlist(mmc)
        if count['result'] == 1:
            count['result'] = 0

    return count


def gcd(*num, result=False):
    """
    :param num: Numbers to be factored
    :param result: If set to True, it will return the greatest common divisor of all numbers together.
    :return: factoring numbers
    """

    num = list(num[:])
    mdc = []
    count = {}
    mult = 1

    for p, n in enumerate(num):
        if type(n) == list or type(n) == tuple:
            for i in num[p]:
                num.append(i)
            del num[p]

    for i in range(2, max(num)+1):
        if mathfox.numis.isprime(i):
            while True:
                if all(n % i == 0 for n in num):
                    mdc.append(i)
                    for n in range(len(num)):
                        num[n] /= i
                else:
                    break

    for i in mdc:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1

    if result:
        for i in mdc:
            mult *= i
        count['result'] = mult
        if count['result'] == 1:
            count['result'] = 0

    return count


def chance(percentage):
    """
    :param percentage: The chance of something happening
    :return: True if it works or False if it fails
    """
    from random import randint
    if percentage <= randint(1, 100):
        return True
    return False


def radians(num):
    """
    :param num: The number to be converted
    :return: The value in radians
    """
    import math
    return math.radians(num)


def degrees(num):
    """
    :param num: The number to be converted
    :return: The value in degrees
    """
    import math
    return math.degrees(num)

def log(exp, base):
    """
    :param exp: Logarithm
    :param base: The base
    :return:
    """
    if exp > 0 and base > 1:
        import math
        return math.log(exp, base)
    return None


def rule_of_three(a, b, c, invert=False):
    """
    A -- B
    C -- X

    :param a: The A value
    :param b: The B value
    :param c:  The C value
    :param invert: if the rule of three is inversely proportional
    :return: The X value
    """
    return c * b / a if not invert else a * b / c


def bhaskara(a, b, c):
    """
    :param a: The A value
    :param b: The B value
    :param c: The C value
    :return: The value of X1 and X2
    """
    delta = b ** 2 - 4 * a * c
    x1 = ((b * -1) + root(delta, 2)) / (2 * a)
    x2 = ((b * -1) - root(delta, 2)) / (2 * a)
    return x1, x2
