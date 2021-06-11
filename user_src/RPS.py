from random import choice

person1 = input("choose R(ROCK) P(PAPER) S(SCISSOR) : ")
bot = choice (["ROCK","PAPER","SCISSOR"])

person1 = person1.upper()

if person1 in ["ROCK", "PAPER", "SCISSORS"]:
  person1 = person1[0]

if not person1 in ["R", "P", "S"]:
  print("Please choose between R(Rock), P(Paper), or S(Scissors)")

if bot == "ROCK":
  if person1 == "R":
    print("DRAW")
  elif person1 == "P" :
    print("WIN")
  elif person1 == "S" :
    print("LOSE")
elif bot == "PAPER":
  if person1 == "R":
    print("LOSE")
  elif person1 == "P" :
    print("DRAW")
  elif person1 == "S" :
    print("WIN")
elif bot == "SCISSOR":
  if person1 == "R":
    print("WIN")
  elif person1 == "P" :
    print("LOSE")
  elif person1 == "S" :
    print("DRAW")