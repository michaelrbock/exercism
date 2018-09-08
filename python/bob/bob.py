def hey(phrase):
  if not phrase or phrase.isspace():
    return 'Fine. Be that way!'

  question = phrase.strip()[-1] == '?'
  yelling = phrase.isupper()

  if question and yelling:
    return "Calm down, I know what I'm doing!"
  elif question:
    return 'Sure.'
  elif yelling:
    return 'Whoa, chill out!'
  return 'Whatever.'
