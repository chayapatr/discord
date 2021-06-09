import os

wd = os.getcwd()
grader_path = wd + '/grader'

code_path = wd + '/grader/code.py'

# run test
def run_test(question):
  question_path = wd + '/grader/challenge/'
  # get question list
  questions = [e for e in os.listdir(question_path) if not os.path.isfile(question_path + e)]
  
  print(questions)
  if not question in questions:
    # handle invalid question name
    pass

  # get filepath
  testpath = question_path + question
  outputfile_path = wd + '/grader/out'
  inputfolder_path = testpath + '/in/'
  expectedfolder_path = testpath + '/expected/'
  
  testcase_number = len (os.listdir(inputfolder_path))

  # loop testcase
  result = []
  for i in range(testcase_number):
    inputfile_path = inputfolder_path + str(i)
    expectedfile_path = expectedfolder_path + str(i)

    # run test
    os.system('python3 {0} < {1} > {2}'.format(code_path,inputfile_path, outputfile_path))

    result.append(check(outputfile_path,expectedfile_path))
    
  return result


def check(outputfile_path, expectedfile_path):
  output = open(outputfile_path, "r")
  expected = open(expectedfile_path, "r")

  output_read = open(outputfile_path, "r").read()
  expected_read = open(expectedfile_path, "r").read()

  output_read = output_read.replace("\n","")
  expected_read = expected_read.replace("\n","")

  # if output_read[-1] == "\n":
  #   output_read = output_read[0:-1]
  # if expected_read[-1] == "\n":
  #   expected_read = expected_read[0:-1]

  output.close()
  expected.close()

  return [output_read == expected_read, expected_read, output_read]
