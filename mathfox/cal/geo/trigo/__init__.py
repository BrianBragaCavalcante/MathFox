import mathfox.cal


def sin(num, type='degrees'):
    """
    Calculates the sine of an angle.

    Args:
        num: The angle in either degrees or radians, depending on the angle_type.
        type: Specifies the unit of the angle, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The sine of the angle.

    Raises:
        ValueError: If the angle_type is not 'degrees' or 'radians'.
    """
    import math
    if type.lower() == 'radians':
        return math.sin(num)
    elif type.lower() == 'degrees':
        degreesr = mathfox.cal.radians(num)
        return mathfox.cal.geo.trigo.sin(degreesr, 'radians')
    else:
        raise ValueError("Invalid angle_type. Must be 'degrees' or 'radians'.")


def cos(num, type='degrees'):
    """
    Calculates the cosine of an angle.

    Args:
        num: The angle in either degrees or radians, depending on the angle_type.
        type: Specifies the unit of the angle, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The cosine of the angle.

    Raises:
        ValueError: If the angle_type is not 'degrees' or 'radians'.
    """
    import math
    if type.lower() == 'radians':
        return math.cos(num)
    elif type.lower() == 'degrees':
        degreesr = mathfox.cal.radians(num)
        return mathfox.cal.geo.trigo.cos(degreesr, 'radians')
    else:
        raise ValueError("Invalid angle_type. Must be 'degrees' or 'radians'.")


def tan(num, type='degrees'):
    """
    Calculates the tangent of an angle.

    Args:
        num: The angle in either degrees or radians, depending on the angle_type.
        type: Specifies the unit of the angle, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The tangent of the angle.

    Raises:
        ValueError: If the angle_type is not 'degrees' or 'radians'.
    """
    if not (num == 90 or num == 180 or num == 270):
        if type.lower() == 'radians':
            return mathfox.cal.geo.trigo.sin(num, 'radians')/mathfox.cal.geo.trigo.cos(num, 'radians')
        elif type.lower() == 'degrees':
            degreesr = mathfox.cal.radians(num)
            return mathfox.cal.geo.trigo.tan(degreesr, 'radians')
        else:
            raise ValueError("Invalid angle_type. Must be 'degrees' or 'radians'.")

    
def arcsin(num, type='degrees'):
    """
    Calculates the arc-sine (inverse sine) of a value.

    Args:
        num: The value for which to calculate the arc-sine. Must be between -1 and 1.
        type: Specifies the desired unit of the result, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The arcsine of the value, in the specified result_type.

    Raises:
        ValueError: If the value is outside the valid range of -1 to 1.
        ValueError: If the result_type is not 'degrees' or 'radians'.
    """
    if not -1 <= num <= 1:
        raise ValueError("Value must be between -1 and 1 for arc-sine.")

    import math
    if type.lower() == 'radians':
        return math.asin(num)
    elif type.lower() == 'degrees':
        return mathfox.cal.degrees(mathfox.cal.geo.trigo.arcsin(num, 'radians'))
    else:
        raise ValueError("Invalid result_type. Must be 'degrees' or 'radians'.")


def arccos(num, type='degrees'):
    """
    Calculates the arc-cosine (inverse cosine) of a value.

    Args:
        num: The value for which to calculate the arc-cosine. Must be between -1 and 1.
        type: Specifies the desired unit of the result, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The arc-cosine of the value, in the specified result_type.

    Raises:
        ValueError: If the value is outside the valid range of -1 to 1.
        ValueError: If the result_type is not 'degrees' or 'radians'.
    """
    if not -1 <= num <= 1:
        raise ValueError("Value must be between -1 and 1 for arccosine.")

    import math
    if type.lower() == 'radians':
        return math.acos(num)
    elif type.lower() == 'degrees':
        return mathfox.cal.degrees(mathfox.cal.geo.trigo.arccos(num, 'radians'))
    else:
        raise ValueError("Invalid result_type. Must be 'degrees' or 'radians'.")


def arctan(num, type='degrees'):
    """
    Calculates the arc-tangent (inverse tangent) of a value.

    Args:
        num: The value for which to calculate the arc-tangent.
        type: Specifies the desired unit of the result, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The arc-tangent of the value, in the specified result_type.

    Raises:
        ValueError: If the result_type is not 'degrees' or 'radians'.
    """
    import math
    if type.lower() == 'radians':
        return math.atan(num)
    elif type.lower() == 'degrees':
        return mathfox.cal.degrees(mathfox.cal.geo.trigo.arctan(num, 'radians'))
    else:
        raise ValueError("Invalid result_type. Must be 'degrees' or 'radians'.")


def csc(num, type='degrees'):
    """
    Calculates the co-secant of an angle.

    Args:
        num: The angle in either degrees or radians, depending on the angle_type.
        type: Specifies the unit of the angle, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The co-secant of the angle.

    Raises:
        ValueError: If the angle is 0, resulting in division by zero.
        ValueError: If the angle_type is not 'degrees' or 'radians'.
    """
    if num == 0:
        raise ValueError("Cannot calculate co-secant of 0 degrees or radians.")

    import math
    if type.lower() == 'radians':
        return 1 / math.sin(num)
    elif type.lower() == 'degrees':
        degreesr = mathfox.cal.radians(num)
        return 1 / mathfox.cal.geo.trigo.sin(degreesr, 'radians')
    else:
        raise ValueError("Invalid angle_type. Must be 'degrees' or 'radians'.")


def sec(num, type='degrees'):
    """
    Calculates the secant of an angle.

    Args:
        num: The angle in either degrees or radians, depending on the angle_type.
        type: Specifies the unit of the angle, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The secant of the angle.

    Raises:
        ValueError: If the angle is 90 degrees or multiples of 180 degrees (pi radian),
                     resulting in division by zero.
        ValueError: If the angle_type is not 'degrees' or 'radians'.
    """
    import math
    if type.lower() == 'radians' and (num % math.pi == math.pi / 2):
        raise ValueError("Cannot calculate secant of 90 degrees or odd multiples of 90 degrees.")
    elif type.lower() == 'degrees' and (num % 180 == 90):
        raise ValueError("Cannot calculate secant of 90 degrees or odd multiples of 90 degrees.")

    if type.lower() == 'radians':
        return 1 / math.cos(num)
    elif type.lower() == 'degrees':
        degreesr = mathfox.cal.radians(num)
        return 1 / mathfox.cal.geo.trigo.cos(degreesr, 'radians')
    else:
        raise ValueError("Invalid angle_type. Must be 'degrees' or 'radians'.")


def cot(num, type='degrees'):
    """
    Calculates the cotangent of an angle.

    Args:
        num: The angle in either degrees or radians, depending on the angle_type.
        type: Specifies the unit of the angle, either 'degrees' or 'radians'.
                   Defaults to 'degrees'.

    Returns:
        The cotangent of the angle.

    Raises:
        ValueError: If the angle is 0 degrees or multiples of 180 degrees (pi radian),
                     resulting in division by zero.
        ValueError: If the angle_type is not 'degrees' or 'radians'.
    """
    if num == 0:
        raise ValueError("Cannot calculate cotangent of 0 degrees or radians.")

    import math
    if type.lower() == 'radians':
        return 1 / math.tan(num)
    elif type.lower() == 'degrees':
        degreesr = mathfox.cal.radians(num)
        return 1 / mathfox.cal.geo.trigo.tan(degreesr, 'radians')
    else:
        raise ValueError("Invalid angle_type. Must be 'degrees' or 'radians'.")
