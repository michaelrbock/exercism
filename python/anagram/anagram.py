from collections import Counter


def find_anagrams(word, candidates):
  word_counter = Counter(word.lower())
  results = []
  for candidate in candidates:
    if (Counter(candidate.lower()) == word_counter and
        word.lower() != candidate.lower()):
      results.append(candidate)
  return results
