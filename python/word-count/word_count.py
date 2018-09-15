import re
from collections import Counter


def word_count(phrase):
  phrase = phrase.lower().replace('_', " ")
  rgx = re.compile(r"([\w][\w']*\w|\w)")
  return Counter(rgx.findall(phrase))