import re

def format_argument(message):
  command_name_size = message.find(' ')
  message = message[command_name_size + 1 : ]
  question_name_size = message.find(' ')
  question = message[ : question_name_size]
  message = message[ question_name_size + 1 : ]
  print(question)
  print(re.sub(r'input\([^\)]*\)','input()',message))
  return question, re.sub(r'input\([^\)]*\)','input()',message)

def format_code(code):
  prefix = """import multiprocessing
import sys
import time

def runner():
  sys.stdin = open(0)
"""
  suffix = """if __name__ == '__main__':
  p = multiprocessing.Process(target=runner)
  start = time.time()
  p.start()
  while (time.time() - start) <= 1 and p.is_alive():
    pass
  if p.is_alive():
    print("Terminate  - Exceed Limit Time")
    p.terminate()
    p.join()
"""
  return prefix+"  "+ code.replace("\n","\n  ")+"\n\n"+suffix

def format_result(result, inputfolder_path):
  string = ""
  correct = True
  for enum, i in enumerate(result):
    status, expected, output = i
    if status:
      string += "`Pass`: Test # {0} :)\n".format(enum+1)
    else:
      f = open(inputfolder_path+str(enum), "r")
      string += "`Fail`: Test # {0} :(\n\n__Input__\n{1}\n\n__Expected__\n```{2}```\n\n__Return__\n```{3}```\n".format(enum+1, f.read().replace("\n", " "), expected, output if output != "" else "Nothing")
      correct = False
      f.close()
      break
      
  return [correct, string]