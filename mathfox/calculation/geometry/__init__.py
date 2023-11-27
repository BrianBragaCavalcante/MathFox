import mathfox.calculation.geometry.trigonometry
import mathfox.calculation.geometry.area


def pythagorean_theorem(a, b):
    """
    :param a: First leg
    :param b: Second leg
    :return: The hypotenuse
    """
    return mathfox.calculation.root(a**2 + b**2, 2)
