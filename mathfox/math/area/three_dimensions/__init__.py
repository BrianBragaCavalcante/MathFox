import mathfox


def cube(edge):
    """
    :param edge: The size of the cube edge
    :return: The area of the cube
    """
    return edge ** 3


def parallelepiped(height, width, depth):
    """
    :param height: The size of the height
    :param width: The size of the width
    :param depth:  The size of the depth
    :return: The area of the parallelepiped
    """
    return height * width * depth


def cylinder(height, radius):
    """

    :param height: The size of the height
    :param radius: The size of the cylinder's radius
    :return: The area of the cylinder
    """
    return mathfox.number.pi() * radius ** 2 * height


def sphere(radius):
    """
    :param radius: he size of the sphere's radius
    :return: The area of the sphere
    """
    return 4 * mathfox.number.pi() * radius ** 2
