from discord.ext import commands

@commands.command()
async def RPS(ctx,*args):
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
      await print("WINE")
    elif person1 == "P" :
      await print("LOSE")
    elif person1 == "S" :
      await print("DRAW")
@RPS.error
async def clear_error(ctx,error):
  await ctx.send('error')
  await ctx.send(error)

def setup(bot):
  bot.add_command(RPS)
  