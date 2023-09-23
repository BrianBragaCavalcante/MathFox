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


def isint(num):
    """
    :param num: The number to check
    :return: True if the number is an integer or False if it is not
    """
    try:
        int(num)
        return True
    except Exception:
        return False


def isfloat(num, comma=False, convert=False):
    """
    :param num: The number to check
    :param comma: If the number has a comma
    :param convert: If you want to return the number with a period instead of a comma
    :return: True if the number is a decimal number or False if it is not
    """
    try:
        string = str(num)
        lista = list()
        if comma:
            for i in string:
                lista.append(i)
            for p, i in enumerate(lista):
                if i == ',':
                    lista[p] = '.'
            string = ''.join(lista)

        if convert:
            return True, float(string)
        else:
            return True

    except Exception:
        return False
