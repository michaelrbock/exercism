import bisect
from collections import defaultdict


class School(object):
  def __init__(self):
    self._children_by_grade = defaultdict(list)

  @property
  def children_by_grade(self):
    raise ValueError('Sorry.')


  def add_student(self, name, grade):
    """Time: O(n * logn) where n = number of children in grade."""
    bisect.insort_left(self._children_by_grade[grade], name)

  def roster(self):
    """Time: O(nlogn) where n = number of grades."""
    result = []
    for grade in sorted(self._children_by_grade):
      result.extend(self._children_by_grade[grade])
    return result

  def grade(self, grade_number):
    """Time: O(1)."""
    return self._children_by_grade[grade_number]
