def isprime(num):
    """
    :param num: The number to check
    :return: True if the number is prime or False if it is not
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def isint(num, decimal=True):
    """
    :param num: The number to check
    :param decimal: Whether the number can be decimal.
    :return: True if the number is an integer or False if it is not
    """
    if decimal:
        try:
            int(num)
            return True
        except Exception:
            return False
    else:
        try:
            integer = int(num)
            if integer == num:
                return True
            else:
                return False
        except Exception:
            return False


def isfloat(num, comma=False, convert=False, integer=True):
    """
    :param num: The number to check
    :param comma: If the number has a comma
    :param convert: If you want to return the number with a period instead of a comma
    :param integer: Whether the number can be integer.
    :return: True if the number is a decimal number or False if it is not
    """
    if integer:
        try:
            string = str(num)
            liststring = list()
            if comma:
                for i in string:
                    liststring.append(i)
                for p, i in enumerate(liststring):
                    if i == ',':
                        liststring[p] = '.'
                string = ''.join(liststring)

            if convert:
                return True, float(string)
            else:
                return True

        except Exception:
            return False
    else:
        try:
            string = str(num)
            liststring = list()
            if comma:
                for i in string:
                    liststring.append(i)
                for p, i in enumerate(liststring):
                    if i == ',':
                        liststring[p] = '.'
                string = ''.join(liststring)

            if int(string) < float(string):
                if convert:
                    return True, float(string)
                else:
                    return True
            else:
                return False
        except Exception:
            return False
