_BRACKET_PAIRS = {')': '(', ']': '[', '}': '{'}


def is_paired(input_string):
  stack = []
  for char in input_string:
    # If opener: add to stack, if closer: pop and check for balance, if other
    # char: skip.
    if char in _BRACKET_PAIRS.values():
      stack.append(char)
    elif char in _BRACKET_PAIRS:
      if not stack or stack.pop() != _BRACKET_PAIRS[char]:
        return False
  return len(stack) == 0
