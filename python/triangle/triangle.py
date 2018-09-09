def _is_triangle(sides):
  return (sum(sides[:2]) > sides[2] and sum(sides[1:]) > sides[0] and
          sides[0] + sides[2] > sides[1])


def is_equilateral(sides):
  return (_is_triangle(sides) and
          (sides[0] == sides[1] and sides[1] == sides[2]))


def is_isosceles(sides):
  return (_is_triangle(sides) and
          (sides[0] == sides[1] or sides[0] == sides[2] or
           sides[1] == sides[2]))


def is_scalene(sides):
  return (_is_triangle(sides) and
          (not is_equilateral(sides) and not is_isosceles(sides)))
