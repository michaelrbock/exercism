def sum_of_multiples(limit, multiples):
  result = 0
  for i in xrange(limit):
    if any(i % m == 0 for m in multiples):
      result += i
  return result
