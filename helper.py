# IDEA
import requests
import json 

def fetch(text):      
  res = requests.get(text)
  response = json.loads(res.text)
  return response

def printList(listname,l):
  print(listname)
  for x in l:
    print(x)
  print('-------------------')