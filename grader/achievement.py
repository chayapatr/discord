from replit import db
from queue import PriorityQueue
# from random import randint
import json
from os import getcwd

def set_achievement(author, challenge):
  score = open(getcwd() + "/grader/challenge/score.json", "r")
  keys = db.keys()
  data = json.load(score)
  
  if not author in keys:
    db[author] = [0, []]
  # if author in keys:
  if not challenge in db[author][1]:
    db[author][1].append(challenge)
    db[author][0] += int(data[challenge])
    return [db[author], int(data[challenge])]
  else:
    return -1

def get_achievement(author):
  keys = db.keys()
  if author in keys:
    return db[author]
  else:
    # return "author not found"
    return None

def get_ranking():
  keys = db.keys()
  table = PriorityQueue()
  # res = ""
  # rank = 1

  for key in keys:
    table.put((-db[key][0], key))

  res = []
  while not table.empty():
    item = table.get()
    res.append(item[1])
    # res += "**#{0} <@{1}>**: {2} {3}\n".format(rank, item[1],-item[0], "Points" if -item[0] > 1 else "Point")
    # rank += 1

  return res

def clear():
  keys = db.keys()
  for key in keys:
    del db[key]

# clear()

# print(set_achievement("Pub","add"))
# print(set_achievement("Keen","add"))
# print(set_achievement("Ta","add"))
# print(set_achievement("Thee","add"))
# print(get_achievement("Pub"))
# get_ranking()