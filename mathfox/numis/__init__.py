def isprime(num):
    """
    Determines whether a given number is prime.

    Args:
        num: The integer to check for primality.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def isint(num, decimal=True):
    """
    Determines whether a given number is an integer (whole number).

    Args:
        num: The number to check.
        decimal: If True, allows for decimal numbers that are equivalent to integers
                       (e.g., 3.0 would be considered an integer). Defaults to False.

    Returns:
        True if the number is an integer, False otherwise.
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


def isdecimal(num, comma=False, convert=False, integer=True, decimal_places=False):
    """
    Determines whether a given string represents a decimal number.

    Args:
        num: The string to check.
        comma: If True, allows for commas as decimal separators. Defaults to True.
        convert: If True, converts commas to periods in the returned value.
                 Defaults to False.
        integer: If True, allows for whole numbers without a decimal point.
                 Defaults to False.
        decimal_places: If True, returns the number of decimal places in the number.
                 Defaults to False.

    Returns:
        True if the string is a decimal number, False otherwise.
        If convert_comma_to_period is True, returns the converted number as a float.
        If return_decimal_places is True, returns the number of decimal places as an int.
    """
    returns = []
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
                cstring = ''.join(liststring)
            else:
                cstring = str(num)

            if convert:
                returns.append(True)
                returns.append(float(cstring))
                if decimal_places:
                    string = str(cstring)
                    for p, i in enumerate(string):
                        if i == '.':
                            returns.append(len(string)-1-p)
                            break
                        if p == len(string) - 1:
                            returns.append(0)
                            break
            else:
                returns.append(True)
                if decimal_places:
                    string = str(cstring)
                    for p, i in enumerate(string):
                        if i == '.':
                            returns.append(len(string)-1-p)
                            break
                        if p == len(string) - 1:
                            returns.append(0)
                            break

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
                cstring = ''.join(liststring)
            else:
                cstring = str(num)

            if int(float(cstring)) < float(cstring):
                if convert:
                    returns.append(True)
                    returns.append(float(string))
                    if decimal_places:
                        string = str(cstring)
                        for p, i in enumerate(string):
                            if i == '.':
                                returns.append(len(string)-1-p)
                                break
                            if p == len(string) - 1:
                                returns.append(0)
                                break

                else:
                    returns.append(True)
                    if decimal_places:
                        string = str(cstring)
                        for p, i in enumerate(string):
                            if i == '.':
                                returns.append(len(string)-1-p)
                                break
                            if p == len(string) - 1:
                                returns.append(0)
                                break
            else:
                return False
        except Exception:
            return False
    if len(returns) > 1:
        return returns

    else:
        return returns[0]
