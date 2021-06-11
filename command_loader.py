import os
from importlib import import_module
from compiler import compile

def load(client):
  wd = os.getcwd()

  # set up native commands
  folder_path = wd + '/commands'
  error_module = []
  filelist = [f for f in os.listdir(folder_path) if f.endswith('.py')]

  for file in filelist:
    filename = file[:-3]
    print('Loading: ' + filename)
    # try:
      # load and set up function
    command_module = import_module('commands.' + filename)
    command_module.setup(client)
    # except:
    #   print("An error has occured")
    #   error_module += [filename]

  # compile user code
  files = [ f[:-3] for f in os.listdir(wd + '/user_src') if f.endswith('.py')]
  if not 'DONTFUCKINGTOUCHTHIS' in os.listdir():
    os.system('mkdir DONTFUCKINGTOUCHTHIS')
  for filename in files:
    print('Compling: ' + filename)
    compile(filename,wd + '/user_src/{}.py'.format(filename), wd + '/DONTFUCKINGTOUCHTHIS/{}.py'.format(filename))

  # set up user command
  folder_path = wd + '/DONTFUCKINGTOUCHTHIS'
  filelist = [f for f in os.listdir(folder_path) if f.endswith('.py')]

  for file in filelist:
    filename = file[:-3]
    print('Loading: ' + filename)
    try:
      # load and set up function
      command_module = import_module('DONTFUCKINGTOUCHTHIS.' + filename)
      command_module.setup(client)
    except:
      print("An error has occured")
      error_module += [filename]

  # try:
  command_module = import_module('grader.main')
  command_module.setup(client)
  #   print('Loaded: Grader')
  # except:
  #   print('Failed to load: Grader')
  #   error_module += ['Grader']

  return error_module