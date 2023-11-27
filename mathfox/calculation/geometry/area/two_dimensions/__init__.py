import mathfox


def square(side):
    """
    :param side: The size of the side of the square
    :return: The area of the cube
    """
    return side ** 2


def rectangle(height, base):
    """
    :param height: The height of the rectangle
    :param base: The base of the rectangle
    :return: The area of the rectangle
    """
    return height * base


def right_triangle(height, base):
    """
    :param height: The height of the right triangle
    :param base: The base of the right_triangle
    :return: The area of the right_triangle
    """
    return base * height / 2


def equilateral_triangle(side):
    """
    :param side: The size of the side of the square equilateral triangle
    :return: The area of the equilateral triangle
    """
    return side ** 2 * mathfox.calculation.root(3, 2) / 4


def pentagon(side):
    """
    :param side: The size of the side of the pentagon
    :return: The area of the pentagon
    """
    tan36 = 0.72654252800536088589546675748062
    return (5 * (side ** 2)) / (4 * tan36)


def hexagon(side):
    """
    :param side: The size of the side of the hexagon
    :return: The area of the hexagon
    """
    tan30 = 0.57735026918962576450914878050196
    return (6 * (side ** 2)) / (4 * tan30)


def polygon(side, sides):
    """
    :param side: How many sides does the polygon have
    :param sides: The size of the side of the polygon
    :return:
    """
    return (side ** 2 * sides) / (4 * mathfox.calculation.geometry.trigonometry.tan(mathfox.number.pi() / sides))


def circle(radius):
    """
    :param radius: The size of the circle's radius
    :return: The area of the o circle
    """
    return mathfox.number.pi() * radius ** 2

