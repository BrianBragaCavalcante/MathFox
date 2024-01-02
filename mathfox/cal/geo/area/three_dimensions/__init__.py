import mathfox


def cube(edge):
    """
    Calculates the volume of a cube given its edge length.

    Args:
        edge: The length of one edge of the cube.

    Returns:
        The volume of the cube.

    Raises:
        ValueError: If edge_length is less than or equal to zero.
    """
    if edge <= 0:
        raise ValueError("Edge length must be positive.")
    return edge ** 3


def parallelepiped(height, width, depth):
    """
    Calculates the volume of a parallelepiped given its dimensions.

    Args:
        height: The height of the parallelepiped.
        width: The width of the parallelepiped.
        depth: The depth of the parallelepiped.

    Returns:
        The volume of the parallelepiped.

    Raises:
        ValueError: If any of the dimensions are less than or equal to zero.
    """
    if any(dimension <= 0 for dimension in (height, width, depth)):
        raise ValueError("All dimensions must be positive.")
    return height * width * depth


def cylinder(height, radius):
    """
    Calculates the volume of a cylinder given its height and radius.

    Args:
        height: The height of the cylinder.
        radius: The radius of the cylinder's base.

    Returns:
        The volume of the cylinder.

    Raises:
        ValueError: If height or radius is less than or equal to zero.
    """
    if height <= 0 or radius <= 0:
        raise ValueError("Height and radius must be positive.")
    return mathfox.number.pi() * radius ** 2 * height


def sphere(radius):
    """
    Calculates the volume of a sphere given its radius.

    Args:
        radius: The radius of the sphere.

    Returns:
        The volume of the sphere.

    Raises:
        ValueError: If radius is less than or equal to zero.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return 4 * mathfox.number.pi() * radius ** 2
