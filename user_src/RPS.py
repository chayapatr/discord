from random import choice

person1 = input("choose R(ROCK) P(PAPER) S(SCISSOR) : ")
bot = choice (["ROCK","PAPER","SCISSOR"])

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
    print("WINE")
  elif person1 == "P" :
    print("LOSE")
  elif person1 == "S" :
    print("DRAW")