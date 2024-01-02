import mathfox
import mathfox.cal.geo


def sublist(list):
    """
    Subtracts all numbers in a list from the first number in the list,
    returning the final difference.

    Args:
        list: The list of numbers to be subtracted.

    Returns:
        The result of subtracting all numbers in the list from the first number.

    Raises:
        ValueError: If the input list is empty.
    """
    if not list:
        raise ValueError("Cannot subtract from an empty list.")

    sub = list[0]
    for i in list:
        sub -= i
    return sub + list[0]


def multlist(list):
    """
    Multiplies all numbers in a list together, returning the product.

    Args:
        list: The list of numbers to be multiplied.

    Returns:
        The product of all numbers in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not list:
        raise ValueError("Cannot multiply an empty list.")
    mult = 1
    for i in list:
        mult *= i
    return mult


def divlist(list):
    """
    Divides the first number in the list by all subsequent numbers,
    returning the final quotient.

    Args:
        list: The list of numbers to be divided.

    Returns:
        The result of dividing the first number in the list by all subsequent numbers.

    Raises:
        ValueError: If the input list is empty or contains a zero.
        ZeroDivisionError: If a zero is encountered during division.
    """

    div = list[0]
    for i in list:
        if i == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        div /= i
    return div * list[0]


def mean(*num):
    """
    Calculates the mean (average) of a variable number of numbers,
    supporting iterables like lists and tuples.

    Args:
        *num: The numbers to be averaged. Can be individual numbers,
                  lists, tuples, or any iterable of numbers.

    Returns:
        The mean of all the numbers.

    Raises:
        ValueError: If no numbers are provided.
    """
    num = list(num)
    if not num:
        raise ValueError("Cannot calculate mean of empty list.")

    numlist = []

    for p, n in enumerate(num):
        if isinstance(n, (list, tuple)):
            for i in num[p]:
                numlist.append(i)
        else:
            numlist.append(n)

    return sum(numlist) / len(numlist)


def median(*num):
    """
    Calculates the median of a variable number of numbers,
    supporting iterables like lists and tuples.

    Args:
        *num: The numbers to be used to calculate the median.
                  Can be individual numbers, lists, tuples, or any iterable of numbers.

    Returns:
        The median of all the numbers.

    Raises:
        ValueError: If no numbers are provided.
    """

    num = list(num)
    if not num:
        raise ValueError("Cannot calculate median of empty list.")

    numlist = []

    for p, n in enumerate(num):
        if isinstance(n, (list, tuple)):
            for i in num[p]:
                numlist.append(i)
        else:
            numlist.append(n)

    numlist.sort()

    return int(mean(numlist[int(len(numlist)/2)], numlist[int(len(numlist)/2-1)])) \
        if len(numlist) % 2 == 0 else numlist[int(len(numlist)/2-0.5)]


def mode(*num):
    """
    Calculates the mode (most frequent value) of a variable number of numbers,
    supporting iterables like lists and tuples.

    Args:
        *num: The numbers to find the mode of. Can be individual numbers,
                  lists, tuples, or any iterable of numbers.

    Returns:
        A list containing the mode(s) of the numbers. If there are multiple
        modes, all of them are returned. If there is no mode (all numbers
        have the same frequency), an empty list is returned.

    Raises:
        ValueError: If no numbers are provided.
    """

    num = list(num)
    if not num:
        raise ValueError("Cannot calculate mode of empty list.")
    dic = {}
    result = []
    numlist = []

    for p, n in enumerate(num):
        if isinstance(n, (list, tuple)):
            for i in num[p]:
                numlist.append(i)
        else:
            numlist.append(n)

    numlist.sort()

    for i in numlist:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1

    result += [i for i in dic.keys() if dic[i] == max(dic.values())]

    if len(result) == 1:
        result = result[0]
    return result


def std(*num):
    """
    Calculates the standard deviation of a variable number of numbers,
    supporting iterables like lists and tuples.

    Args:
        *num: The numbers to calculate the standard deviation of.
                  Can be individual numbers, lists, tuples, or any iterable of numbers.

    Returns:
        The standard deviation of the numbers.

    Raises:
        ValueError: If no numbers are provided.
    """
    num = list(num)
    if not num:
        raise ValueError("Cannot calculate standard deviation of empty list.")

    numlist = []

    for p, n in enumerate(num):
        if isinstance(n, (list, tuple)):
            for i in num[p]:
                numlist.append(i)
        else:
            numlist.append(n)
    num = numlist

    micro = mean(numlist)
    module = [(i - micro)**2 for i in num]
    return root(sum(module)/len(numlist), 2)


def var(*num):
    """
        Calculates the variance of a list of numbers.

        Args:
            *num: A list of numbers or nested iterables containing numbers.

        Returns:
            The variance of the numbers.

        Raises:
            ValueError: If the input is empty.
        """
    if not num:
        raise ValueError("Cannot calculate variance of empty list.")

    num = list(num)
    if not num:
        raise ValueError("Cannot calculate variance of empty list.")
    numlist = []

    for p, n in enumerate(num):
        if isinstance(n, (list, tuple)):
            for i in num[p]:
                numlist.append(i)
        else:
            numlist.append(n)

    num = numlist

    mean = mathfox.cal.mean(num)
    var = [(subnum - mean)**2 for subnum in num]
    var = sum(var)

    return var/len(num)


def root(num, ind):
    """
    Calculates the root of a number with a given index.

    Args:
        num: The number to take the root of.
        ind: The index of the root to calculate.

    Returns:
        The root of the number with the given index.

    Raises:
        ValueError: If the index is zero.
        ZeroDivisionError: If the number is zero and the index is negative.
    """
    if ind == 0:
        raise ValueError("Cannot calculate root with index zero.")
    if num == 0 and ind < 0:
        raise ZeroDivisionError("Cannot calculate zeroth root of zero.")

    return num ** (1 / ind)


def factorial(num):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        num: The non-negative integer for which to calculate the factorial.

    Returns:
        The factorial of the number.

    Raises:
        ValueError: If the number is negative.
    """

    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if num == 0:
        return 1

    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


def lcm(*num, result=False):
    """
    Calculates the prime factorization of numbers and optionally the least common multiple (LCM).

    Args:
        *num: The numbers to factor and find the LCM of.
                  Can be individual numbers, lists, tuples, or any iterable of numbers.
        result: If True, returns the LCM in addition to the factorization.
                Defaults to False.

    Returns:
        A dictionary containing the prime factorization of each number, with primes as keys and their
        exponents as values. If `result` is True, also includes a 'result' key with the LCM.

    Raises:
        ValueError: If any of the input numbers are not positive integers.
    """

    num = list(num)
    numtemp = []
    lcm = []
    temp = []
    count = {}
    smash = False

    for p, n in enumerate(num):
        if isinstance(n, (list, tuple)):
            for i in num[p]:
                numtemp.append(i)
        else:
            numtemp.append(n)

    num = numtemp

    for i in num:
        if not isinstance(i, int) or i <= 0:
            raise ValueError("Input numbers must be positive integers.")

    for i in range(2, max(num) + 1):
        if mathfox.numis.isprime(i):
            for n1 in num:
                if n1 % i == 0:
                    while True:
                        lcm.append(i)
                        for p, n2 in enumerate(num):
                            if n2 % i == 0:
                                smash = True
                                num[p] /= i
                        if not smash:
                            break
                        else:
                            smash = False

    for i in lcm:

        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1

    for i in count.keys():
        count[i] -= 1

    for p, i in enumerate(lcm):
        if temp.count(i) == 0:
            temp.append(i)

    for i in temp:
        lcm.remove(i)

    if result:
        count['result'] = multlist(lcm)
        if count['result'] == 1:
            count['result'] = 0

    return count


def gcd(*num, result=False):
    """
    Calculates the prime factorization of numbers and optionally the greatest common divisor (GCD).

    Args:
        *num: The numbers to factor and find the GCD of.
                  Can be individual numbers, lists, tuples, or any iterable of numbers.
        result: If True, returns the GCD in addition to the factorization.
                Defaults to False.

    Returns:
        A dictionary containing the prime factorization of each number, with primes as keys and their
        exponents as values. If `result` is True, also includes a 'result' key with the GCD.

    Raises:
        ValueError: If any of the input numbers are not positive integers.
    """

    num = list(num)
    numtemp = []
    gcd = []
    count = {}
    mult = 1

    for p, n in enumerate(num):
        if type(n) == list or type(n) == tuple:
            for i in num[p]:
                numtemp.append(i)
        else:
            numtemp.append(n)

    num = numtemp

    for i in num:
        if not isinstance(i, int) or i <= 0:
            raise ValueError("Input numbers must be positive integers.")

    for i in range(2, max(num) + 1):
        if mathfox.numis.isprime(i):
            while True:
                if all(n % i == 0 for n in num):
                    gcd.append(i)
                    for n in range(len(num)):
                        num[n] /= i
                else:
                    break

    for i in gcd:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1

    if result:
        for i in gcd:
            mult *= i
        count['result'] = mult
        if count['result'] == 1:
            count['result'] = 0

    return count


def chance(percentage):
    """
    Determines whether an event occurs based on a given percentage chance.

    Args:
        percentage: The percentage chance of the event occurring, as an integer between 0 and 100.

    Returns:
        True if the event occurs, False otherwise.

    Raises:
        ValueError: If the percentage is not a valid integer between 0 and 100.
    """
    import random
    if not isinstance(percentage, (int, float)):
        raise ValueError("Percentage must be an integer.")
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")

    random_number = random.randint(1, 100)
    return percentage <= random_number


def radians(num):
    """
    Converts an angle from degrees to radians.

    Args:
        num: The angle in degrees.

    Returns:
        The angle in radians.

    Raises:
        ValueError: If the input is not a numerical value.
    """
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a numerical value.")
    import math
    return math.radians(num)


def degrees(num):
    """
    Converts an angle from radians to degrees.

    Args:
        num: The angle in radians.

    Returns:
        The angle in degrees.

    Raises:
        ValueError: If the input is not a numerical value.
    """
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a numerical value.")

    import math
    return math.degrees(num)


def log(exp, base):
    """
    Calculates the logarithm of a number with a given base.

    Args:
        exp: The number (argument) of the logarithm.
        base: The base of the logarithm.

    Returns:
        The logarithm of exp to the base, or None if the cal is undefined.

    Raises:
        ValueError: If the base is not positive or not equal to 1.
        ValueError: If the argument is not positive.
    """
    if base <= 1:
        raise ValueError("Base must be positive and not equal to 1.")
    if exp <= 0:
        raise ValueError("Argument must be positive.")
    import math
    return math.log(exp, base)


def rule_of_three(a, b, c, invert=False):
    """
    Calculates the unknown value X in a rule of three proportion.

    A -- C
    B -- X

    Args:
        a: The first known value.
        b: The second known value, corresponding to a.
        c: The third known value, corresponding to the unknown value X.
        invert: If True, calculates an inverse proportion. Defaults to False.

    Returns:
        The calculated value of X.

    Raises:
        ZeroDivisionError: If a or c is zero, resulting in division by zero.
        ValueError: If any of the input values are not numerical.
    """
    if not all(isinstance(value, (int, float)) for value in (a, b, c)):
        raise ValueError("Input values must be numerical.")

    if a == 0 or c == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return c * b / a if not invert else a * b / c


def bhaskara(a, b, c):
    """
    :param a: The A value
    :param b: The B value
    :param c: The C value
    :return: The value of X1 and X2
    """
    if a == 0:
        raise ValueError("The equation is not quadratic (a cannot be zero).")

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return "Equation has no real roots."

    x1 = ((b * -1) + root(delta, 2)) / (2 * a)
    x2 = ((b * -1) - root(delta, 2)) / (2 * a)
    return x1, x2


def array(function, scale, init_attribute, end_attribute):

    if len(init_attribute) != len(end_attribute):
        raise ValueError("`init_attribute` e `end_attribute` devem ter o mesmo comprimento.")

    array = list()

    attribute = list(init_attribute)
    increment = [(end_attribute[p] - init_attribute[p]) / (scale - 1) for p, i in enumerate(init_attribute) if isinstance(i, (int, float))]

    for _ in range(scale):
        array.append(function(*attribute))
        for p, i in enumerate(attribute):
            if isinstance(i, (int, float)):
                attribute[p] += increment[p]
    return array

