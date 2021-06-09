def format_result(result):
  string = ""
  correct = True
  for enum, i in enumerate(result):
    status, expected, output = i
    if status:
      string += "Test # {0} Pass :)\n".format(enum+1)
    else:
      string += "Test # {0} Fail :( -> Expected {1} Return {2}\n".format(enum+1, expected, output)
      correct = False
      break
  return [correct, string]