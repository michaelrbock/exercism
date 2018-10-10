from collections import defaultdict

_CODE_TO_PLANT = {'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}


class Garden(object):

  def __init__(self, diagram, students=None):
    self.student_to_plants = defaultdict(list)
    if not students:
      students = [
          'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet',
          'Ileana', 'Joseph', 'Kincaid', 'Larry'
      ]
    students.sort()
    diagram_list = diagram.split('\n')
    for row in diagram_list:
      for index, char in enumerate(row):
        self.student_to_plants[students[index / 2]].append(_CODE_TO_PLANT[char])

  def plants(self, student):
    return self.student_to_plants[student]
