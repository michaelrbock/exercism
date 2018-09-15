_ALLERGIES = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'cats'
}


class Allergies(object):

  def __init__(self, score):
    self.allergies = []
    for value, name in _ALLERGIES.iteritems():
      if score & value:
        self.allergies.append(name)

  def is_allergic_to(self, item):
    return item in self.allergies

  @property
  def lst(self):
    return self.allergies
