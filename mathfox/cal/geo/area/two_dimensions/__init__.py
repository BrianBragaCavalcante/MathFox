import mathfox


def square(side):
    """
    Calculates the area of a square given its side length.

    Args:
        side: The length of one side of the square.

    Returns:
        The area of the square.

    Raises:
        ValueError: If side_length is less than or equal to zero.
    """

    if side <= 0:
        raise ValueError("Side length must be positive.")
    return side ** 2


def rectangle(height, base):
    """
    Calculates the area of a rectangle given its height and base.

    Args:
        height: The height of the rectangle.
        base: The base of the rectangle.

    Returns:
        The area of the rectangle.

    Raises:
        ValueError: If height or base is less than or equal to zero.
    """
    if height <= 0 or base <= 0:
        raise ValueError("Height and base must be positive.")
    return height * base


def right_triangle(height, base):
    """
    Calculates the area of a right triangle given its height and base.

    Args:
        height: The height of the triangle.
        base: The base of the triangle.

    Returns:
        The area of the triangle.

    Raises:
        ValueError: If height or base is less than or equal to zero.
    """
    if height <= 0 or base <= 0:
        raise ValueError("Height and base must be positive.")
    return base * height / 2


def equilateral_triangle(side):
    """
    Calculates the area of an equilateral triangle given its side length.

    Args:
        side: The length of one side of the equilateral triangle.

    Returns:
        The area of the equilateral triangle.

    Raises:
        ValueError: If side_length is less than or equal to zero.
    """
    if side <= 0:
        raise ValueError("Side length must be positive.")
    return side ** 2 * mathfox.cal.root(3, 2) / 4


def pentagon(side):
    """
    Calculates the area of a regular pentagon given its side length.

    Args:
        side: The length of one side of the pentagon.

    Returns:
        The area of the pentagon.

    Raises:
        ValueError: If side_length is less than or equal to zero.
    """
    if side <= 0:
        raise ValueError("Side length must be positive.")
    tan36 = 0.72654252800536088589546675748062
    return (5 * (side ** 2)) / (4 * tan36)


def hexagon(side):
    """
    Calculates the area of a regular hexagon given its side length.

    Args:
        side: The length of one side of the hexagon.

    Returns:
        The area of the hexagon.

    Raises:
        ValueError: If side_length is less than or equal to zero.
    """
    if side <= 0:
        raise ValueError("Side length must be positive.")
    tan30 = 0.57735026918962576450914878050196
    return (6 * (side ** 2)) / (4 * tan30)


def polygon(side, sides):
    """
    Calculates the area of a regular polygon given its side length and number of sides.

    Args:
        side: The length of one side of the polygon.
        sides: The number of sides in the polygon.

    Returns:
        The area of the polygon.

    Raises:
        ValueError: If side_length or num_sides are less than or equal to zero, or if num_sides is not an integer.
    """
    if side <= 0 or sides <= 0:
        raise ValueError("Side length and number of sides must be positive.")
    if not isinstance(sides, int):
        raise ValueError("Number of sides must be an integer.")
    return (side ** 2 * sides) / (4 * mathfox.cal.geo.trigo.tan(float(mathfox.number.pi()) / sides, 'radians'))


def circle(radius):
    """
    Calculates the area of a circle given its radius.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.

    Raises:
        ValueError: If radius is less than or equal to zero.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return mathfox.number.pi() * radius ** 2

