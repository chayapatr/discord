from .template import getprefix, getsuffix

def compile(filename, filepath, outputpath):
  code = getcode(filename,filepath)
  # print(code)
  savecode(code,outputpath)

def getcode(filename, filepath):
  output = ""
  output += getprefix(filename) + "\n"
  with open(filepath,'r') as f:
    for line in f:
      output += "  " + line.replace("print","await print")
  output += getsuffix(filename)
  return output

def savecode(code, outputpath):
  with open(outputpath, 'w') as f:
    f.write(code)