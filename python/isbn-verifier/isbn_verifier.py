def verify(isbn):
  isbn = isbn.replace('-', '')
  if len(isbn) != 10:
    return False
  total = 0
  for i, num in enumerate(isbn):
    if not num.isdigit() and num != 'X':
      return False
    total += 10 if num == 'X' else int(num) * (10 - i)
  return total % 11 == 0
