import mathfox.cal.geo.trigo
import mathfox.cal.geo.area


def hypotenuse(leg1, leg2):
    """
    Calculates the hypotenuse of a right triangle given its two legs using the Pythagorean theorem.

    Args:
        leg1: The length of the first leg of the triangle.
        leg2: The length of the second leg of the triangle.

    Returns:
        The length of the hypotenuse.

    Raises:
        ValueError: If leg1 or leg2 is less than or equal to zero.
    """
    if leg1 <= 0 or leg2 <= 0:
        raise ValueError("Leg lengths must be positive.")
    return mathfox.cal.root(leg1**2 + leg2**2, 2)
