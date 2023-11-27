import mathfox.calculation


def sin(num, type='degrees'):
    """
    :param num: The value in degrees of the angle
    :param type: degrees or radian
    :return: The sine of the number
    """
    import math
    if type == 'radian':
        return math.sin(num)
    elif type == 'degrees':
        degreesr = mathfox.calculation.radians(num)
        return mathfox.calculation.geometry.trigonometry.sin(degreesr, 'radians')


def cos(num, type='degrees'):
    """
    :param num: The value in degrees of the angle
    :param type: degrees or radian
    :return: The cosine of the number
    """
    import math
    if type == 'radian':
        return math.cos(num)
    elif type == 'degrees':
        degreesr = mathfox.calculation.radians(num)
        return mathfox.calculation.geometry.trigonometry.cos(degreesr, 'radians')


def tan(num, type='degrees'):
    """
    :param num: The value in degrees of the angle
    :param type: degrees or radian
    :return: The tangent of the number
    """
    import math
    if type == 'radian':
        return math.tan(num)
    elif type == 'degrees':
        degreesr = mathfox.calculation.radians(num)
        return mathfox.calculation.geometry.trigonometry.tan(degreesr, 'radians')


def asin(num, type='degrees'):
    """
    :param num: The value in degrees of the angle
    :param type: degrees or radian
    :return: The arc-sine of the number
    """
    import math
    if type == 'radian':
        return math.asin(num)
    elif type == 'degrees':
        degreesr = mathfox.calculation.radians(num)
        return mathfox.calculation.geometry.trigonometry.asin(degreesr, 'radians')


def acos(num, type='degrees'):
    """
    :param num: The value in degrees of the angle
    :param type: degrees or radian
    :return: The arc-cosine of the number
    """
    import math
    if type == 'radian':
        return math.acos(num)
    elif type == 'degrees':
        degreesr = mathfox.calculation.radians(num)
        return mathfox.calculation.geometry.trigonometry.acos(degreesr, 'radians')


def atan(num):
    """
    :param num: The value in degrees of the angle
    :return: The arc-tangent of the number
    """
    import math
    return math.atan(num)


def csc(num, type='degrees'):
    """
    :param num: The value in degrees of the angle
    :param type: degrees or radian
    :return: The co-secant of the number
    """
    import math
    if type == 'radian':
        return math.sin(num)
    elif type == 'degrees':
        degreesr = 1 / mathfox.calculation.radians(num)
        return 1 / mathfox.calculation.geometry.trigonometry.sin(degreesr, 'radian')


def sec(num, type='degrees'):
    """
    :param num: The value in degrees of the angle
    :param type: degrees or radian
    :return: The secant of the number
    """
    import math
    if type == 'radian':
        return 1 / math.cos(num)
    elif type == 'degrees':
        degreesr = mathfox.calculation.radians(num)
        return 1 / mathfox.calculation.geometry.trigonometry.cos(degreesr, 'radian')


def cot(num, type='degrees'):
    """
    :param num: The value in degrees of the angle
    :param type: degrees or radian
    :return: The co-tangent of the number
    """
    import math
    if type == 'radian':
        return 1 / math.tan(num)
    elif type == 'degrees':
        degreesr = mathfox.calculation.radians(num)
        return 1 / mathfox.calculation.geometry.trigonometry.tan(degreesr, 'radian')
