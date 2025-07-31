def is_valid_triangle(sides):
    a, b, c = sides
    return all(x > 0 for x in sides) and (a + b >= c and a + c >= b and b + c >= a)


def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b or a == c or b == c


def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a != b and a != c and b != c
