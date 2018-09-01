from collections import Counter

def is_pangram(sentence):
  sentence_counter = Counter(sentence)
  # 97 is ASCII code for 'a' and there are 26 letters in English.
  for i in xrange(97, 97+26):
    if chr(i) not in sentence_counter and chr(i).upper() not in sentence_counter:
      return False
  return True
