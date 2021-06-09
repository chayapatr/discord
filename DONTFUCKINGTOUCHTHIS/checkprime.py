from discord.ext import commands

@commands.command(aliases=["prime"])
async def checkprime(ctx,*args):
  _idx = 0
  def input():
    nonlocal _idx
    _idx += 1
    return args[_idx - 1]
  async def print(str):
    await ctx.send(str)
  a = int(input())
  if a <= 0 or a == 1:
    await print("this is not a prime number.")
  else :
    for x in range(2,a) :
      ans = a % x
      if ans == 0 :
        break
    if ans == 0 :
      await print("this is not a prime number.")
    else :
      await print("this is a prime number.")

def setup(bot):
  bot.add_command(checkprime)