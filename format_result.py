def format_result(result, inputfolder_path):
  string = ""
  correct = True
  for enum, i in enumerate(result):
    status, expected, output = i
    if status:
      string += "`Pass`: Test # {0} :)\n".format(enum+1)
    else:
      f = open(inputfolder_path+str(enum), "r")
      string += "`Fail`: Test # {0} :(\n\n__Input__\n{1}\n\n__Expected__\n{2}\n\n__Return__\n{3}\n".format(enum+1, f.read().replace("\n", " "), expected, output if output != "" else "Nothing")
      correct = False
      f.close()
      break
  return [correct, string]