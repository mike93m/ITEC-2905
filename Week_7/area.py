# Function for calculating the area of a triangle

def triangle_area(base, height):
    """Calculate the area of a triangle given its base and height.
    Raises ValueError for negative base or height."""
    if base < 0 or height < 0:
        raise ValueError("Base and height must be a positive number.")
    return 0.5 * base * height