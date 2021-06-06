import requests
import json 

def fetch(text):
  res = requests.get(text)
  response = json.loads(res.text)
  return response