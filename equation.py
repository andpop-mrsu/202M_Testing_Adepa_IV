import math


def find_roots(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return []  # No real roots
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return sorted([root1, root2])

# Example usage:
print(find_roots(1, -3, 2))
