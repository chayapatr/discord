#!/opt/virtualenvs/python3/bin/python
import random
import math
import os

def geninput() -> str:
  res = ""
  n = random.randint(1,10)
  res += str(n) + "\n"
  for x in range(n):
    res += str(random.randint(1,10)) + "\n"
  return res

path = os.getcwd()

test_case_num = 10

source = open("{}/code.py".format(path), "r")
source_read = source.read()

os.system("rm -rf in expected")
os.system("mkdir in expected")

for i in range(0,test_case_num):
  with open("in/{}".format(i), "w") as in_file:
    in_file.write(geninput())

for i in range(0,test_case_num):
  with open("{0}/expected/{1}".format(path,i), "w") as expected_file:
    expected_file.write("")

for i in range(0,test_case_num):
  os.system('python3 {path}/code.py < {path}/in/{0} > {path}/expected/{1}'.format(i, i, path=path))

source.close()