def distance(strand_a, strand_b):
  if len(strand_a) != len(strand_b):
    raise ValueError('Strands must be the same length.')
  # Idea:
    # Go thru strings, comparing char at each index & adding to count of diffs.
      # O(n)
  hamming = 0
  for i in range(len(strand_a)):
    if strand_a[i] != strand_b[i]:
      hamming += 1
  return hamming
