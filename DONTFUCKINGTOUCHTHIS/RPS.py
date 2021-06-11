from discord.ext import commands

@commands.command()
async def RPS(ctx,*args):
  """
  <a compiled function>
  """

  _idx = 0
  def input(*argumentholder):
    nonlocal _idx
    _idx += 1
    return args[_idx - 1]
  async def print(*message):
    await ctx.send(''.join([str(x) for x in message]))
  from random import choice
  
  person1 = input("choose R(ROCK) P(PAPER) S(SCISSOR) : ")
  bot = choice (["ROCK","PAPER","SCISSOR"])
  
  person1 = person1.upper()
  
  if person1 in ["ROCK", "PAPER", "SCISSORS"]:
    person1 = person1[0]
  
  if not person1 in ["R", "P", "S"]:
    await print("Please choose between R(Rock), P(Paper), or S(Scissors)")
  
  if bot == "ROCK":
    if person1 == "R":
      await print("DRAW")
    elif person1 == "P" :
      await print("WIN")
    elif person1 == "S" :
      await print("LOSE")
  elif bot == "PAPER":
    if person1 == "R":
      await print("LOSE")
    elif person1 == "P" :
      await print("DRAW")
    elif person1 == "S" :
      await print("WIN")
  elif bot == "SCISSOR":
    if person1 == "R":
      await print("WIN")
    elif person1 == "P" :
      await print("LOSE")
    elif person1 == "S" :
      await print("DRAW")
@RPS.error
async def clear_error(ctx,error):
  print(error)

def setup(bot):
  bot.add_command(RPS)
  