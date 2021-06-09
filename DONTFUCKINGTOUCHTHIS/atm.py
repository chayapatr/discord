from discord.ext import commands

@commands.command()
async def atm(ctx,*args):
  _idx = 0
  def input(*argumentholder):
    nonlocal _idx
    _idx += 1
    return args[_idx - 1]
  async def print(*message):
    await ctx.send(''.join([str(x) for x in message]))
  cost = int(input("Enter amount of product : "))
  paid = int(input("Enter amount of paid : "))
  total = paid - cost
  await print("Change money total : ", total)
  b100 = total // 100
  lot2 = total - (b100 * 100)
  b20 = lot2 // 20
  lot3 = lot2 - (b20 * 20)
  # await print(total,lot2,lot3)
  b2 = lot3 // 2
  await print("100 bath = ", b100 ,"\n 20 bath = ", b20 ,"\n  2 bath = ", b2) 

def setup(bot):
  bot.add_command(atm)
  